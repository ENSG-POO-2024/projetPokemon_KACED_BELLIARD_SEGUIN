import numpy as np
import matplotlib.pyplot as plt
import random as rd
import pandas as pd

a=30 
p=2

pok = pd.read_csv("data/pokemon_first_gen.csv") #Lecture de la base de données des pokémons avec le module pandas
pok_init = pok.values.tolist()#Transformation du tableau panda en array
list_pok_joueur = rd.sample(pok_init,k=10)#Choix aléatoire de 10 pokémons pour le joueur 
pok_jeu = [i for i in pok_init if i not in list_pok_joueur]

pos_pok_init = pd.read_csv("data/pokemon_coordinates.csv")
pos_pok = pos_pok_init.values.tolist()




class Pokemon():
    def __init__(self, nom):
        self.nom = nom



class Joueur(Pokemon):
    def __init__(self, nom, list_pok_joueur, pos_init):
        self.nom = nom
        self.list_pok = list_pok_joueur
        self.pos_init = pos_init
        
    def deplacement(self, pos_init, new_pos):
        if (self.pos_init.x + rd.uniform(0,5)<=a-1) and (self.pos_init.x + rd.uniform(0,5)>=0) and (self.pos_init.y + rd.uniform(0,5)<=a-1) and (self.pos_init.y + rd.uniform(0,5)>=0):
            x = self.pos_init.x + rd.uniform(0,5)
            y = self.pos_init.y + rd.uniform(0,5)
            self.new_pos.x = x
            self.new_pos.y = y
            
    def pokemon_trouve(self, new_pos, pos_pok):
        d = int (np.sqrt( (new_pos.x-pos_pok.x)**2 + (new_pos.y - pos_pok.y)**2 ))
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
j1 = Joueur(nom,list_pok_joueur,pos_pok)