# mediachecker

## Introduction

Ce dépôt rassemble les travaux de collaboration [dataforgoodfr](http://www.dataforgood.fr) - [cahiers de la liberté](http://www.cahiersdelaliberte.org) réalisés au printemps 2018.

## Installation

Ce dépôt requiert Python 3.7.
Pour tout installer, exécuter :

```sh
make install
```

Noter que chaque script peut être installé séparément.  
Voir le fichier `Makefile` pour en savoir plus.

## Exécution

> Requiert un fichier `key_newapi` contenant l'identifiant individuel à fournir pour la récupération des articles [NewsAPI.org](NewsAPI.org)

Afin d'exécuter tous les scripts, appeler :

```sh
python main.py
```
> Ignore néanmoins les recherches de représentation du fact checking.

## Contenu

### Moissonnage de données de référence

__Répertoire `/indices`.__

#### Liste des députés de l'Assemblée des Représentants du Peuple

`liste_deputes.py` > `liste_deputes.csv`  
Src : https://majles.marsad.tn/2014/fr/assemblee

Les données générées sont mémorisées dans :
* `data/liste_deputes.csv` (moissonnée en 08/2019)
  * Cette liste est retranscrite pour le fact checking (cf.`fact_checking/source/key_words.py`).
* `data/liste_deputes_2018.csv` (moissonnée en 2018 pour dataforgoodfr)


### Moissonnage d'articles

__Répertoire `/articles`__

#### Articles MosaïqueFM

`mosaique_fm.py` > `mosaique.csv`

Récupère les derniers articles de la [rubrique Politique](https://www.mosaiquefm.net/fr/actualites/actualite-politique-tunisie/4/).

#### Articles divers via NewsAPI

`newsAPIdata4good.py` > `tunis.json` (pour une recherche du mot clef `tunis`)

Récupère tous les articles récents concernant la Tunisie via [NewsAPI.org](NewsAPI.org).  
Sélectionne les articles par mots clefs pouvant être en français ou en arabe.

> Requiert un fichier `key_newapi` contenant l'identifiant individuel à fournir au `NewsApiClient`  
> (et un retour à la ligne pour éviter `apiKeyInvalid`).

Endpoint principal requêté : [/v2/everything](https://newsapi.org/docs/endpoints/everything)

### Fact checking

__Répertoire `/fact_checking`.__

`fact_checking.py`

Pour un article donné, `fact_checking.py` recherche la liste des mots clefs présents parmi la liste définie dans `key_words.py`.

#### Recherches sur la représentation des résultats

##### Notebook HTML

`D4G_Fact_checking_mosaiqueFM.py` : script de vérification des articles mosaique fm  
`D4G_Fact_checking_mosaiqueFM.html` : notebook vérifiant les articles mosaique fm

##### Test de surlignage JS/HTML

`utils/surligne.js` : script de surlignage de mots de texte  
`utils/page_test.html` : page appelant les fonctions de `surligne.js` pour les tester dans les navigateurs
> ouvrir `page_test.html` dans un navigateur pour exécuter les tests

### Clustering (ou production de nuage de mots)

__Répertoire `/clustering`.__

`clustering_news.py` : script de production de nuage de mots par article 
    pour une liste d'articles issus de [News API](https://newsapi.org)

`/inputs/stopwords-fre.txt` : liste de mots en français à ignorer à la production des nuages de mots

## Sites cibles

Portail open data cahiers de la liberté :
https://www.data4tunisia.org et ses [moissonneurs](https://github.com/cahiersdelaliberte/data4tunisia/tree/e1472ed43842e1623f62dc1a73ce7f605d924531/udata/harvest/backends).

Portail de fact checking cahiers de la liberté :
http://birrasmi.tn

## Divers

Nouvelle version de DBnomics pour les données économiques :  
http://next.nomics.world/

Logiciel de fact checking :  
https://www.inria.fr/centre/saclay/actualites/un-logiciel-de-fact-checking-pour-comprendre-le-monde-qui-nous-entoure

Datification d'évènements AFP :  
https://www.afp.com/fr/lagence/MediaLab/ASRAEL

Fact checking & IA :  
https://factmata.com

Exemple de source de news :   
https://www.huffpostmaghreb.com/news/politique-tunisie/
Exemple d'article :  https://www.huffpostmaghreb.com/entry/le-fmi-approuve-le-decaissement-de-2573-millions-de-dollars-au-profit-de-la-tunisie_mg_5ab77d56e4b008c9e5f83125?utm_hp_ref=mg-economie-tunisie 

TV - Watania replay :  
https://www.youtube.com/user/televisiontunisie6

Aggrégation de l'actualité / identification de thématiques :  
https://newsapi.org/s/google-news-api

Détection et extraction mondiale d’événements en temps réel (identification des groupes d'articles dans différentes langues rapportant d'un même événement + regroupement en 1) :  
http://eventregistry.org/

Speech to text en python :  
https://www.alexkras.com/transcribing-audio-file-to-text-with-google-cloud-speech-api-and-python/

A scrapper :  
https://www.shemsfm.net/fr/actualites/2

Site du Ministère de l'Industrie :  
http://www.data4tunisia.org/fr/organizations/ministere-de-lindustrie-de-lenergie-et-des-mines/

Site du Ministère de la Culture :  
http://www.data4tunisia.org/fr/organizations/ministere-de-la-culture/

Elus de l'Assemblée des Représentants du Peuple :  
https://majles.marsad.tn/2014/fr/assemblee

Huffpost Tunisie :  
https://www.huffpostmaghreb.com/tunisie/

Kapitalis :  
http://kapitalis.com/tunisie/

Businessnews.tn :  
https://www.businessnews.com.tn/
