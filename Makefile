#!/bin/bash

# Python 3.6+
# Initialisation d'un environnement virtuel toto en python 3.6 : 
# pew new toto --python=python3.6

all: clean run

install: install-marsad install-newsapi install-mosaique install-clusters
	@echo "> Etes-vous bien en python 3.6+ ?"
	python --version


install-marsad:
	@echo "> Installation du script de scrapping de la liste des députés..."
	pip install beautifulsoup4
	pip install lxml
	pip install numpy
	pip install pandas
	pip install nltk

marsad:
	python indices/liste_deputes.py 


install-newsapi:
	@echo "> Installation du script newsapi..."
	pip install newsapi-python

newsapi:
	python articles/newsAPIdata4good.py


install-mosaique:
	@echo "> Installation du script mosaïque fm..."
	pip install beautifulsoup4
	pip install lxml
	pip install numpy
	pip install pandas

mosaique:
	python articles/mosaique_fm.py


install-clusters:
	@echo "> Installation du script de clustering..."
	pip install sklearn
	pip install pandas
	pip install matplotlib
	pip install wordcloud

clusters:
	python clustering/clustering_news.py

run: clean
	python main.py

clean:
	find . -name '*.pyc' -exec rm \{\} \;
	@echo "> Suppression des éventuels fichiers générés..."
	rm -f mosaique.csv
	rm -f out-articlesClusters.csv
	rm -f out-articlesClusters_mosaique.csv
	rm -f out-articlesClusters_tunis.csv
	rm -f out-clusteringVocabALL.txt
	rm -f out-clusteringVocabALL_mosaique.txt
	rm -f out-clusteringVocabALL_tunis.txt
	rm -f out-wc_Content_9_mosaique.png
	rm -f out-wc_Content_9_tunis.png
	rm -f out-wc_Title_9_mosaique.png
	rm -f out-wc_Title_9_tunis.png
	rm -f tunis.csv
	rm -f tunis.json
