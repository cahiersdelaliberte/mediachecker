
# coding: utf-8

# In[13]:


import re 
import pandas as pd
import unicodedata


# * Exemple : Fact checking pour les sommes en dinars dans les articles

# In[7]:


re.search('\d+(.*?)(?i)dinar' ,'invest 300 millions de dinars pour l education').group()


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


# In[48]:


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
        res1 = re.search('\d+(.*?)(?i)dinar|\d+(.*?)(?i)euro|\d+(.*?)(?i)dollar' ,text.decode("utf-8")).group()
        list_res.append(("financement",res1))
    except:
        pass          
    if list_res:
        return list_res
    else:
        return ""


# In[49]:


fact_check("invest 300 millions de dinars pour l education 100 M d'euros education emploi chômeur chomage",list_fact )


# In[50]:


#lire la table des articles Mosaique FM
data = pd.read_csv('C:/Users/houeslat/Documents/DataForGood/data/MosaiqueFM_v0.csv',encoding="utf8")


# In[51]:


data.head()


# In[52]:


data['fact_checking_list'] = data['Article'].apply(lambda row : fact_check(row,list_fact) )


# In[53]:


data.head()


# In[54]:


def flag_fact_check(x):
    if x:
        return "OUI"
    else:
        return "NON"


# In[55]:


data["Vérifier l'article"] = data['fact_checking_list'].apply(lambda row :flag_fact_check(row) )


# In[56]:


data.head()


# In[57]:


data.drop('Unnamed: 0',axis=1,inplace=True)


# In[58]:


data.head()


# In[59]:


data.to_csv('C:/Users/houeslat/Documents/DataForGood/data/mosaique_articals_with_facts_to_check.csv',index=False,encoding="utf8")

