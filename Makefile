#!/bin/bash

# Python 3.6
# Initialisation d'un environnement virtuel toto en python 3.6 : 
# pew new toto --python=python3.6

all: clean

install:
	@echo "> Etes-vous bien en python 3.6 ?"
	python --version
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
