# mediachecker

## Introduction


## Data

`hpm_legistunisia.csv`
Articles Huff. Post Maghreb, metadata + text. Obtenus par requête : Législatives + Tunisia.

`MosaiqueFM_v0.csv`
Site Mosaique Fm. Rubrique Politique.

`data.json`
Tous les articles récents concernant la Tunisie. Obtenus via newsapi.
* mots clefs `tunis`, `tunisie` 
* période 2 derniers mois

`liste_deputes.csv`
Src : https://majles.marsad.tn/2014/fr/assemblee
> À améliorer : texte dans la colonne rang pas un chiffre et garder uniquement la partie numériquede la colonne Nombre de voix

`liste_deputes_2.csv`
`liste_deputes.csv` enrichi.

`liste_deputes_3.csv`
`liste_deputes_2.csv` enrichi de l'âge et de l'année de naissance.

## Sites utilisés

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
Exemple d'article : https://www.huffpostmaghreb.com/entry/le-fmi-approuve-le-decaissement-de-2573-millions-de-dollars-au-profit-de-la-tunisie_mg_5ab77d56e4b008c9e5f83125?utm_hp_ref=mg-economie-tunisie 

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
