# -*- coding: utf-8 -*-
"""
Created on Fri May  3 13:44:09 2024

@author: Formation
"""


import numpy as np
import pandas as pd
# import fichierClassesLuna
from déplacement_joueur import *
import déplacement_joueur as dj




class Pokemon():
    def __init__(self, name, type_1, attack, defense, sp_attack, sp_defense, hp_depart, hp_restant):
        self.name=name
        self.type_1=type_1
        self.attack=attack
        self.defense=defense
        self.sp_attack=sp_attack
        self.sp_defense=sp_defense
        self.hp_depart=hp_depart
        self.hp_restant = hp_restant




class PointsAttaque():
    
    def __init__(self, joueur, pok_def, pok_att):
        
        self.joueur = joueur
        self.pok_def = pok_def
        self.pok_att = pok_att
        
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
        print("Valeur de l'attaque spéciale :", degatsSpe*coef)
        print("infos calcul :", self.pok_att.sp_attack, self.pok_def.defense, coef)
        
        if degatsSpe*coef <= 0:
            return 0
        else:
            return int(degatsSpe * coef)
    
    
    def retraitPtsAttaque(self):
        choixSpe = int(input("Entrez 1 si vous souhaitez faire une attaque spéciale, 2 sinon : "))
        
        if choixSpe == 1:
            degSpe = self.calcDegatsSpe()
            self.pok_def.hp_restant -= degSpe
            print("!! HP perdus :", degSpe)
            
        else:
            degSpl = self.calcDegatsSimples()
            self.pok_def.hp_restant -= degSpl
            print("!! HP perdus :", degSpl)





class Combat(PointsAttaque):
    
    def __init__(self, joueur, pok_def, pok_att):
        super().__init__(joueur, pok_def, pok_att)
        
        self.vainqueur = False
        self.nb_pok_utilises = 0
        self.nb_pok_restants = 0
        
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
            self.attaque()

        elif choixTemp == 'c':
            self.choix = 2
            self.changement()
            
    
    def attaque(self):
        att = PointsAttaque(self.joueur, self.pok_def, self.pok_att)
        att.retraitPtsAttaque()

    
    
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
            print("\n*** Fuite impossible : vous avez trop de PV restants (", self.pok_att.hp_restant,") ***\n")
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
        for p in self.joueur.list_pok:
            print("Nom : " + p.name + ", HP restants : " + str(p.hp_restant))
        
        # Demande à l'utilisateur de sélectionner le pokemon à rentrer
        nv_pok_str = input("Entrez le nom du pokemon souhaité :")
        nv_pok = Pokemon(nv_pok_str, 'Feu', 50, 50, 50, 50, 50, 50) # !!! Ligne A MODIFIER pour qu'elle s'adapte au pokemon entré par le joueur
        
        # Test si Pokemon entré est dans la liste
        test = False
        for p in self.joueur.list_pok:
            if nv_pok == p:
                test = True
        if test == False:
            print("Vous n'avez pas ce Pokemon !")
        
        if nv_pok == None:
            print("Aucun Pokemon entré..")
        
        else:
            # Indication du niveau de vie restant du pokemon
            if nv_pok.hp_restant <= 0.2*nv_pok.hp_depart:
                print("Niveau de PV critique ! Changement de Pokemon stratégique.")
            else:
                print("Il reste ", nv_pok.hp_restant, " hp restants à votre ", nv_pok.name)
            
            self.pok_att = nv_pok  # Le pokemon attaquant est maintenant le pokemon sélectionné
            self.continuer_combat = True
            self.nb_pok_utilises += 1
        
        
    def afficheInfosCombat(self):
        print("\n*** Infos combat ***")
        print("Nom pokemon attaquant :", self.pok_att.name)
        print("HP restants pok attaquant :", self.pok_att.hp_restant)
        print("Nom pokemon sauvage :", self.pok_def.name)
        print("HP restants pok sauvage :", self.pok_def.hp_restant)
        
        

            

