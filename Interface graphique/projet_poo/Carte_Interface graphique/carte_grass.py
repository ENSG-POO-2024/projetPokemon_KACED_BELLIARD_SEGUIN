# -*- coding: utf-8 -*-
"""
Created on Wed May  8 18:58:04 2024

@author: laura
"""

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

        # Charger l'image d'arbre une seule fois
        pixmap = QtGui.QPixmap("herbe.jpg")

        # Dessiner les arbres sur tout le frame
        for x in range(0, 1000, 30):  # Boucle sur la largeur du frame
            for y in range(0, 1000, 30):  # Boucle sur la hauteur du frame
                label = QtWidgets.QLabel(self.frame)
                label.setGeometry(QtCore.QRect(x, y, 30, 30))  # Position et taille de chaque image d'arbre
                label.setPixmap(pixmap)  # Utiliser la même QPixmap pour toutes les images d'arbre
                label.setScaledContents(True)
                label.setObjectName("label")

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

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()  # Correct instantiation
    app.setQuitOnLastWindowClosed(True)
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())