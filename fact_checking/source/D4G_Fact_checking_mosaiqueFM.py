
# coding: utf-8

# In[13]:


import re
import pandas as pd
import unicodedata


# * Exemple : Fact checking pour les sommes en dinars dans les articles

# In[98]:


#re.search('\d+(.*?)(?i)dinar' ,'invest 300 millions de dinars pour l education').group()
re.search('(\d+)\D*dinar' ,'invest 500 M dollars 300 millions de dinars pour l education').group()


# In[8]:


# le préfixe (?i) permet de rendre la recherche des mots insensibles à la casse
re.search("(?i)emploi" ,"pole emPloi").group()


# In[11]:


#Ici j'ai juste pris les éléments figurant dans le fichier
#https://docs.google.com/spreadsheets/d/12ElwEojNy9w7mYtwlERt_YcHwtcfAja3EhSrYWVu_TI/edit#gid=0
list_fact = [("emploi","chômage"),
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


# In[164]:


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
            res = re.search("(?i)"+mot_check.decode("utf-8")  ,text.decode("utf-8") ).group()
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


# In[180]:


import unicodedata
def strip_accents(s):
    try : s = s.decode('utf-8')
    except : s = str(s)
    return ''.join(c for c in unicodedata.normalize('NFD', s)  if unicodedata.category(c) != 'Mn')
strip_accents("élément")


# In[144]:


def flag_fact_check(x):
    """
    Cette fonction retourne OUI si l'article est à fact checker, NON sinon
    """
    if x:
        return "OUI"
    else:
        return "NON"


# In[99]:


fact_check("invest 300 millions de dinars pour l education 100 M de dollars pour l'emploi chômeur chomage",list_fact )


# In[165]:


#lire la table des articles Mosaique FM
data = pd.read_csv('C:/Users/houeslat/Documents/DataForGood/data/MosaiqueFM_v0.csv',encoding="utf8")


# In[166]:


#la colonne 'Unnamed: 0' est juste un index, elle n'est pas utile pour notre analyse
data.drop('Unnamed: 0',axis=1,inplace=True)


# In[167]:


data = data.drop_duplicates()


# In[168]:


data.head()


# In[169]:


data['fact_checking_list'] = data['Article'].apply(lambda row : fact_check(row,list_fact) )


# In[170]:


data.head()


# In[171]:


data["Vérifier l'article"] = data['fact_checking_list'].apply(lambda row :flag_fact_check(row) )


# In[172]:


data.head()


# In[173]:


list(data['url'])[0]


# In[174]:


data['nb_facts'] = data ["fact_checking_list"].apply(lambda row : len(row))


# In[175]:


data.sort_values(by="nb_facts",ascending=False).head()


# In[176]:


list(data.loc[data["Titre"].str.contains("Réouverture de l’appel à candidatures pour la"),"fact_checking_list" ])


# In[124]:


data.shape


# In[177]:

#compter le nombre d'articles par taille de la liste des éléments à checker
data['nb_facts'].value_counts()


# In[178]:


data.to_csv('data/mosaique_articals_with_facts_to_check.csv',index=False,encoding="utf8")