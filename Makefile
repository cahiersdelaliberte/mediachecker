#!/bin/bash

# Python 3.6+
# Initialisation d'un environnement virtuel toto en python 3.6 : 
# pew new toto --python=python3.6

all: clean

install: install-newsapi install-mosaique install-clusters
	@echo "> Etes-vous bien en python 3.6+ ?"
	python --version


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


clean:
	find . -name '*.pyc' -exec rm \{\} \;
