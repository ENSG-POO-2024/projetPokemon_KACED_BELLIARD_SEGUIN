
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication
import code_combat as tcc
import pokemons_final as pk
import sys


#création d'une instance de combat qu'on utilise comme test
pikachu = pk.Pokemon(pk.df_n[24,:])
rattata = pk.Pokemon(pk.df_n[18,:])
bulbasaur = pk.Pokemon(pk.df_n[3,:])
liste_pok_j1 = [pikachu, rattata, bulbasaur]
J1 = pk.Joueur('j1', liste_pok_j1, 45)
C1 = tcc.Combat(J1, bulbasaur, pikachu)

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(769, 561)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(-10, 0, 771, 551))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("image/Galerie.jpg"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        
        
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(650, 480, 91, 21))
        self.pushButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("image/bouton fuite 4.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setIconSize(QtCore.QSize(96, 56))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.fctFuite)
        
              
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(630, 440, 111, 21))
        self.pushButton_2.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("image/bouton_changement_2.PNG"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_2.setIcon(icon1)
        self.pushButton_2.setIconSize(QtCore.QSize(117, 212))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.fctChangement)
        
        
        self.pushButton_3 = QtWidgets.QPushButton(Form)
        self.pushButton_3.setGeometry(QtCore.QRect(650, 400, 91, 21))
        self.pushButton_3.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("image/bouton petit attaque .png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_3.setIcon(icon2)
        self.pushButton_3.setIconSize(QtCore.QSize(95, 50))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.clicked.connect(self.fctActivationAttaque)
        
        
        self.pushButton_4 = QtWidgets.QPushButton(Form)
        self.pushButton_4.setGeometry(QtCore.QRect(510, 100, 231, 41))
        self.pushButton_4.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("image/bouton attaque spéciale 4.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_4.setIcon(icon3)
        self.pushButton_4.setIconSize(QtCore.QSize(230, 70))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_4.hide()
        self.pushButton_4.clicked.connect(self.fctAttSpe)

        
        self.pushButton_5 = QtWidgets.QPushButton(Form)
        self.pushButton_5.setGeometry(QtCore.QRect(510, 170, 231, 41))
        self.pushButton_5.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("image/bouton attaque neutre 4.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_5.setIcon(icon4)
        self.pushButton_5.setIconSize(QtCore.QSize(230, 70))
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_5.hide()
        self.pushButton_5.clicked.connect(self.fctAttSpl)
        
        
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(30, 360, 250, 150))
        self.label_2.setStyleSheet("background-color: rgb(226, 226, 226);")
        self.label_2.setObjectName("label_2")

        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(450, 300, 250, 100))
        self.label_3.setObjectName("labelAfficheResultatCombat")
        self.label_3.setStyleSheet('background-color: rgb(0, 89, 255);\n')
        self.label_3.setText("")
        self.label_3.hide()
        
        self.comboBoxChgmt = QtWidgets.QComboBox(Form)
        self.comboBoxChgmt.setGeometry(QtCore.QRect(200, 400, 231, 41))
        self.comboBoxChgmt.setObjectName("choixPokChgmt")
        for p in C1.joueur.list_pok:
            self.comboBoxChgmt.addItem(p.name)
        self.comboBoxChgmt.hide()
        self.comboBoxChgmt.currentIndexChanged.connect(self.fctChoixPokChgmt)
        self.pok_select_nom = self.comboBoxChgmt.currentText()
    
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_2.setText(_translate("Form", "Infos combat"))
        
    def fctActivationAttaque(self):
        """
        Activation d'une attaque

        Returns
        -------
        None.

        """
        txt = C1.afficheInfosCombat()
        self.label_2.setText(txt)
        if C1.is_spe_possible ==True:
            self.pushButton_4.show() #Cas dans lequel le joueur a fait une attaque spéciale il y a 3 tours
        self.pushButton_5.show()
        
        
    def fctFuite(self):
        """
        Activation d'une fuite: la fenêtre se ferme lorsque le joueur clique sur le bouton fuite

        Returns
        -------
        None.

        """
        C1.fuite()
        if C1.continuer_combat == False:
            print("\nVous fuyez !")
            self.close()
 
       
    def fctAttSpe(self):
        """
        Activation d'une attaque spéciale lorsque le joueur clique sur le bouton Attaque spéciale

        Returns
        -------
        None.

        """
        C1.choixSpe = 1
        C1.attaque()
        if C1.pok_def.hp_restant <= 0:
            self.close()
        self.pushButton_4.hide()
        self.pushButton_5.hide()
        C1.attPokSauvage()
        txt = C1.afficheInfosCombat()
        self.label_2.setText(txt)
        
        self.gestionMortPok()
            
    
    
    def fctAttSpl(self):
        """
        Activation d'une attaque simple lorsque le joueur clique sur le bouton Attaque neutre

        Returns
        -------
        None.

        """
        C1.choixSpe = 2 
        C1.attaque()
        if C1.pok_def.hp_restant <= 0:
            self.close()
        self.pushButton_4.hide()
        self.pushButton_5.hide()
        C1.attPokSauvage()
        txt = C1.afficheInfosCombat()
        self.label_2.setText(txt)
        
        self.gestionMortPok()
        
    def fctChangement(self):
        """
        Fonction qui affiche les différents pokémons possédés par le joueur sous forme de combo box

        Returns
        -------
        None.

        """
        self.comboBoxChgmt.show()
    
    
    def fctChoixPokChgmt(self):
        """
        Attribue au pokémon attaquant la valeur que le joueur a sélectionnée dans la combo box

        Returns
        -------
        None.

        """
        self.pok_select_nom = self.comboBoxChgmt.currentText()
        pok_att_origine = C1.pok_att
        for p in C1.joueur.list_pok:
            if p.name == self.pok_select_nom:
                if p != pok_att_origine and p != C1.pok_def: #on vérifie si le pokémon sélectionné n'est pas le pokémon attaquant ni le pokémon défenseur
                    C1.pok_att = p
                else:
                    print('Choisir un pokémon différent !')
        self.comboBoxChgmt.hide()
        txt = C1.afficheInfosCombat()
        self.label_2.setText(txt)
        if C1.pok_att.hp_restant > 0:
            self.pushButton_3.show()
            self.label_3.hide()
        
    def gestionMortPok(self):
        """
        Teste si le pokémon attaquant du joueur est mort 

        Returns
        -------
        None.

        """
        C1.testMortPokemonJoueur()
        if C1.is_att_possible == False:  # Si le pokemon attaquant est mort
            self.pushButton_3.hide()
            # C1.joueur.list_pok.remove(C1.pok_att)
            print("Pokémon encore en possession du joueur :")
            for p in C1.joueur.list_pok:
                print(p.name)
            self.label_3.show()
            self.label_3.setText("Votre pokemon est mort !\n\nVous n'avez plus qu'à le changer, ou à fuire...")
        
class XXXXWindow (QMainWindow, Ui_Form):
    def __init__(self, parent=None ):
        super(XXXXWindow, self).__init__(parent)
        self.setupUi(self)
        
        
 
def run_app_1():
   
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    mainWin = XXXXWindow()
    mainWin.show()
    app.exec_()

if __name__ == "__main__":
    
    run_app_1()