import re
import unicodedata


def fact_check(article,list_facts):
    """
    Cette fonction retourne une liste de couple (thématque, mot déclencheur du fact check) pouvant figurer dans une article
    @INPUT
        list_facts :  la liste des mots à fact checker
        article : le texte de l'article
    """
    list_res = []
    text = unicodedata.normalize('NFD', article).encode('ascii', 'ignore')
    #print(text)
    for elt in list_facts:
        mot_check = unicodedata.normalize('NFD', elt[1]).encode('ascii', 'ignore')
        #print(mot_check)
        try:
            #print(str(mot_check) in str(text), mot_check, text)
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