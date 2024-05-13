import numpy as np
import random as rd
import pandas as pd
from PyQt5 import QtCore, QtGui, QtWidgets

a=30 
p=2


pok = pd.read_csv("../data/pokemon_first_gen.csv") #Lecture de la base de données des pokémons avec le module pandas
pok_init = pok.values.tolist()#Transformation du tableau panda en liste
list_pok_joueur = rd.sample(pok_init,k=10)#Choix aléatoire de 10 pokémons pour le joueur 
pok_jeu = [i for i in pok_init if i not in list_pok_joueur]#liste des pokémons présents sur la carte
pos_pok_init = pd.read_csv("../data/pokemon_coordinates.csv")#Lecture des coordonnées des pokemons
pos_pok = pos_pok_init.values.tolist()#Transformation du tableau en liste



#Tranformation des coordonnées (chaine de caractère) en liste
for i in range(len(pos_pok)):
    b = pos_pok[i][1]
    l = eval(b)
    pos_pok[i] = [pos_pok[i][0], l]

#Liste des pokémons uniques contenant toutes les informations (dont les coordonnées)
    for j in range(len(pok_jeu)):
        if pos_pok[i][0] == pok_jeu[j][1]:
            if len(pok_jeu[j]) == 13:
                pok_jeu[j].append(pos_pok[i][1])
                x = int(pok_jeu[j][13][0]) + rd.randint(0,10)
                y = int(pok_jeu[j][13][1]) + rd.randint(0,10)
                pok_jeu[j][13][0] = x
                pok_jeu[j][13][1] = y
    
pokemons = pok_jeu

pos_init = [600,300]

class MovableSquare(QtWidgets.QLabel):
    positionChanged = QtCore.pyqtSignal(QtCore.QPoint)
    
    def keyPressEvent(self, event):
        # Récupérer la position actuelle du carré
        current_pos = self.pos()

        # Déplacer le carré en fonction de la touche appuyée
        if event.key() == QtCore.Qt.Key_Left:
            self.move(current_pos.x() - 10, current_pos.y())
        elif event.key() == QtCore.Qt.Key_Right:
            self.move(current_pos.x() + 10, current_pos.y())
        elif event.key() == QtCore.Qt.Key_Up:
            self.move(current_pos.x(), current_pos.y() - 10)
        elif event.key() == QtCore.Qt.Key_Down:
            self.move(current_pos.x(), current_pos.y() + 10)
            
        self.current_pos = self.pos()
        self.positionChanged.emit(self.current_pos)
        return self.current_pos
            
    def eventFilter(self, source, event):
        if event.type() == QtCore.QEvent.KeyPress:
            self.keyPressEvent(event)
            return True
        return super().eventFilter(source, event)


class Pokemons():
    def __init__():
        pass

class Player(Pokemons,MovableSquare):
    def __init__(self, nom, list_pok_joueur, pos_init):
        self.nom = nom
        self. list_pok_joueur = list_pok_joueur
        self.pos_init = pos_init
        
    def currentPosition(self):
        return MovableSquare.keyPressEvent(self)
        
    def FindPokemon(self, new_pos, pokemons):
        for idx, pokemon in enumerate(pokemons):
            d = np.sqrt( (new_pos.x() - pokemon[13][0])**2 + (new_pos.y() - pokemon[13][1])**2 )
            if d <= 1: 
                return d  # Retourne la distance si un Pokémon est trouvé à proximité
        return None  # Retourne None si aucun Pokémon n'est trouvé à proximité

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(5000, 5000)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(9, 9, 5000, 5000))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.frame.setStyleSheet("background-color: green")
        
        
        # Add Pokémon labels dynamically
        self.pokemon_labels = []
        for idx, pokemon_data in enumerate(pokemons):
            nom = pokemon_data[1]
            position = pokemon_data[13]
            label = QtWidgets.QLabel(self.frame)
            label.setGeometry(QtCore.QRect(position[0]*10*5+rd.randint(-10,10), position[1]*10*5+rd.randint(-10,10), 81, 31))
            font = QtGui.QFont()
            font.setPointSize(10)
            font.setBold(True)
            font.setWeight(75)
            label.setFont(font)
            label.setStyleSheet("color: rgb(0, 0, 0, 0);\n"
                                "background-color: rgb(0, 0, 0, 0);")
            label.setScaledContents(True)
            label.setObjectName(f"label_{idx}")
            label.setText(nom)
            self.pokemon_labels.append(label)
        
        self.square = MovableSquare(self.frame)
        self.square.setGeometry(QtCore.QRect(600, 300, 30, 30))  # Position et taille du carré rouge
        self.square.setStyleSheet("background-color: red")  # Définir la couleur de fond du carré rouge
        self.square.setObjectName("square")
        
        
        # Connecter le signal positionChanged du carré à la méthode updatePokemonLabels
        self.square.positionChanged.connect(self.updatePokemonLabels)
        
        # Installer un filtre d'événement pour la fenêtre principale
        MainWindow.installEventFilter(self.square)
        
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 856, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        
    def updatePokemonLabels(self, new_pos):
        player = Player("Nom", list_pok_joueur, pos_init)
        for idx, pokemon_data in enumerate(pokemons):
            # Créer une instance de la classe Player
            d = player.FindPokemon(new_pos, [pokemon_data])  # Utiliser l'instance player pour appeler FindPokemon
            label = self.pokemon_labels[idx]
            if d is not None:
                label.setStyleSheet("color: rgba(0, 0, 0, 0);\n"
                                    "background-color: rgba(0, 0, 0, 0);")
            else:
                label.setStyleSheet("color: rgb(255, 210, 47);\n"
                                    "background-color: rgb(51, 68, 167);")
    
        
        


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())   

