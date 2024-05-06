# -*- coding: utf-8 -*-
"""
Created on Fri May  3 13:44:09 2024

@author: Formation
"""


import numpy as np
import pandas as pd
# import fichierClassesLuna
# import fichierDeplacementLauraLee


class Combat():
    
    def __init__(self, joueur, pok_def, pok_att):
        self.vainqueur = False
        self.is_fini = False
        self.nb_pok_utilises = 0
        self.nb_pok_restants = 0
        
        self.joueur = joueur
        self.pok_def = pok_def
        self.pok_att = pok_att
        
        self.continuer_combat = True  # Tant que True, on continue le combat --> On sort de la boucle combat du jeu lorsque False
        self.choix = 0
        choixPossibles = {0:"fuite", 1:"attaque", 2:"changement"}

    
    def demandeChoixAction(self):
        choixTemp = ""
        
        # while not (choix == 'a' or choix == 'c' or choix == 'f'):
        #     choix = input("Entrez votre choix d'action (parmi a, c ou f): ")
            
        #     if choix == 'a': # Si le choix est ATTAQUE
        #         # Ecrire le code correspondant à ce cas
        #         print("Le joueur attaque")
        #         return 'a'
                
        #     elif choix == 'c': # Si le choix est CHANGEMENT DE JOUEUR
        #         # Ecrire le code correspondant à ce cas
        #         print("Le joueur change de pokemon")
        #         return 'c'
                
        #     elif choix == 'f': # # Si le choix est FUITE
        #         # Ecrire le code correspondant à ce cas
        #         print("Le joueur fuit")
        #         return 'f'
                
        #     else:
        #         print("\n*** Veuillez saisir un choix parmi : a, c ou f ***\n")
        
        while not (choixTemp == 'a' or choixTemp == 'c' or choixTemp == 'f'):        
            print("\n*** Veuillez saisir un choix parmi : a, c ou f ***\n")
            choixTemp = input("Entrez votre choix d'action (parmi a, c ou f): ")
        
        if choixTemp == 'f':
            self.choix = 0
            self.fuite()
        elif choixTemp == 'a':
            self.choix = 1
        elif choixTemp == 'c':
            self.choix = 2
            self.changement()
            
    
    def fuite(self):
        """
        Détermine si le joueur a le droit de fuir, puis, si c'est le cas, attribue False à la variable continuer_combat si le choix du joueur est de fuir

        Returns
        -------
        None.

        """
        
        if self.pok_att.hp_restant <= 0.2*self.pok_att.hp_depart:  # Si le nombre d'hp restants pour le pokemon attaquant en cours est <= à 20% des hp de départ
            if self.choix == 0:
                self.continuer_combat = False  # Dans le cas où le joueur choisit la fuite, le combat s'arrête
            else:
                self.continuer_combat = True
        else:
            print("\n*** Fuite impossible : vous avez trop de PV restants ***\n")
            self.continuer_combat = True
        
        
    # def afficheHPRestants(pok):
    #     txt = "Il reste " + str(pok.hp_restants) + " HP restants à votre " + str(pok.name) + "."
        
    #     if pok.hp_restants <= 0.2*pok.hp_depart:
    #         txt += " Ce pokemon a une santé critique !"
    #     else:
    #         txt += " Vous êtes encore en course !"
        
    #     return txt
    
    
    def changement(self):
        """
        Propose à l'utilisateur de choisir un Pokemon dans la liste des Pokemons en sa possession puis définit le pokemon sélectionné comme le Pokemon attaquant

        Returns
        -------
        None.

        """
        
        # Affichage de la liste des pokemons disponibles
        print("Il vous reste les pokemons suivants :")
        for p in self.joueur.liste_pokemon_joueur:
            print("Nom : " + p.name + ", HP restants : " + str(p.hp_restants))
        
        # Demande à l'utilisateur de sélectionner le pokemon à rentrer
        nv_pok = input("Entrez le nom du pokemon souhaité :")
        
        if nv_pok == None:
            print("Aucun changement effectué")
        
        else:
            # Indication du niveau de vie restant du pokemon
            if nv_pok.hp_restants <= 0.2*nv_pok.hp_depart:
                print("Niveau de PV critique ! Changement de Pokemon stratégique.")
            else:
                print("Il reste ", nv_pok.hp_restants, " hp restants à votre ", nv_pok.name)
            
            self.pok_att = nv_pok  # Le pokemon attaquant est maintenant le pokemon sélectionné
            self.continuer_combat = True
            self.nb_pok_utilises += 1
        
        
            
     


