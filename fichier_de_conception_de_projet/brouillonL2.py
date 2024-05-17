# -*- coding: utf-8 -*-
"""
Created on Tue May  7 10:28:42 2024

@author: Formation
"""

import pandas as pd
from abc import abstractmethod, ABCMeta
import numpy as np





data=pd.read_csv(("./data/pokemon_first_gen.csv"), delimiter=",")

#Dictionnaire type pokemon et index
dico_ang_fr={"Steel":"Acier", "Fighting":"Combat", "Dragon":"Dragon", "Water": "Eau", "Electric":"Electrik", "Fire": "Feu", "Fairy":"Fee", "Ice":"Glace", "Bug":"Insecte", "Normal":"Normal", "Grass":"Plante", "Poison":"Poison", "Psychic":"Psy", "Rock":"Roche", "Ground":"Sol", "Ghost":"Spectre", "Dark":"Tenebres", "Flying":"Vol"}
dicoTypes = {'Acier':0,'Combat':1,'Dragon':2,'Eau':3,'Electrik':4,'Feu':5,'Fee':6,'Glace':7,'Insecte':8,'Normal':9 ,'Plante':10 ,'Poison':11 ,'Psy':12 ,'Roche':13,'Sol':14 ,'Spectre':15 ,'Tenebres':16 ,'Vol':17}



#transposer la dataframe
dfT=data.T
print(dfT)

#Renommer colonnes

##Name
dfT=dfT.rename({"Name":"name"})

##Total
dfT=dfT.rename({"Total":"total"})

##Attack
dfT=dfT.rename({"Attack":"attack"})

##Defense
dfT=dfT.rename({"Defense":"defense"})
##Type1
dfT=dfT.rename({"Type 1":"type_1"})





##HP
dfT=dfT.rename({"HP":"hp_depart"})

##SPATTACK
dfT=dfT.rename({"Sp. Atk":"sp_attack"})

##SPDEFENSE
dfT=dfT.rename({"Sp. Def":"sp_defense"})

##RETRANSPOSER LA DATA
df=dfT.T
print(df)

#avoie les 5 pokemon aux HP les plus élevés

def appliquer_tri():
    tri_choisis=input("Entrez le type de tri que vous souhaitez appliquer (entre guillemets):")
    if tri_choisis=="HP":
        tri_max=df.sort_values(by='hp_depart', ascending=False).head(5)
        return tri_max
    elif tri_choisis=="Type":
        tri_type= input("Entrez le type d'un pokemon (entre guillemets):")
        type_trie=df.loc[df.type_1== tri_type, :]
        return type_trie
    else:
        return False