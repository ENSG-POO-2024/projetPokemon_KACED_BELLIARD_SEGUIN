# -*- coding: utf-8 -*-
"""
Created on Wed May  8 19:26:10 2024

@author: laura
"""


            
# -*- coding: utf-8 -*-
"""
Created on Wed May  8 18:58:04 2024

@author: laura
"""
import random as rd
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1200, 1200)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(70, 30, 1000, 1000))  # Taille du frame
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")

        # Charger l'image une seule fois
        pixmap = QtGui.QPixmap("herbe.jpg")

        # Dessiner la pelouse sur tout le frame
        for x in range(0, 1000, 30):  # Boucle sur la largeur du frame
            for y in range(0, 1000, 30):  # Boucle sur la hauteur du frame
                label = QtWidgets.QLabel(self.frame)
                label.setGeometry(QtCore.QRect(x, y, 30, 30))  # Position et taille de chaque image d'arbre
                label.setPixmap(pixmap)  # Utiliser la même QPixmap pour toutes les images d'arbre
                label.setScaledContents(True)
                label.setObjectName("label")
                
        # Charger l'image d'arbre une seule fois
        pixmap1 = QtGui.QPixmap("arbre.jpg")

        # Dessiner les arbres sur tout le frame
        for _ in range(30):  # Boucle pour placer 10 arbres
            x = rd.randint(0, 970)  # Générer une coordonnée x aléatoire
            y = rd.randint(0, 970)  # Générer une coordonnée y aléatoire
            label1 = QtWidgets.QLabel(self.frame)
            label1.setGeometry(QtCore.QRect(x, y, 30, 30))  # Position et taille de chaque image d'arbre
            label1.setPixmap(pixmap1)  # Utiliser la même QPixmap pour toutes les images d'arbre
            label1.setScaledContents(True)
            label1.setObjectName("label")
            
        # # Ajouter un carré rouge
        # square = QtWidgets.QLabel(self.frame)
        # square.setGeometry(QtCore.QRect(600, 300, 30, 30))  # Position et taille du carré rouge
        # square.setStyleSheet("background-color: red")  # Définir la couleur de fond du carré rouge
        # square.setObjectName("square")
        
        # MainWindow.keyPressEvent = square.keyPressEvent
        
        self.square = MovableSquare(self.frame)
        self.square.setGeometry(QtCore.QRect(600, 300, 30, 30))  # Position et taille du carré rouge
        self.square.setStyleSheet("background-color: red")  # Définir la couleur de fond du carré rouge
        self.square.setObjectName("square")

        # Installer un filtre d'événement pour la fenêtre principale
        MainWindow.installEventFilter(self.square)


        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1200, 26))
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
        
        
class MovableSquare(QtWidgets.QLabel):
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
            
    def eventFilter(self, source, event):
        if event.type() == QtCore.QEvent.KeyPress:
            self.keyPressEvent(event)
            return True
        return super().eventFilter(source, event)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()  # Correct instantiation
    app.setQuitOnLastWindowClosed(True)
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    
    MainWindow.show()
    
    sys.exit(app.exec_())