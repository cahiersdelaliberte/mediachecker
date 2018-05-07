# -*- coding: utf-8 -*-
"""
Created on Sun Apr 22 21:32:04 2018

@author: houeslat
Récupérer la liste des députés à partir du site Majles https://majles.marsad.tn/2014/fr/assemblee
"""

###########################################################################
######################   Importer les librairies   ########################
###########################################################################
import sys
reload(sys)
sys.setdefaultencoding('utf-8')   
import numpy as np
import pandas as pd
import re
import urllib
from lxml import html as lxml_html
import requests
from bs4 import BeautifulSoup
from scipy import *
import datetime
import re
from nltk.tokenize import TreebankWordTokenizer
tokenizer = TreebankWordTokenizer()

###########################################################################
######################   Définir les fonctions     ########################
###########################################################################
#Récupérer le rang du député en chiffre
def get_rank(x):
    if re.findall(r'\d+',x):
        return re.findall(r'\d+',x)[0]
    else:
        return 1

def get_text_html(link):
    """
    Remove HTML markup from the given string.

    :param html: the HTML string to be cleaned
    :type html: str
    :rtype: str
    """
    code_source = urllib.request.urlopen(link).read()
    html = code_source.decode('utf8')
    # First we remove inline JavaScript/CSS:
    cleaned = re.sub(r"(?is)<(script|style).*?>.*?(</\1>)", "", html.strip())
    # Then we remove html comments. This has to be done before removing regular
    # tags since comments can contain '>' characters.
    cleaned = re.sub(r"(?s)<!--(.*?)-->[\n]?", "", cleaned)
    # Next we can remove the remaining tags:
    cleaned = re.sub(r"(?s)<.*?>", " ", cleaned)
    # Finally, we deal with whitespace
    cleaned = re.sub(r"&nbsp;", " ", cleaned)
    cleaned = re.sub(r"  ", " ", cleaned)
    cleaned = re.sub(r"  ", " ", cleaned)
    cleaned = cleaned.encode('utf8').decode('unicode_escape')
    cleaned =  " ".join([','.join(tokenizer.tokenize(mot))   for mot in cleaned.split()  ])
    return cleaned.strip()

###########################################################################
######################   Importer les librairies   ########################
###########################################################################

metier_regex = r'(?<=Parcours professionnel).*?(?=Parcours politique)'
regex_region = r'(?<=\,).*'



name_list = []
region = []
nb_voix = []
rang = []
parti = []
annee_naissance = []
metier = []

#récupérer l'url des fiches des députés à partir du site de l'assemblée nationale
page_url = "https://majles.marsad.tn/2014/fr/assemblee"
dep_link=[]  
soup = BeautifulSoup(urllib.request.urlopen(page_url)) #on récupère le code source de chaque url (page de recherche)
for a in soup.find_all('a', href=True): 
    #on cherche dans toutes les balise <a> les "href" dont l'url commence par /r/
    if "elus" in a['href']:
        dep_link.append("https://majles.marsad.tn"+a['href'])



#récupérer les différentes informations relatives aux députés
for link in dep_link:
    page = requests.get(link) #ouvrir l'url 
    tree = lxml_html.fromstring(page.content)
    name_list.append(tree.xpath('//div/h1[@id="elu-nom"]/text()'))
    parti.append(tree.xpath('//div[@class="top-20"]/div/text()') [0])
    region.append(re.findall( regex_region , tree.xpath('//div[@class="top-30"]/div/text()') [0])[0].strip())
    nb_voix.append((re.findall(r'\d+', tree.xpath('//div[@class="top-30"]/div/text()')[-1].split(',')[0].strip())))
    rang.append(tree.xpath('//div[@class="top-30"]/div/text()')[-1].split(',')[1].strip())
    try:
        annee_naissance.append(2017 - int(re.findall(r'\d+', tree.xpath('//div[@class="grey"]/span/text()')[-1])[0]))
    except: 
        annee_naissance.append(0)
    try:
        metier.append(re.findall( metier_regex ,get_text_html(link))[0].strip())
    except: 
        metier.append("")



X=np.column_stack((name_list,parti,region,nb_voix,rang,annee_naissance,metier)) 
df_dep=pd.DataFrame(X)
df_dep.columns = ['Député','Parti polituque','Région','Nombre de voix','Rang dans la liste',"Année de naissance","Profession"]
df_dep.to_cvs('C:/Users/houeslat/Documents/DataForGood/data/liste_deputes.csv',encoding='utf8',index=False)



#récupérer le rang en chiffre des député     
df_dep['Rang dans la liste'] = df_dep['Rang dans la liste'].apply(lambda x : get_rank(x))