class Jeu(Combat):
    
    def __init__(self, joueur, pok_def, pok_att):
        super().__init__(joueur, pok_def, pok_att)
        self.is_finito = False
    
    
    def boucleCombat(self):
        self.is_finito = False
        cb = Combat(self.joueur, self.pok_def, self.pok_att)  # Initialisation d'une instance de la classe combat
        
        while not self.is_finito:
            print("Condition boucle :", self.is_finito)
            cb.afficheInfosCombat()
            
            cb.demandeChoixAction()
            if cb.continuer_combat == False:
                self.is_finito = True
                print("\nTu as fui, c'est pas ouf mais pas grave persévère mgl")
            elif cb.pok_def.hp_restant <= 0:
                self.is_finito = True
                print("\nTrop fort ! Le combat est gagné !")
            
            




if __name__ == "__main__":
    
    
    # TESTS CLASSE COMBAT
    
    P1 = Pokemon('P1', 'Plante', 75, 30, 150, 60, 800, 25)
    P2 = Pokemon('P2', 'Eau', 50, 50, 100, 85, 700, 700)
    P3 = Pokemon('P3', 'Glace', 78, 60, 89, 75, 687, 687)
    liste_pok_j1 = [P1,P2,P3]
    J1 = dj.Joueur('j1', liste_pok_j1, 45)
    
    combat1 = Combat(J1, P2, P1)
    # combat1.demandeChoixAction()
    # print("\n*** Test fonction demandeChoixAction, doit s'afficher le choix entré par l'utilisateur (0, 1 ou 2) : ", combat1.choix)
    
    # combat1.demandeChoixAction()
    # combat1.fuite()
    # print("\n*** Test fonction fuite, doit afficher la valeur de la variable cotinuer_combat : ", combat1.continuer_combat)
    
    
    # TESTS CLASSE POINTS ATTAQUE
    
    pts1 = PointsAttaque(J1, P2, P1)
    # degatsSimples = pts1.calcDegatsSimples()
    # print("\nSont attendus les degats causés par une attaque simple de", P1.name, "de valeur", P1.attack, "sur", P2.name, "de défense", P2.defense, ':', degatsSimples)
    # coef = pts1.rechCoef()
    # print("\nEst attendu le coef de l'attaque d'un pok de type", P1.type_1, "sur un pok de type", P2.type_1, ":", coef)
    # degatsSpe = pts1.calcDegatsSpe()
    # print("\nSont attendus les degats causés par une attaque spéciale de", P1.name, "de valeur", P1.sp_attack, "sur", P2.name, "de défense spéciale", P2.sp_defense, ':', degatsSpe)
    
    
    # TESTS SYSTEME ATTAQUE CLASSE COMBAT
    
    combat2 = Combat(J1, P3, P2)
    # print("PV de", combat2.pok_def.name, "avant l'attaque simple de", combat2.pok_att.name, "de valeur", combat2.pok_att.attack-combat2.pok_def.defense, ":", combat2.pok_def.hp_restant)
    # combat2.attaque()
    # print("PV de", combat2.pok_def.name, "après l'attaque simple de", combat2.pok_att.name, ":", combat2.pok_def.hp_restant)
    
    # print("\n***\nPV de", combat2.pok_def.name, "avant l'attaque spéciale de", combat2.pok_att.name, ":", combat2.pok_def.hp_restant)
    # combat2.attaque()
    # print("PV de", combat2.pok_def.name, "après l'attaque spéciale de", combat2.pok_att.name, ":", combat2.pok_def.hp_restant)
    
    
    # TESTS ENCHAINEMENT COMBATS
    
    print("\n\t*** TEST JEU ***\n")
    combat3 = Combat(J1, P2, P1)
    jeu1 = Jeu(J1, P2, P1)
    jeu1.boucleCombat()

























