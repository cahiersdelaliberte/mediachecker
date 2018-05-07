#!/bin/bash

# Python 3.5
# Initialisation d'un environnement virtuel toto en python 3.5 : 
# pew new toto --python=python3.5

all: clean

install:
	@echo "> Installation du script newsapi..."
	pip install newsapi-python
	@echo "> Installation du script mosaïque fm..."
	pip install beautifulsoup4
	pip install lxml
	pip install numpy
	pip install pandas

newsapi:
	python articles/newsAPIdata4good.py

mosaique:
	python articles/mosaique_fm.py

clean:
	find . -name '*.pyc' -exec rm \{\} \;
