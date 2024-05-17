import pandas as pd
from abc import abstractmethod, ABCMeta
import numpy as np
import random as rd 


###PROBLEME INDENTER

pok_data=pd.read_csv(("../data/pokemon_first_gen.csv"), delimiter=",")
pos_pok_init = pd.read_csv("../data/pokemon_coordinates.csv")#Lecture des coordonnées des pokemons
#Dictionnaire type pokemon et index

dico_ang_fr={"Steel":"Acier", "Fighting":"Combat", "Dragon":"Dragon", "Water": "Eau", "Electric":"Electrik", "Fire": "Feu", "Fairy":"Fee", "Ice":"Glace", "Bug":"Insecte", "Normal":"Normal", "Grass":"Plante", "Poison":"Poison", "Psychic":"Psy", "Rock":"Roche", "Ground":"Sol", "Ghost":"Spectre", "Dark":"Tenebres", "Flying":"Vol"}
dicoTypes = {'Acier':0,'Combat':1,'Dragon':2,'Eau':3,'Electrik':4,'Feu':5,'Fee':6,'Glace':7,'Insecte':8,'Normal':9 ,'Plante':10 ,'Poison':11 ,'Psy':12 ,'Roche':13,'Sol':14 ,'Spectre':15 ,'Tenebres':16 ,'Vol':17}

#transposer la dataframe
dfT=pok_data.T
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

#transformation en tableau numpy
df_n = np.array(df)


##Class définissant tous les pokémons
class Pokemon(metaclass=ABCMeta):
    
    def __init__(self, pok_data):
          self.name = pok_data[1]
          self.type_1 = pok_data[2]
          self.attack = pok_data[6]
          self.defense = pok_data[7]
          self.sp_attack = pok_data[8]
          self.sp_defense = pok_data[9]
          self.hp_depart = pok_data[5]
          self.hp_restant = self.hp_depart
      
        
    def nom_pok_to_id_pok(nom_pok):
        """
        Donne l'identifiant du pokémon depuis son nom

        Parameters
        ----------
        nom_pok : TYPE: string
            DESCRIPTION.

        Returns
        -------
        TYPE: integer
            DESCRIPTION.

        """
        liste_noms = df_n[:,1]
       
        return liste_noms.tolist().index(nom_pok)
                 
        
        
    def tri_max():
        """
        Trie qui donne les 5 pokemons aux hp les plus élevés

        Returns
        -------
        tri_max : TYPE
            DESCRIPTION.

        """
    
        tri_max=df.sort_values(by='hp_depart', ascending=False).head(5)
        return tri_max
    
    



    #tri qui sélectionne tous les pokemon avec le type choisis par l'utilisateur
    
    def type_choisis():
        """
        Tri qui sélectionne tous les pokemon avec le type choisis par l'utilisateur

        Returns
        -------
        None.

        """
        type_choisis= input("Entrez le type d'un pokemon (entre guillemets):")
        affichage_type_choisis=df.loc[df.type_1== type_choisis, :]
        print(affichage_type_choisis)


##sélectionner le tri à appliquer
        

    def appliquer_tri():
        """
        Demande au joueur quel tri à appliquer

        Returns
        -------
        TYPE
            DESCRIPTION.

        """
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
         


    
   
#classe définissant l'état des pokémons pour réinitialiser les HP des pokémons       
class Etat(Pokemon, metaclass=ABCMeta):
    
    def __init__(self, pok_data, pos_init, hp_restant, nb_combats):
        super().__init__(pok_data)
        
        self.hp_restant=hp_restant
        self.nb_combats=nb_combats
        
        
        
#Transformation du tableau panda en liste       
pok_init = pok_data.values.tolist()

#Choix aléatoire de 10 pokémons pour le joueur 
pokemon_joueur = rd.sample(pok_init,k=10)


#liste des pokémons présents sur la carte    
pokemon_sauvage = [i for i in pok_data.values.tolist() if i not in pokemon_joueur]

#Transformation du tableau en liste
pos_pok = pos_pok_init.values.tolist()

#Tranformation des coordonnées (chaine de caractère) en liste
for i in range(len(pos_pok)):
    b = pos_pok[i][1]
    l = eval(b)
    pos_pok[i] = [pos_pok[i][0], l]

#Liste des pokémons uniques contenant toutes les informations (dont les coordonnées)
    for j in range(len(pokemon_sauvage)):
        if pos_pok[i][0] == pokemon_sauvage[j][1]:
            if len(pokemon_sauvage[j]) == 13:
                pokemon_sauvage[j].append(pos_pok[i][1])
                x = int(pokemon_sauvage[j][13][0])*10*5 + rd.randint(-10,10)
                y = int(pokemon_sauvage[j][13][1])*10*5 + rd.randint(-10,10)
                pokemon_sauvage[j][13][0] = x
                pokemon_sauvage[j][13][1] = y



class PokemonJoueur(Pokemon):
    def __init__(self, pokemon_joueur):
        super().__init__(pokemon_joueur)
        
               
class PokemonSauvage(Pokemon):
    def __init__(self, pokemon_sauvage):
        super().__init__(pokemon_sauvage)



class Joueur(Pokemon):
    def __init__(self, nom, list_pok_joueur, pos_init):
        self.nom = nom
        self.list_pok = list_pok_joueur
        self.pos_init = pos_init
        



if __name__ == "__main__":
    #Test class Pokemon et ses sous-classes
    poo = pok_init[5]
    poo1 = Pokemon(poo)
    print(poo1.name)
    
    pii = pokemon_joueur[3]
    pii1 = PokemonJoueur(pii)
    print(pii1.name)
    
    puu = pokemon_sauvage[2]
    puu1 =PokemonSauvage(puu)
    print(puu1.name)