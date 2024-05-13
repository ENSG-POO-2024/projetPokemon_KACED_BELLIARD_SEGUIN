
import random as rd
from PyQt5 import QtCore, QtGui, QtWidgets
from deplacement_joueur import *





pokemons = dj.pok_jeu

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
        
        # # Charger l'image une seule fois
        # pixmap = QtGui.QPixmap("herbe.jpg")

        # # Dessiner la pelouse sur tout le frame
        # for x in range(0, 5000, 30):  # Boucle sur la largeur du frame
        #     for y in range(0, 5000, 30):  # Boucle sur la hauteur du frame
        #         label = QtWidgets.QLabel(self.frame)
        #         label.setGeometry(QtCore.QRect(x, y, 30, 30))  # Position et taille de chaque image d'arbre
        #         label.setPixmap(pixmap)  # Utiliser la même QPixmap pour toutes les images d'arbre
        #         label.setScaledContents(True)
        #         label.setObjectName("label")
                
        # # Charger l'image d'arbre une seule fois
        # pixmap1 = QtGui.QPixmap("arbre.jpg")

        # # Dessiner les arbres sur tout le frame
        # for _ in range(30):  # Boucle pour placer 10 arbres
        #     x = rd.randint(0, 4980)  # Générer une coordonnée x aléatoire
        #     y = rd.randint(0, 4980)  # Générer une coordonnée y aléatoire
        #     label1 = QtWidgets.QLabel(self.frame)
        #     label1.setGeometry(QtCore.QRect(x, y, 30, 30))  # Position et taille de chaque image d'arbre
        #     label1.setPixmap(pixmap1)  # Utiliser la même QPixmap pour toutes les images d'arbre
        #     label1.setScaledContents(True)
        #     label1.setObjectName("label")

        
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
            label.setStyleSheet("color: rgba( 0, 0, 0, 0);\n"
                                "background-color: rgba( 0, 0, 0, 0);")
            label.setScaledContents(True)
            label.setObjectName(f"label_{idx}")
            label.setText(nom)
            self.pokemon_labels.append(label)
            
        self.square = Player(self.frame)
        self.square.setGeometry(QtCore.QRect(600, 300, 30, 30))  # Position et taille du carré rouge
        self.square.setStyleSheet("background-color: red")  # Définir la couleur de fond du carré rouge
        self.square.setObjectName("square")
        
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

    
        
class Player(QtWidgets.QLabel):
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
            
        # Vérifier la distance entre le carré rouge et chaque Pokémon
        for label in ui.pokemon_labels:
            pokemon_pos = label.pos()
            distance = ((current_pos.x() - pokemon_pos.x()) ** 2 + (current_pos.y() - pokemon_pos.y()) ** 2) ** 0.5
            if distance < 20:  # 20 pixels est la distance approximative entre le centre du carré et le coin
                label.setStyleSheet("color: yellow")  # Changer la couleur du nom du Pokémon en jaune
            else:
                label.setStyleSheet("color: rgba( 0, 0, 0, 0);")  # Remettre la couleur du nom du Pokémon à transparent
            
        self.current_pos = self.pos()
        return self.current_pos
            
    def eventFilter(self, source, event):
        if event.type() == QtCore.QEvent.KeyPress:
            self.keyPressEvent(event)
            return True
        return super().eventFilter(source, event)

if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    app.setQuitOnLastWindowClosed(True)
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())