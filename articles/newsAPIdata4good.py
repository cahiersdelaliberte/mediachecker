# -*- coding: utf-8 -*-
"""
Created on Mon Apr 16 20:06:00 2018

@author: workspace
"""

import newsapi
from newsapi import NewsApiClient

import csv, json, sys

# Init: get your API-key on : https://newsapi.org/account
key = open('./articles/key_newapi', 'r').read()
newsapi = NewsApiClient(api_key=key[0:-1]) #API-KEY (do not release it) 

keyword = 'tunis'
data = newsapi.get_everything(q=keyword, language='fr', page_size=100)

with open(keyword + '.json', 'w') as outfile:
    json.dump(data, outfile, indent = 4)

# /v2/top-headlines
#top_headlines = newsapi.get_top_headlines(q='tunisia',
##                                          sources='bbc-news,the-verge',
##                                          category='business',
#                                          language='en')
#print(top_headlines)
# /v2/everything
#all_articles = newsapi.get_everything(q='bitcoin',
#                                      sources='bbc-news,the-verge',
#                                      domains='bbc.co.uk,techcrunch.com',
##                                      from_parameter='2017-12-01',
#                                      to='2017-12-12',
#                                      language='en',
#                                      sort_by='relevancy',
#                                      page=2)
#print(all_articles)

# /v2/sources
#sources = newsapi.get_sources()