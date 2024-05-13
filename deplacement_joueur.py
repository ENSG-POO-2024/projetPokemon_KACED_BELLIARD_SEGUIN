import numpy as np
import matplotlib.pyplot as plt
import random as rd
import pandas as pd
import pokemon as pk

a=30 
p=2

# # pok = pd.read_csv("../data/pokemon_first_gen.csv") #Lecture de la base de données des pokémons avec le module pandas
# # pok_init = pok.values.tolist()#Transformation du tableau panda en liste
# # list_pok_joueur = rd.sample(pok_init,k=10)#Choix aléatoire de 10 pokémons pour le joueur 
# # pok_jeu = [i for i in pok_init if i not in list_pok_joueur]#liste des pokémons présents sur la carte
# # pos_pok_init = pd.read_csv("../data/pokemon_coordinates.csv")#Lecture des coordonnées des pokemons
# # pos_pok = pos_pok_init.values.tolist()#Transformation du tableau en liste

# #Tranformation des coordonnées (chaine de caractère) en liste
# for i in range(len(pos_pok)):
#     b = pos_pok[i][1]
#     l = eval(b)
#     pos_pok[i] = [pos_pok[i][0], l]

# #Liste des pokémons uniques contenant toutes les informations (dont les coordonnées)
#     for j in range(len(pok_jeu)):
#         if pos_pok[i][0] == pok_jeu[j][1]:
#             if len(pok_jeu[j]) == 13:
#                 pok_jeu[j].append(pos_pok[i][1])
#                 x = int(pok_jeu[j][13][0]) + rd.randint(0,10)
#                 y = int(pok_jeu[j][13][1]) + rd.randint(0,10)
#                 pok_jeu[j][13][0] = x
#                 pok_jeu[j][13][1] = y




class Pokemon():
    def __init__(self, name, type_1, attack, defense, sp_attack, sp_defense, hp_depart, hp_restant, pos):
        self.name=name
        self.type_1=type_1
        self.attack=attack
        self.defense=defense
        self.sp_attack=sp_attack
        self.sp_defense=sp_defense
        self.hp_depart=hp_depart
        self.hp_restant = hp_restant
        self.pos = pos


class Joueur(Pokemon):
    def __init__(self, nom, list_pok_joueur, pos_init):
        self.nom = nom
        self.list_pok = list_pok_joueur
        self.pos_init = pos_init
        self.new_pos = 0
        
    def deplacement(self, pos_init, new_pos):
        if (self.pos_init.x + rd.uniform(0,5)<=a-1) and (self.pos_init.x + rd.uniform(0,5)>=0) and (self.pos_init.y + rd.uniform(0,5)<=a-1) and (self.pos_init.y + rd.uniform(0,5)>=0):
            x = self.pos_init.x + rd.uniform(0,5)
            y = self.pos_init.y + rd.uniform(0,5)
            self.new_pos.x = x
            self.new_pos.y = y
            
    def pokemon_trouve(self, pok):
        pos_pok = pok.pos
        
        d = int (np.sqrt( (self.new_pos.x-pos_pok.x)**2 + (self.new_pos.y - pos_pok.y)**2 ))
        if d<=2:
            return True
        else: return False
        
    
    
    
    
class Plateau(Joueur,Pokemon):
    def __init__(self, list_pok_joueur,pos_init, pok_init):
        self.list_pok_joueur = list_pok_joueur
        self.pos_init = pos_init
        self.pok_init = pok_init
        
    def __str__(self):
        pass
nom = 'Sacha'
# j1 = Joueur(nom,list_pok_joueur,pos_pok)