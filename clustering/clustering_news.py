# -*- coding: utf-8 -*-
"""
Created on Tue May 22 19:41:25 2018

@author: samah.ghalloussi
"""

import json, csv
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.preprocessing import StandardScaler
import pandas as pd
from sklearn import cluster
import numpy as np
import matplotlib.pyplot as plt
#from sklearn.preprocessing import StandardScaler
from wordcloud import WordCloud
from collections import Counter
import csv, unicodedata


def strip_accents(s):
     try : s = s.decode('utf-8') 
     except : s = str(s)
     return ''.join(c for c in unicodedata.normalize('NFD', s) 
                    if unicodedata.category(c) != 'Mn')  
     
STOPWORDSFR = open('stopwords-fre.txt', 'r').readlines()
tabSW = []
for line in STOPWORDSFR :
    tabSW.append(line[0:-1]) 

    
def removeStopwords(data):
	chaine = ' '
	for word in data.lower().split() :
		
		if word not in tabSW:
			chaine = chaine + word + " "
			
	return chaine[1:len(chaine)]

def deletion(deltab, replacement, text):
    
    for elem in deltab:
        text.replace(elem, replacement)
    
    return text

#wordcloud generation for each cluster
def generateWC(wc, name, dico, nbclusters, y_pred):
    
    plt.figure(figsize=(17, 9.5))
    plt.subplots_adjust(left=.001, right=.999, bottom=.001, top=.96, wspace=.05, hspace=.01)          
    plot_num = 1
    print("wordcloud", name)
    for label in dico:
         nbdim = int(nbclusters/3) #right sizing for 9 clusters
         plt.subplot(nbdim, nbdim, plot_num) 
        #        fig, ax = plt.subplots(figsize=(16, 12))
         try : emailsWC = wc.generate(dico[label].replace("'", " "))
         except: 
             emailsWC = wc.generate("none")
         plt.imshow(emailsWC)
         plt.axis("off")
         title = " ".join(['label_'+ str(label)+ " nbr_docs:" + str(Counter(y_pred)[label])])
         plt.title(title)
         plot_num += 1
        
         if plot_num > nbclusters :
             break
    
    plt.savefig('out-wc_' + name + '.png') #, bbox_inches='tight', dpi = 900, transparent = True)
#    plt.show()
    plt.close()
    
def newsjsontocsv(inpath, outpath):
    header = []
    with open(inpath, 'r') as data_file:
        jsonarticles = json.load(data_file)
        with open(outpath, 'w') as csvfile:
            w = csv.writer(csvfile, lineterminator='\n')
#            w.writerow(rawIndex)
            for article in jsonarticles['articles'] :
                for elem in article :
                    header.append(elem)
                break
            w.writerow(header)   
            for article in jsonarticles['articles'] :
                try :
                    rawIndex = []
                    article['source'] = article['source']['name']
                    article['description'] = article['description'].replace("[Tunis Afrique Presse]", '')
                    for elem in article :
                        rawIndex.append(strip_accents(article[elem]).encode('utf-8'))
                            
                    w.writerow(rawIndex)
                except :
                    pass
#                    print(article['title'])


def datacsv(outpath, nbclusters=9):
    data = pd.read_csv(outpath)
    df = pd.DataFrame(columns = data.columns)
    df = data[['source', 'author', 'title', 'description', 'url', 'urlToImage', 'publishedAt']]
    
    vect = TfidfVectorizer(stop_words=tabSW, max_df=0.90, min_df=1)#, ngram_range=(1, 2))
#        vect = TfidfVectorizer(tokenizer=tokenize, stop_words='french', max_df=0.50, min_df=2)

#    X = vect.fit_transform(data["title"].astype('U'))
#    X = vect.fit_transform(data["description"].astype('U'))
    X = vect.fit_transform(data["description"] + ' ' + data["title"])
#    X = StandardScaler(with_mean=False).fit_transform(X)
    
    #vocabulary
    feature_names = vect.get_feature_names()  
    vocab = open("out-clusteringVocabALL.txt", "w")
    for i, name in enumerate(feature_names):
        vocab.write(str(i) + '\t' + name + '\n')
    vocab.close() 
    
#    for i, elem in enumerate(X):
#        print ('\n', i, data["title"][i])
#        for wordline in str(X[i]).split('\n') :
#             index = wordline.split('\t')[0].split()[-1].replace(')','')
#             print(feature_names[int(index)], '-', wordline.split('\t')[1])
    
    X = X.toarray()
    n_samples, n_features = X.shape
    print ("n_samples:", n_samples, "n_features:", n_features)
    
    algorithm = cluster.SpectralClustering(n_clusters=nbclusters,
                                      eigen_solver='arpack',
                                      affinity="nearest_neighbors",
                                      assign_labels='discretize',
                                      random_state=73)
#    algorithm = cluster.DBSCAN(eps=.2)
#    algorithm = cluster.DBSCAN(eps=0.3)
#    algorithm = cluster.AgglomerativeClustering(n_clusters=nbclusters, affinity='euclidean')
    algorithm.fit(X)
    analyse(nbclusters, algorithm, X, data)
     

def analyse(nbclusters, algorithm, X, data) :

    if hasattr(algorithm, 'labels_'):
        y_pred = algorithm.labels_.astype(np.int)
    else:
        y_pred = algorithm.predict(X)

    dicoContent, dicoTitle = {}, {}
    dicoSources, dicoAuthors = {}, {}
    for i, value in enumerate(y_pred):
#            print (i, value, data["created_at"][i], Counter(y_pred)[value])            
            try : dicoContent[value] += " " + data["description"][i]
            except : dicoContent[value] = data["description"][i]
                
            try : dicoTitle[value] += " " + data["title"][i]
            except : dicoTitle[value] = data["title"][i]
            
            author = deletion(["b\'","\'"], '', data["author"][i])
            try : dicoAuthors[value] += " " + author
            except : dicoAuthors[value] = author
             
            deltab = [".", "/", ":", "-"]
            url = deletion(deltab, '', data["url"][i])
            try : dicoSources[value] += " " + url
            except : dicoSources[value] = url
            
    with open("out-ArticlesClusters_"+str(nbclusters)+".csv", 'w') as csvfileWriter:
        w = csv.writer(csvfileWriter, lineterminator='\n')
        header = ['source', 'author', 'title', 'description', 'url', 'urlToImage', 'publishedAt']
#        header = ["created_at", "body", "type", "cluster"]
        w.writerow(header)
        for i, value in enumerate(y_pred):
            raw = [value, data["source"][i], data["title"][i], data["description"][i], data["url"][i], data["publishedAt"][i]]
            w.writerow(raw)
                
#    for l in sorted(dicoContent) :        
#        print(l, '---', dicoFrom[l], dicoContent[l])
#                

    print (Counter(y_pred))
    
    #################################

    wc = WordCloud(mode="RGB", stopwords=tabSW, background_color=None, max_font_size=40, max_words=100, relative_scaling=0.5)
#    generateWC(wc, "Sources_"+str(nbclusters), dicoSources, nbclusters, y_pred)
#    generateWC(wc, "Authors_"+str(nbclusters), dicoAuthors, nbclusters, y_pred)
    generateWC(wc, "Title_"+str(nbclusters), dicoTitle, nbclusters, y_pred)
    generateWC(wc, "Content_"+str(nbclusters), dicoContent, nbclusters, y_pred)
    
    ##############################################################################
    
    
inpath = 'tunis.json'
outpath = 'out-datatunis.csv'
newsjsontocsv(inpath, outpath)
datacsv(outpath)
