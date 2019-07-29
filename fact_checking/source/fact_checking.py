import re
import unicodedata


# éléments figurant dans le fichier
# https://docs.google.com/spreadsheets/d/12ElwEojNy9w7mYtwlERt_YcHwtcfAja3EhSrYWVu_TI/edit#gid=0
fact_buddies = [("emploi","chômage"),
("emploi","chômeurs"),
("emploi","chômeur"),
("emploi","emploi"),
("emploi","travail"),
("emploi","diplômé"),
("emploi","diplômés"),
("emploi","jeune diplômé"),
("emploi","jeunes diplômés"),
("emploi","PIB"),
("emploi","PNB"),
("activité","croissance"),
("activité","industrie"),
("activité","concurrence"),
("activité","marchés"),
("activité","marché"),
("activité","entreprise"),
("budget","budget"),
("budget","déficit"),
("budget","dette"),
("budget","équilibre"),
("budget","solde"),
("budget","dépenses"),
("budget","recettes"),
("fiscalité","taxe"),
("fiscalité","fiscalité"),
("fiscalité","impôt"),
("fiscalité","TVA"),
("fiscalité","impôt sur les sociétés"),
("sécurité sociale","sécurité sociale"),
("sécurité sociale","cotisation"),
("sécurité sociale","charge"),
("commerce international","commerce international"),
("commerce international","importations"),
("commerce international","exportations"),
("commerce international","balance"),
("commerce international","balance commerciale"),
("commerce international","balance courante"),
("commerce international","balance des changes"),
("commerce international","réserves de changes"),
("politique monétaire","politique monétaire"),
("politique monétaire","inflation"),
("politique monétaire","taux directeur"),
("politique monétaire","banque centrale"),
("élection","circonscription"),
("élection","élections"),
("élection","élection"),
("élection","vote"),
("élection","scrutin"),
("élection","résultat électoral"),
("élection","programme électoral"),
("élection","bulletin de vote"),
("élection","bureau de vote"),
("élection","élections municipales"),
("contestation","contestation"),
("contestation","manifestation"),
("contestation","manifestant"),
("organisation locale","municipalités"),
("organisation locale","maire"),
("organisation locale","région"),
("organisation locale","gouvernorat"),
("organisation locale","gouverneur")]


def fact_check(article,list_facts):
    """
    Cette fonction retourne une liste de couple (thématque, mot déclencheur du fact check) pouvant figurer dans une article
    @INPUT
        list_facts :  la liste des mots à fact checker
        article : le texte de l'article
    """
    list_res = []
    text = unicodedata.normalize('NFD', article).encode('ascii', 'ignore')
    for elt in list_facts:
        mot_check = unicodedata.normalize('NFD', elt[1]).encode('ascii', 'ignore')
        try:
            res = re.search("(?i)"+mot_check.decode("utf-8"), text.decode("utf-8")).group()
            list_res.append(elt)
        except:
            pass
    try:
        res1 = re.search('(\d+)\D*dinar' ,text.decode("utf-8")).group()
        list_res.append(("financement",res1))
    except:
        pass
    try:
        res1 = re.search('(\d+)\D*euro' ,text.decode("utf-8")).group()
        list_res.append(("financement",res1))
    except:
        pass
    try:
        res1 = re.search('(\d+)\D*dollar' ,text.decode("utf-8")).group()
        list_res.append(("financement",res1))
    except:
        pass
    try:
        res1 = re.search('(\d+)\D*voix' ,text.decode("utf-8")).group()
        list_res.append(("élection",res1))
    except:
        pass

    if list_res:
        return list_res
    else:
        return ""
