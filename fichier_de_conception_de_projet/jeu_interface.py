# -*- coding: utf-8 -*-
"""
Created on Mon May 13 09:26:44 2024

@author: eloua
"""

import random as rd

import combat as cbt
from combat import *
import pokemon as pk
from pokemon import *
import deplacement_joueur as dj
from deplacement_joueur import *
import interface_pour_jouer as ipj
from interface_pour_jouer import *
import test_interface_graphique as tig
from test_interface_graphique import *
from PyQt5 import QtCore, QtGui, QtWidgets
import sys


class Jeu(cbt.Combat, dj.Joueur, ipj.Player):
    
    def __init__(self, joueur, pok_def, pok_att):
        super().__init__(joueur, pok_def, pok_att)
        self.is_finito = False
        self.is_combat = False
        
        self.ui_main_window = None
        self.main_window = None
        self.Form = None
        self.ui = None
        
    
    def attributionAleatPokJoueur(self):
        # Tirage au sort de 10 pokemons :
        liste_pok_aleat = []
        for k in range(10):
            deja_attribue = True
            while deja_attribue == True:
                i_aleat = rd.randint(0, 150)
                data_pok = pk.df_n[i_aleat, :]
                pok = pk.Pokemon(data_pok, (5,5))  # !! Faire ATTENTION à modifier la position initiale par la suite
                if pok in liste_pok_aleat:
                    deja_attribue = True
                else:
                    deja_attribue = False
            liste_pok_aleat.append(pok)
        self.joueur.list_pok = liste_pok_aleat
        
        # Le joueur sélectionne 7 pokemons parmi ces 10 possibles
        print("\nVoici la liste des pokemons disponibles :")
        for i in range(len(liste_pok_aleat)):
            print(i, ":", liste_pok_aleat[i].name)
        print("\nVeuillez sélectionner les numeros des 5 pokemons voulus :")
        liste_pok_gardes = []
        for i in range(5):
            indice = int(input("Pokemon " + str(i+1) + ': '))
            liste_pok_gardes.append(liste_pok_aleat[indice])
        
        self.joueur.list_pok = liste_pok_gardes
    
    
    def creationInstanceInterface(self):
        app = QtWidgets.QApplication(sys.argv)

        # Créez une instance de votre fenêtre principale
        self.main_window = QtWidgets.QMainWindow()
        self.ui_main_window = ipj.Ui_MainWindow()
        self.ui_main_window.setupUi(self.main_window)
        self.main_window.ui = self.ui_main_window  # Ajoutez l'attribut ui à main_window


        # Créez une instance de votre fenêtre de formulaire
        self.Form = QtWidgets.QWidget()
        self.ui = ipj.Ui_Form(self.main_window)
        self.ui.setupUi(self.Form)

        # name_player = ui.on_play_clicked()
        
    
    def boucleCombat(self):
        self.is_finito = False
        cb = cbt.Combat(self.joueur, self.pok_def, self.pok_att)  # Initialisation d'une instance de la classe combat
        
        while not self.is_finito:
            print("\n\n||| NOUVELLE ATTAQUE |||\n")
            
            print("Condition boucle :", self.is_finito)
            cb.afficheInfosCombat()
            
            cb.demandeChoixAction()
            if cb.continuer_combat == False:
                self.is_finito = True
                print("\nTu as fui, c'est pas ouf mais pas grave persévère mgl")
            elif cb.pok_def.hp_restant <= 0:
                self.is_finito = True
                print("\nTrop fort ! Le combat est gagné !")
                
            # Contre-attaque du pokemon sauvage
            if self.is_finito != True:
                if cb.is_changement == False:  # On n'enlève pas de PV si un changement est effectué
                    cb.attPokSauvage()
                cb.is_changement = False
                cb.testMortPokemonJoueur()
            
    
    def lancementCombat(self):
        if True:  # Si le pokemon est trouvé
            print("\nVous tombez sur un pokemon ! Lancement du combat !")
            self.is_combat = True  # Il doit y avoir un combat
        else:
            self.is_combat = False
        
    
    def jouer(self):
        
        # Initiation du jeu : on demande à l'utilisateur de choisir ses pokemons
        # self.attributionAleatPokJoueur()
        # self.pok_att = self.joueur.list_pok[0]
        
        # Affichez la fenêtre de formulaire
        ipj.Form.show()
        sys.exit(app.exec_())
        self.is_combat = ipj.is_combat_global
        if self.is_combat == True:
            print(self.is_combat)
            ipj.main_window.close()
            tig.run_app_1()
        
        # Test si combat puis insctructions combat
        # self.lancementCombat()
        # self.is_combat = True  # !! Ligne A SUPPRIMER plus tard
        # if self.is_combat == True:
        #     self.boucleCombat()
            
            
            
if __name__ == "__main__":
    pikachu = pk.Pokemon(pk.df_n[24,:], (5,5))
    rattata = pk.Pokemon(pk.df_n[18,:], (5,5))
    bulbasaur = pk.Pokemon(pk.df_n[0,:], (5,5))
    liste_pok_j1 = [pikachu, rattata, bulbasaur]
    J1 = dj.Joueur('j1', liste_pok_j1, 45)

    # TESTS ENCHAINEMENT COMBATS
    
    print("\n\t*** TEST JEU ***\n")
    combat3 = Combat(J1, rattata, pikachu)
    jeu1 = Jeu(J1, rattata, pikachu)
    # jeu1.boucleCombat()
    
    
    # TESTS INITATION POKEMONS JOUEUR
    
    jeu2 = Jeu(J1, rattata, pikachu)
    # liste_pok_j2 = jeu2.attributionAleatPokJoueur()
    # liste_pok = jeu2.joueur.list_pok
    # for p in liste_pok:
    #     print(p.name)
    
    jeu2.jouer()
    
    
    
    
    
    
    
    