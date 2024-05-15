# -*- coding: utf-8 -*-
"""
Created on Mon May 13 10:08:57 2024

@author: Formation
"""


#code interface graphique 

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication
import sys
import test_code_combat as tcc
from test_code_combat import *
import pokemon as pk 
from pokemon import *
import deplacement_joueur as dj
from deplacement_joueur import *


pikachu = pk.Pokemon(pk.df_n[24,:], (5,5))
rattata = pk.Pokemon(pk.df_n[18,:], (5,5))
bulbasaur = pk.Pokemon(pk.df_n[0,:], (5,5))
liste_pok_j1 = [pikachu, rattata, bulbasaur]
J1 = dj.Joueur('j1', liste_pok_j1, 45)
C1 = tcc.Combat(J1, bulbasaur, pikachu)


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(800, 600)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(20, 10, 391, 281))
        self.label.setText(str(C1.pok_def.hp_restant))
        self.label.setPixmap(QtGui.QPixmap("Galerie.jpg"))
        self.label.setObjectName("label")
        
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(450, 30, 300, 200))
        self.label_2.setPixmap(QtGui.QPixmap("Galerie.jpg"))
        self.label_2.setObjectName("label2")
        self.label_2.setStyleSheet('background-color: rgb(255, 0, 0);\n')
        txt = C1.afficheInfosCombat()
        self.label_2.setText(txt)
        
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(340, 241, 71, 20))
        self.pushButton.setText("Fuite")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("bouton fuite 4.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setIconSize(QtCore.QSize(75, 50))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.fctFuite)
        
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(340, 221, 71, 20))
        self.pushButton_2.setText("Sac")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("bouton sac 3.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_2.setIcon(icon1)
        self.pushButton_2.setIconSize(QtCore.QSize(75, 50))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.fctChangement)
        
        self.pushButton_3 = QtWidgets.QPushButton(Form)
        self.pushButton_3.setGeometry(QtCore.QRect(340, 200, 71, 21))
        self.pushButton_3.setText("Attaque")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("bouton petit attaque .png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_3.setIcon(icon2)
        self.pushButton_3.setIconSize(QtCore.QSize(75, 50))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.clicked.connect(self.fctActivationAttaque)
        
        self.pushButton_4 = QtWidgets.QPushButton(Form)
        self.pushButton_4.setGeometry(QtCore.QRect(100, 100, 231, 41))
        self.pushButton_4.setText("Attaque spe")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("bouton attaque spéciale 4.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_4.setIcon(icon3)
        self.pushButton_4.setIconSize(QtCore.QSize(230, 70))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_4.hide()
        self.pushButton_4.clicked.connect(self.fctAttSpe)
        
        self.pushButton_5 = QtWidgets.QPushButton(Form)
        self.pushButton_5.setGeometry(QtCore.QRect(100, 160, 231, 41))
        self.pushButton_5.setText("Attaque spl")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("bouton attaque neutre 4.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_5.setIcon(icon4)
        self.pushButton_5.setIconSize(QtCore.QSize(230, 70))
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_5.hide()
        self.pushButton_5.clicked.connect(self.fctAttSpl)
        
        self.comboBoxChgmt = QtWidgets.QComboBox(Form)
        self.comboBoxChgmt.setGeometry(QtCore.QRect(200, 400, 231, 41))
        self.comboBoxChgmt.setObjectName("choixPokChgmt")
        # self.comboBoxChgmt.addItem("pok1")
        # self.comboBoxChgmt.addItem("pok2")
        # self.comboBoxChgmt.addItem("pok3")
        for p in C1.joueur.list_pok:
            self.comboBoxChgmt.addItem(p.name)
        # self.comboBoxChgmt.setText("Choix du pokemon")
        self.comboBoxChgmt.hide()
        self.comboBoxChgmt.currentIndexChanged.connect(self.fctChoixPokChgmt)
        self.pok_select_nom = self.comboBoxChgmt.currentText()
        
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        
    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText("HP_restants pok def : " + str(C1.pok_def.hp_restant))

        
    def fctActivationAttaque(self):
        txt = C1.afficheInfosCombat()
        self.label_2.setText(txt)
        self.pushButton_4.show()
        self.pushButton_5.show()
        # self.close()
    
    def fctAttSpe(self):
        C1.choixSpe = 1
        C1.attaque()
        self.label.setText("HP_restants pok def : " + str(C1.pok_def.hp_restant))
        if C1.pok_def.hp_restant <= 0:
            self.close()
        self.pushButton_4.hide()
        self.pushButton_5.hide()
        C1.attPokSauvage()
        txt = C1.afficheInfosCombat()
        self.label_2.setText(txt)
    
    def fctAttSpl(self):
        C1.choixSpe = 2 
        C1.attaque()
        self.label.setText("HP_restants pok def : " + str(C1.pok_def.hp_restant))
        if C1.pok_def.hp_restant <= 0:
            print("Combat gagné !")
            self.close()
        self.pushButton_4.hide()
        self.pushButton_5.hide()
        C1.attPokSauvage()
        txt = C1.afficheInfosCombat()
        self.label_2.setText(txt)
        
    def fctFuite(self):
        C1.fuite()
        if C1.continuer_combat == False:
            print("\nVous fuyez !")
            self.close()
    
    def fctChangement(self):
        self.comboBoxChgmt.show()
    
    def fctChoixPokChgmt(self):
        self.pok_select_nom = self.comboBoxChgmt.currentText()
        pok_att_origine = C1.pok_att
        for p in C1.joueur.list_pok:
            if p.name == self.pok_select_nom:
                if p != pok_att_origine and p != C1.pok_def:
                    C1.pok_att = p
                else:
                    print('Choisir un pok différent !')
        self.comboBoxChgmt.hide()
        txt = C1.afficheInfosCombat()
        self.label_2.setText(txt)
              
      
      
      
class XXXXWindow (QMainWindow, Ui_Form):
    def __init__(self, parent=None):
        super(XXXXWindow, self).__init__(parent)
        self.setupUi(self)
        # ...


def run_app_1():
    app = QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    mainWin = XXXXWindow()
    mainWin.show()
    app.exec_()




if __name__ == "__main__":
    
    run_app_1()
        
        
    # ui = Ui_Form()
    # fenetre = XXXXWindow()
    # def run_app_2():
    #     app = QApplication(sys.argv)
    #     mainWin = XXXXWindow()
    #     mainWin.show()
    #     app.exec_()
    # run_app_2()
 
    
    
    
    
    
    
    