# -*- coding: utf-8 -*-
"""
Created on Fri May 17 14:54:18 2024

@author: eloua
"""

import random as rd

import code_combat as cbt
from code_combat import *
import pokemons_final as pk
from pokemons_final import *
import interface_pour_jouer as ipj
from interface_pour_jouer import *



class Joueur(pk.Pokemon):
    def __init__(self, nom, list_pok_joueur, pos_init):
        self.nom = nom
        self.list_pok = list_pok_joueur
        self.pos_init = pos_init
        self.new_pos = 0


class Jeu(cbt.Combat, Joueur):
    
    def __init__(self, joueur, pok_def, pok_att):
        super().__init__(joueur, pok_def, pok_att)
        self.is_finito = False
        self.is_combat = False
    
    
    def attributionAleatPokJoueur(self):
        # Tirage au sort de 10 pokemons :
        liste_pok_aleat = []
        for k in range(10):
            deja_attribue = True
            while deja_attribue == True:
                i_aleat = rd.randint(0, 150)
                data_pok = pk.df_n[i_aleat, :]
                pok = pk.Pokemon(data_pok)  # !! Faire ATTENTION à modifier la position initiale par la suite
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
        
    
    def lancementCombat(self):
        if self.joueur.pokemon_trouve(new_pos, pok) == True:  # Si le pokemon est trouvé
            print("\nVous tombez sur un pokemon ! Lancement du combat !")
            self.is_combat = True  # Il doit y avoir un combat
        else:
            self.is_combat = False
        
    
    def jouer(self):
        
        # Initiation du jeu : on demande à l'utilisateur de choisir ses pokemons
        self.attributionAleatPokJoueur()
        self.pok_att = self.joueur.list_pok[0]
        
        # Test si combat puis insctructions combat
        # self.lancementCombat()
        self.pok_att = self.joueur.list_pok[0]
        cb_en_cours = cbt.Combat(self.joueur, self.pok_def, self.pok_att)
        ipj.main()
            
         
            
if __name__ == "__main__":
    pikachu = pk.Pokemon(pk.df_n[24,:])
    rattata = pk.Pokemon(pk.df_n[18,:])
    bulbasaur = pk.Pokemon(pk.df_n[0,:])
    liste_pok_j1 = [pikachu, rattata, bulbasaur]
    J1 = Joueur('j1', liste_pok_j1, 45)

    # TESTS ENCHAINEMENT COMBATS
    
    print("\n\t*** TEST JEU ***\n")
    # combat3 = Combat(J1, rattata, pikachu)
    # jeu1 = Jeu(J1, rattata, pikachu)
    # jeu1.boucleCombat()
    
    
    # TESTS INITATION POKEMONS JOUEUR
    
    jeu2 = Jeu(J1, rattata, pikachu)
    # liste_pok_j2 = jeu2.attributionAleatPokJoueur()
    # liste_pok = jeu2.joueur.list_pok
    # for p in liste_pok:
    #     print(p.name)
    
    jeu2.jouer()
    
    
    
    