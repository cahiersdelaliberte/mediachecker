"""
Created on Mon Apr 16 20:06:00 2018

@author: workspace
"""

import newsapi
from newsapi import NewsApiClient

import csv, json, sys

# Configuration
# Init: get your API-key on : https://newsapi.org/account
NEWS_API_KEY_PATH = './articles/key_newsapi'
SEARCH_LANGUAGE = 'fr'
SEARCH_KEYWORD = 'tunis'
OUTPUT_FILENAME = SEARCH_KEYWORD + '.json'
OUTPUT_ARTICLES_NUMBER = 10


def get_newsapi_articles():
    try:
        key = open(NEWS_API_KEY_PATH, 'r').read()
    except FileNotFoundError:
      print("Votre clef personnelle de connexion à News API n'a pas été trouvée.  \
            Veuillez la récupérer sur 'https://newsapi.org/register'  \
            et l'ajouter à './articles/key_newsapi'.")

    newsapi = NewsApiClient(api_key=key[0:-1]) # API-KEY (do not release it) 

    data = newsapi.get_everything(q=SEARCH_KEYWORD, language=SEARCH_LANGUAGE, page_size=OUTPUT_ARTICLES_NUMBER)

    with open(OUTPUT_FILENAME, 'w') as outfile:
        json.dump(data, outfile, indent = 4)




# /v2/top-headlines
# top_headlines = newsapi.get_top_headlines(q='tunisia',
##                                          sources='bbc-news,the-verge',
##                                          category='business',
#                                           language='en')
# print(top_headlines)

# /v2/everything
# all_articles = newsapi.get_everything(q='bitcoin',
#                                       sources='bbc-news,the-verge',
#                                       domains='bbc.co.uk,techcrunch.com',
##                                      from_parameter='2017-12-01',
#                                       to='2017-12-12',
#                                       language='en',
#                                       sort_by='relevancy',
#                                       page=2)
# print(all_articles)

# /v2/sources
# sources = newsapi.get_sources()
