#!/usr/bin/python
"""
Created on Mon Apr 23 17:44:20 2018

@author: houeslat
Scraping du site mosaique FM
"""

############################
######### MOSAIQUE #########
############################


from bs4 import BeautifulSoup
import urllib.request
import requests
import lxml.html as lxml_html
import numpy as np
import pandas as pd


OUTPUT_PATH = './mosaique.csv'


#récupérer les urls des articles de la rubrique Politique
def scrap_political_articles_list():
    article_link=[]  
    url_info = "/fr/actualite-politique-tunisie/" 
    url = "https://www.mosaiquefm.net/fr/actualites/actualite-politique-tunisie/4/"
    #pour cet exemple, on scrape uniquement les 4 premières pages de recherche
    nb_pages = 4
    for num_page in range(1, nb_pages + 1):
        soup = BeautifulSoup(urllib.request.urlopen(url+str(num_page)), "html.parser") #on récupère le code source de chaque url (page de recherche)
        for a in soup.find_all('a', href=True): 
            #on cherche dans toutes les balise <a> les "href" dont l'url commence par /r/
            if url_info in a['href']:
                article_link.append("https://www.mosaiquefm.net"+a['href'])
    return article_link


def scrap_articles_information(articles_links):
    title    = []
    article  = []
    key_word = []
    article_date =  []
    for link in articles_links:
        page = requests.get(link) #ouvrir l'url du CV
        tree = lxml_html.fromstring(page.content)
        key_word.append('Politique')
        part1 = tree.xpath('//div/p/strong/text()')  #ça fonctionne
        part2 = tree.xpath('//div[@class="desc descp__content"]/p/text()') #ça fonctionne
        article.append(' '.join(part1+part2))
        article_date.append(tree.xpath('//div[@class="date text-center"]/text()')[0].strip()) #ça fonctionne
        title.append(tree.xpath('//div/h1[@class="title"]/text()')[0].strip())

    #Consolider les données scrapées dans un dataframe 
    X=np.column_stack((title, article_date, articles_links, article))
    df=pd.DataFrame(X)
    df.columns = ['titre', 'date', 'url', 'article']
    return df


def get_mosaique_articles():
    articles_dataframe = scrap_articles_information(scrap_political_articles_list())
    articles_dataframe.to_csv(OUTPUT_PATH, index=False)
    return OUTPUT_PATH
