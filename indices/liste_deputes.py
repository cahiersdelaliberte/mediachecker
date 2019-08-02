# -*- coding: utf-8 -*-
"""
Created on Sun Apr 22 21:32:04 2018

@author: houeslat
Récupérer la liste des députés à partir du site Majles https://majles.marsad.tn/2014/fr/assemblee
"""

###########################################################################
######################   Importer les librairies   ########################
###########################################################################
# import sys
# reload(sys)
# sys.setdefaultencoding('utf-8')   
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
parti = []
metier = []
annee_naissance_calculee = []

#récupérer l'url des fiches des députés à partir du site de l'assemblée nationale
page_url = "https://majles.marsad.tn/2014/fr/assemblee"
dep_link=[]  
soup = BeautifulSoup(urllib.request.urlopen(page_url)) #on récupère le code source de chaque url (page de recherche)
for a in soup.find_all('a', href=True): 
    #on cherche dans toutes les balise <a> les "href" dont l'url commence par /r/
    if "elus" in a['href']:
        dep_link.append("https://majles.marsad.tn"+a['href'])


#récupérer les différentes informations relatives aux députés
#exemple de fiche de député au 01/08/2019 :
#<div class="card is-elu mb-1 shadow" data-nom="Olfa Jouini" 
#    data-photo="/2014/uploads/images/olfa jouini.thumb50.png" 
#    data-bloc="Mouvement Nidaa Tounes" data-groupe_id="Mouvement_Nidaa_Tounes" 
#    data-liste="Union Patriotique Libre" data-circ="Tunis 1" 
#    data-genre="Femmes" data-age="0" data-profession="" data-siege="76">
#</div>
for link in dep_link:
    page = requests.get(link) #ouvrir l'url 
    tree = lxml_html.fromstring(page.content)
    name_list.append(tree.xpath('//div[@class="card is-elu mb-1 shadow"]/@data-nom'))
    parti.append(tree.xpath('//div[@class="card is-elu mb-1 shadow"]/@data-liste'))
    region.append(tree.xpath('//div[@class="card is-elu mb-1 shadow"]/@data-circ'))
    metier.append(tree.xpath('//div[@class="card is-elu mb-1 shadow"]/@data-profession'))
    annee_naissance_calculee.append(list(map(lambda age : (2019 - int(age)), tree.xpath('//div[@class="card is-elu mb-1 shadow"]/@data-age'))))
    

X=np.column_stack((name_list[0],parti[0],region[0],annee_naissance_calculee[0],metier[0])) 
df_dep=pd.DataFrame(X)
df_dep.columns = ['Député','Parti politique','Région', 'Année de naissance calculée', 'Profession']
df_dep.to_csv('./liste_deputes.csv',encoding='utf8',index=False)
