#!/bin/bash

# Python 3.5
# Initialisation d'un environnement virtuel toto en python 3.5 : 
# pew new toto --python=python3.5

all: clean

install:
	pip install newsapi-python

newsapi:
	python articles/newsAPIdata4good.py

clean:
	find . -name '*.pyc' -exec rm \{\} \;
