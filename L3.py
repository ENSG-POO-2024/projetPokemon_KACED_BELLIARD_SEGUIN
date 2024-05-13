# -*- coding: utf-8 -*-
"""
Created on Tue May  7 09:21:59 2024

@author: Formation
"""


import pandas as pd
from abc import abstractmethod, ABCMeta
import numpy as np

###PROBLEME INDENTER

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




    

#classe Pokemon 

class Pokemon(metaclass=ABCMeta):
    def __init__(self, name, type_1, attack, defense, sp_attack, sp_defense, hp_depart):
          self.name=name
    
          self.type_1=type_1
          self.attack=attack
          self.defense=defense
          self.sp_attack=sp_attack
          self.sp_defense=sp_defense
          self.hp_depart=hp_depart
          self.hp_restant=hp_depart
          #self.speed=speed
          #self.generation=generation
          
        # #fonction affichage par ligne

    def affichage_ligne():
        df_affiche=data.loc[0, :]
        print(df_affiche)
        
        
        #fonction affichage par colonne
            
    def affichage_colonne():
        df_affiche=df.iloc[:, [0,-1]].head()
        print(df_affiche)
            
            
        #fonction affichage avec nom du pokemon et obenir les informations associées
            #utilise affichage par ligne
        
    def affichage_nom():
        name=input("Entrez le nom d'un pokemon (entre guillemets):")
  #creation d'un index correspondant au nom des pokemon
        df_index_name=df.set_index("name")
        infos=df_index_name.loc["Bulbasaur", :]
        print(infos)
    

##TRI
    
#tri par hp ordre croissant
##attention le tri s'effectue en fonction des pokemon que le joueur possède et non sur toutes la base de données

     
        
        
        def tri_max():
         
  
   #si on selectionne une valeur de HP     
         # tri_max=df.loc[df.hp_depart==45, :]
         # print(tri_max)
  
  
   # #tri au-dessus d'une certaine valeur
         # tri_max=df.loc[(df.hp_depart >=100), :]
         # print(tri_max)
  
   # #tri qui donne les infos du pokemon avec le max de HP
            # tri_max=df.loc[df.hp_depart== max(df.hp_depart), :]
            # print(tri_max)
     #tri qui donne les 5 pokemons aux hp les plus élevés
            #def tri_max():
                # tri_max=df.sort_values(by='hp_depart', ascending=False).head(5)
                # print(tri_max)
    
    
#tri type 




##attention le tri s'effectue en fonction des pokemon que le joueur possède et non sur toutes la base de données
    
    #tri qui sélectionne tous les pokemon avec le type choisis par l'utilisateur
    
    # def type_choisis():
    #     type_choisis= input("Entrez le type d'un pokemon (entre guillemets):")
    #     affichage_type_choisis=df.loc[df.type_1== type_choisis, :]
    #     print(affichage_type_choisis)


##sélectionner le tri à appliquer
        

    def appliquer_tri():
        tri_choisis=input("Entrez le type de tri que vous souhaitez appliquer (entre guillemets):")
        if tri_choisis=="HP":
            tri_hp=df.sort_values(by='hp_depart', ascending=False).head(5)
            return tri_hp
        elif tri_choisis=="Type":
            tri_type= input("Entrez le type d'un pokemon (entre guillemets):")
            type_trie=df.loc[df.type_1== tri_type, :]
            return type_trie
        else:
            return False
         

   ##faire fonction qui permet de choisir le pokemon après les tris effectués     

#classe Etat
         
class etat(Pokemon, metaclass=ABCMeta):
    
    @abstractmethod
    def __init__(self, hp_restant, nb_combats):
        super().__init__(self, name, type_1, attack, defense, sp_attack, sp_defense, hp_depart)
        self.hp_restant=hp_restant
        self.nb_combats=nb_combats