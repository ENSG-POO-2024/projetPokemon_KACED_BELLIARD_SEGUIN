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
# print(dfT)

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
# print(df)


df_n = np.array(df)




#classe Pokemon 

class Pokemon(metaclass=ABCMeta):
    
    def __init__(self, pok_data, pos_init):
          self.name = pok_data[1]
          self.type_1 = pok_data[2]
          self.attack = pok_data[6]
          self.defense = pok_data[7]
          self.sp_attack = pok_data[8]
          self.sp_defense = pok_data[9]
          self.hp_depart = pok_data[5]
          self.hp_restant = self.hp_depart
          #self.speed = pok_data[10]
          #self.generation pok_data[11]
          
          self.pos = pos_init
          
        # #fonction affichage par ligne

    # def affichage_ligne(self):
    #     df_affiche=df.loc[1, :]
    #     print(df_affiche)
        
        
        #fonction affichage par colonne
            
    # def affichage_colonne(self):
    #     df_affiche=df.iloc[:, [0,-1]].head()
    #     print(df_affiche)
            
            
        #fonction affichage avec nom du pokemon et obenir les informations associées
            #utilise affichage par ligne
        
    # def affichage_nom(self):
    #     name=input("Entrez le nom d'un pokemon (entre guillemets):")
    #     #creation d'un index correspondant au nom des pokemon
    #     df_index_name=df.set_index("name")
    #     infos=df_index_name.loc["Bulbasaur", :]
    #     print(infos)
    

##TRI
    
#tri par hp ordre croissant
##attention le tri s'effectue en fonction des pokemon que le joueur possède et non sur toutes la base de données

     
        
        
    def tri_max():
        X = 0 
  
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
         
class Etat(Pokemon, metaclass=ABCMeta):
    
    def __init__(self, pok_data, pos_init, hp_restant, nb_combats):
        super().__init__(pok_data, pos_init)
        
        self.hp_restant=hp_restant
        self.nb_combats=nb_combats




# pok1 = Pokemon('Pikachu', 'Electric', 75, 30, 150, 60, 800, (5,5))

pikachu_data = df_n[24,:]
pikachu = Pokemon(pikachu_data, (5,5))
print(pikachu.sp_attack)

# pok1.affichage_ligne()
# pok1.affichage_colonne()
# pok1.affichage_nom()
