class PointsAttaque(Combat):
    
    def __init__(self, joueur, pok_def, pok_att):
        super().__init__(joueur, pok_def, pok_att)
        
        self.is_spe = False
    
    
    def calcDegatsSimples(self):
        """
        Calcul des dégâts causés lors d'une attaque simple

        Returns
        -------
        TYPE
            DESCRIPTION.

        """
        
        pointsAtt = self.pok_att.attack
        pointsDef = self.pok_def.defense
        
        if pointsAtt-pointsDef <= 0:
            return 0
        else:
            return pointsAtt - pointsDef
    
    
    def rechCoef(self):
        """
        Recherche du coefficient multiplicateur des attaques spéciales dans une grille créée

        Returns
        -------
        TYPE
            DESCRIPTION.

        """
        
        # Initialisation de la grille des coef
        grilleCoefs = [
            [0.5,1,1,0.5,0.5,0.5,2,2,1,1,1,1,1,2,1,1,1,1],
            [2,1,1,1,1,1,0.5,2,0.5,2,1,0.5,0.5,2,1,0,2,0.5],
            [0.5,1,2,1,1,1,0,1,1,1,1,1,1,1,1,1,1,1],
            [1,1,0.5,0.5,2,1,1,1,1,1,0.5,1,1,2,2,1,1,1],
            [1,1,0.5,2,1,0.5,1,1,1,1,0.5,1,1,1,0,1,1,2],
            [2,1,0.5,0.5,0.5,1,1,2,2,1,2,1,1,0.5,1,1,1,1],
            [0.5,2,2,1,0.5,1,1,1,1,1,1,0.5,1,1,1,1,2,1],
            [0.5,1,2,0.5,0.5,1,1,0.5,1,1,2,1,1,1,2,1,1,2],
            [0.5,0.5,1,1,0.5,1,0.5,1,1,1,2,0.5,2,1,1,0.5,2,0.5],
            [0.5,1,1,1,1,1,1,1,1,1,1,1,1,0.5,1,0,1,1],
            [0.5,1,0.5,2,0.5,1,1,1,0.5,1,0.5,0.5,1,2,2,1,1,0.5],
            [0,1,1,1,1,1,2,1,1,1,2,0.5,1,0.5,0.5,0.5,1,1],
            [0.5,2,1,1,1,1,1,1,1,1,1,2,0.5,1,1,1,0,1],
            [0.5,0.5,1,1,2,1,1,2,2,1,1,1,1,1,0.5,1,1,2],
            [2,1,1,1,2,2,1,1,0.5,1,0.5,2,1,2,1,1,1,0],
            [1,1,1,1,1,1,1,1,1,0,1,1,2,1,1,2,0.5,1],
            [1,0.5,1,1,1,1,0.5,1,1,1,1,1,2,1,1,2,0.5,1],
            [0.5,2,1,1,1,0.5,1,1,2,1,2,1,1,0.5,1,1,1,1],
            ]
        grilleCoefs = np.array(grilleCoefs)
        
        dicoTypes = {'Acier':0, 'Combat':1, 'Dragon':2, 'Eau':3, 'Electrik':4, 'Feu':5, 'Fee':6, 'Glace':7, 'Insecte':8, 'Normal':9 , 'Plante':10 , 11:'Poison' , 'Psy':12 , 'Roche':13 , 'Sol':14 , 'Spectre':15 , 'Tenebres':16 , 'Vol':17}
        
        indiceLig = dicoTypes[self.pok_att.type_1]
        indiceCol = dicoTypes[self.pok_def.type_1]
        
        return grilleCoefs[indiceLig][indiceCol]
    
    
    def calcDegatsSpe(self):
        """
        Calcule les dégâts causés par une attaque de type spéciale

        Returns
        -------
        TYPE
            DESCRIPTION.

        """
        
        coef = self.rechCoef()
        degatsSpe = self.pok_att.sp_attack - self.pok_def.defense
        
        if degatsSpe*coef <= 0:
            return 0
        else:
            return degatsSpe * coef
    
    
    def retraitPtsAttaque(self):
        if int(input("Entrez 1 si vous souhaitez faire une attaque spéciale : ")) == 1:
            self.pok_def.pv_restants -= self.calcDegatsSpe()
        else:
            self.pok_def.pv_restants -= self.calcDegatsSimples()
        
        
    

class Pokemon():
    def __init__(self, name, type_1, attack, defense, sp_attack, sp_defense, hp_depart):
        self.name=name
        self.type_1=type_1
        self.attack=attack
        self.defense=defense
        self.sp_attack=sp_attack
        self.sp_defense=sp_defense
        self.hp_depart=hp_depart

            



if __name__ == "__main__":
    
    
    # TESTS CLASSE COMBAT
    
    combat1 = Combat('joueur1', 'nomPokSauvage', 'nomPokAttaquant')
    combat1.demandeChoixAction()
    print("Test fonction demandeChoixAction, doit s'afficher le choix entré par l'utilisateur (0, 1 ou 2) : ", combat1.choix)
    
    combat1.fuite()
    print(combat1.continuer_combat)
    
    P1 = Pokemon('P1', 'Feu', 45, 30, 65, 60, 800)
    P2 = Pokemon('P2', 'Acier', 35, 50, 70, 85, 700)
    
    pts1 = PointsAttaque('j1', P2, P1)
    print("Choix : ")
    print(pts1.choix)
    coef = pts1.rechCoef()
    degatsSimples = pts1.calcDegatsSimples()
    degatsSpe = pts1.calcDegatsSpe()























