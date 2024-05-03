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
    
    def __init__(self, joueur, pok_sauvage, pok_attaquant):
        self.joueur = joueur
        self.pok_sauvage = pok_sauvage
        self.pok_attaquant = pok_attaquant
        self.nb_pok_utilises = 0
        self.continuer_combat = True
        self.choix = ""

    
    def choixAction(self):
        self.choix = ""
        
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
                    
                
        while not (self.choix == 'a' or self.choix == 'c' or self.choix == 'f'):        
            print("\n*** Veuillez saisir un choix parmi : a, c ou f ***\n")
            self.choix = input("Entrez votre choix d'action (parmi a, c ou f): ")
    
    
    def fuite(self):
        if self.choix == 'f':
            self.continuer_combat = False # Dans le cas où le joueur choisit la fuite, le combat s'arrête
        else:
            self.continuer_combat = True
    
    
    def incrementationNbPokUtilises(self):
        if self.choix == 'c':
            self.nb_pok_utilises += 1
        else :
            self.nb_pok_utilises += 0
            
     
        

class ChangementPok(Combat):
     
    def __init__(self, joueur, pok_sauvage, pok_attaquant):
        super().__init__(joueur, pok_sauvage, pok_attaquant)
    
    def incrementationNbPokUtilises(self):
        if self.X
        
            
            



# class PointAttaque():
#     X



if __name__ == "__main__":
    
    
    # TEST CLASSE COMBAT
    
    # j1 = Joueur()
    combat1 = Combat('joueur1', 'nomPokSauvage', 'nomPokAttaquant')
    print(combat1.choixAction())
    print(combat1.choix)
    combat1.fuite()
    print(combat1.continuer_combat)
    
    # p1 = Pokemon('bulbizar', 'type_bulbizar')
    # P1.attak
























