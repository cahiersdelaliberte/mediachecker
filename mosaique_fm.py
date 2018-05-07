# -*- coding: utf-8 -*-
"""
Created on Mon Apr 23 17:44:20 2018

@author: houeslat
Scraping du side mosaique FM
"""

############################
######### MOSAIQUE #########
############################


#récupérer les urls des articles de la rubrique Politique
artical_link=[]  
url_info = "/fr/actualite-politique-tunisie/" 
url = "https://www.mosaiquefm.net/fr/actualites/actualite-politique-tunisie/4/"
#pour cet exemple, on scrape uniquement les 4 premières pages de recherche
nb_pages = 4
for num_page in range(1, nb_pages + 1):
    soup = BeautifulSoup(urllib.request.urlopen(url+str(num_page))) #on récupère le code source de chaque url (page de recherche)
    for a in soup.find_all('a', href=True): 
        #on cherche dans toutes les balise <a> les "href" dont l'url commence par /r/
        if url_info in a['href']:
            artical_link.append("https://www.mosaiquefm.net"+a['href'])


title    = []
article  = []
key_word = []
date_article =  []
for link in artical_link:
    page = requests.get(link) #ouvrir l'url du CV
    tree = lxml_html.fromstring(page.content)
    key_word.append('Politique')
    part1 = tree.xpath('//div/p/strong/text()')  #ça fonctionne
    part2 = tree.xpath('//div[@class="desc descp__content"]/p/text()') #ça fonctionne
    article.append(' '.join(part1+part2))
    date_article.append(tree.xpath('//div[@class="date text-center"]/text()')[0].strip()) #ça fonctionne
    title.append(tree.xpath('//div/h1[@class="title"]/text()')[0].strip())


#Consolider les données scrapées dans un dataframe 
X=np.column_stack((artical_link,key_word,title,date_article,article)) 
df=pd.DataFrame(X)
df.columns = ['url','Section','Titre','Date','Article']
X=np.column_stack((date_article,artical_link,key_word,title,article)) 


