# -*- coding: utf-8 -*-
"""
Created on Fri May  3 14:30:59 2024

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
df=data.T
print(df)

#Renommer colonnes

##Name
df=df.rename({"Name":"name"})

##Total
df=df.rename({"Total":"total"})

##Attack
df=df.rename({"Attack":"attack"})

##Defense
df=df.rename({"Defense":"defense"})
##Type1
df=df.rename({"Type 1":"type_1"})

##HP
df=df.rename({"HP":"hp_depart"})

##SPATTACK
df=df.rename({"Sp. Atk":"sp_attack"})

##SPDEFENSE
df=df.rename({"Sp. Def":"sp_defense"})
print(df)


#Convertir en numpy
nmp=data.to_numpy()
print(nmp)




##selectionner colonne
df1=nmp[62]
print(df1)

##





                      

#classe Pokemon 

# class Pokemon(metaclass=ABCMeta):
#      def __init__(self, name, type_1, attack, defense, sp_attack, sp_defense, hp_depart):
#          self.name=name
#          self.type_1=type_1
#          self.attack=attack
#          self.defense=defense
#          self.sp_attack=sp_attack
#          self.sp_defense=sp_defense
#          self.hp_depart=hp_depart
#          #self.speed=speed
#          #self.generation=generation
         
#     def affichage(self, name, type_1, attack, defense, sp_attack, sp_defense, hp_depart):
#         name=input("Entrez le nom d'un pokemon (entre guillemets):")
#         for in range(12):
#             for j in range(150):
#                 name=nmp[0][j]
#                 print (nmp[j])

# #classe Etat
         
# class etat(Pokemon, metaclass=ABCMeta):
    
#     @abstractmethod
#     def __init__(self, hp_restant, nb_combats):
#         super().__init__(self, name, type_1, attack, defense, sp_attack, sp_defense, hp_depart)
#         self.hp_restant=hp_restant
#         self.nb_combats=nb_combats
        
        
    
        
        
        
        
    


#avec name

##si 13 i et 150 colonnes
# def infos():
#     Name=input("Entrez le nom d'un pokemon:")
#     for j in range(150):
#         Name=nmp[0][j]
#         #df1=nmp[0][j]
#         print(nmp[j])


##si 150 lignes et 13 colonnes

def infos():
    name=input("Entrez le nom d'un pokemon:")
    for i in range(150):
        name=nmp[i][0]
        print(nmp[j])
        
        
##demander à l'utilisateur quel tri il veut

def selection_tri(tri_choisi):
    tri_choisi=input("Entrez le tri choisis (entre guillemets):")
    #fonction if tel tri alors appliquer telle fonction 

def tri_hp(hp_restant):
    #tri par selection selectionner le hp max
    #a faire
    #V=colonne des HP
    N=size(V)
    min=1
    
    i=1
    
    j=i+1
    
    for i in range(0, N-1, -1):
        min=V[i]
        index=i
        #Recherche de l'élément minimal
        for m in range(i+1, N, 1):
            if (V[m]<min):
                min=V[m]
                index=m
                #on échange la valeur à l'indice courant avec l'élément minimal
                G=V[index]
                V[index]=V[i]
                V[i]=G
                

#trier selon catégorie de pokemon
#premiere etape : trier par liste pour les 18 types
#deuxieme etape : selectionner la liste qui correspond au tri choisi par l'utilisateur
                
def tri_type(type_1):
    L_0=[]
    L_1=[]
    L_2=[]
    L_3=[]
    L_4=[]
    L_5=[]
    L_6=[]
    L_7=[]
    L_8=[]
    L_9=[]
    L_10=[]
    L_11=[]
    L_12=[]
    L_13=[]
    L_14=[]
    L_15=[]
    L_16=[]
    L_17=[]
    
    #faire une boucle pour trier chaque pokemon et le placer dans une liste/catégorie
    #soit on designe le type par : sa case/sa valeur dans le tableau, soit par le nom du type, soit apr le numéro qui correspond au nom du type
    
    for i in range():
        for j in range():
            if typedunom==0:
                L_0.append()
            elif ==1:
                L_1.append()
            elif ==2:
                L_2.append()
            elif =3:
                L_3.append()
            elif ==4:
                L_4.append()
            elif ==5:
                L_5.append()
            elif ==6:
                L_6.append()
            elif ==7:
                L_7.append()
            elif ==8:
                L_8.append()
            elif ==9:
                L_9.append()
            elif ==10:
                L_10.append()
            elif ==11:
                L_11.append()
            elif ==12:
                L_12.append()
            elif ==13:
                L_13.append()
            elif ==14:
                L_14.append()
            elif ==15:
                L_15.append()
            elif ==16:
                L_16.append()
            elif ==17:
                L_17.append()
    print(L_0,L_1,L_2,L_3,L_4,L_5,L_6,L_7,L_8,L_9,L_10,L_11,L_12,L_13,L_14,L_15,L_16,L_17)
    
    # demander à l'utilisateur quelle categorie 
    
    type_choisi=input("Entrez le type de pokemon que vous souhaitez choisir (entre guillemets):")
    #n=numero qui correspond au type de pokemon dans le dico
    #le plus pratique serait 
    #for n in range(18)
    return L_n #ou print
        


####Autre methode 
    ##au lieu de répartir les différents okemon selon des categories et ensuite de choisir la catégorie que l'utilsateur souhaite
    ##on peut faire une selection avec le site et afficher dans une liste vide au départ la catégorie souhaitée
        
    
    
                
    
    

            
            
    
    

#Convertir en numpy
#nmp=data.to_numpy()
#print(nmp)

#df=data["Name", "Type 1", "Type 2", "attack", "defense", "sp_attack", "sp_defense", "speed", "generation"]
#M=np.array(df)
#VX=np.array(df.X)
#print(data.head())
                 



#class Pokemon(metaclass=ABCMeta):
     #def __init__(self, name, type_pok, attack, defense, sp_attack, sp_defense, speed, generation ):
         #self.name=name
        # self.type=type_pok
         #self.attack=attack
        # self.defense=defense
         #self.sp_attack=sp_attack
         #self.sp_defense=sp_defense
        # self.speed=speed
         #self.generation=generation
    


