# mediachecker

## Introduction

Ce dépôt rassemble les travaux de collaboration [dataforgoodfr](http://www.dataforgood.fr) - [cahiers de la liberté](http://www.cahiersdelaliberte.org) réalisés au printemps 2018.

## Data & Scripts

`hpm_legistunisia.csv`  
Articles Huff. Post Maghreb, metadata + text. Obtenus par requête : Législatives + Tunisia.

`mosaique_fm.py` > `MosaiqueFM_v0.csv`  
Site Mosaique Fm. Rubrique Politique.

`liste_deputes.py` > `liste_deputes_3.csv`  
Src : https://majles.marsad.tn/2014/fr/assemblee

`newsAPIdata4good.py`  
> Requiert un fichier `key_newapi` contenant l'identifiant individuel à fournir au `NewsApiClient` (et un retour à la ligne pour éviter `apiKeyInvalid`).

Récupère tous les articles récents concernant la Tunisie. Obtenus via `NewsAPI.org`.  
Il produit `tunis.json` : les dernières 100 publications contenant le mot `tunis`.  
Et, dans sa version précédente, a produit `data.json` :
* mots clefs `tunis`, `tunisie` 
* période 2 derniers mois
Et la librairie employée :
https://github.com/mattlisiv/newsapi-python

La version suivante crée :
`tunis-ar.json` : résultat arabe pour mot clef en français `tunis`.
`تونس.json` :  résultat arabe pour mot clef en arabe `تونس` (mais soucis d'encodage)
`arabicresultsتونس.json` : résultat arabe pour mot clef en arabe `تونس` (sans problématique d'encodage grâce au passage à python 3 ?) ; ce JSON n'est pas aimé par les éditeurs mais est bien formé.


## Fact checking

`D4G_Fact_checking_mosaiqueFM.py` : script de vérification des articles mosaique fm  
`D4G_Fact_checking_mosaiqueFM.html` : notebook vérifiant les articles mosaique fm

`surligne.js` : script de surlignage de mots de texte  
`page_test.html` : page appelant les fonctions de `surligne.js` pour les tester dans les navigateurs
> ouvrir `page_test.html` dans un navigateur pour exécuter les tests



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
