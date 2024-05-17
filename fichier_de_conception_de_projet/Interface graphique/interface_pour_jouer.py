from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    
    def __init__(self, main_window):
        self.main_window = main_window
    
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(362, 271)
        self.groupBox = QtWidgets.QGroupBox(Form)
        self.groupBox.setGeometry(QtCore.QRect(0, 0, 361, 271))
        self.groupBox.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.pushButton = QtWidgets.QPushButton(self.groupBox)
        self.pushButton.setGeometry(QtCore.QRect(80, 210, 191, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("background-color: rgb(255, 0, 0);\n"
"color: rgb(255, 255, 255);")
        self.pushButton.setObjectName("pushButton")
        self.lineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit.setGeometry(QtCore.QRect(20, 140, 321, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet("color: rgb(40, 83, 175);\n"
"background-color: rgb(250, 207, 51);")
        self.lineEdit.setText("")
        self.lineEdit.setFrame(False)
        self.lineEdit.setCursorPosition(0)
        self.lineEdit.setReadOnly(False)
        self.lineEdit.setObjectName("lineEdit")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(100, 80, 171, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(40, 83, 175);\n"
"")
        self.label.setObjectName("label")
        self.frame = QtWidgets.QFrame(self.groupBox)
        self.frame.setGeometry(QtCore.QRect(30, 19, 311, 61))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(0, 0, 311, 61))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("pokemon.png"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        
        self.pushButton.clicked.connect(Form.close)
        # Connect the closed signal of the form to open_main_window function of the main window
        Form.closed.connect(self.main_window.show)
        

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton.setText(_translate("Form", "Jouer "))
        self.label.setText(_translate("Form", "Nouveau Joueur "))
        
    def on_play_clicked(self):
        # Get the text from the QLineEdit and store it in the variable
        self.user_input = self.lineEdit.text()
        return self.user_input

import random as rd
from PyQt5 import QtCore, QtGui, QtWidgets
import pokemons_final as p
from PyQt5.QtWidgets import QApplication, QWidget
pokemons = p.pokemons




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
            label.setGeometry(QtCore.QRect(position[0], position[1], 81, 31))
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

# if __name__ == "__main__":
#     import sys

#     app = QtWidgets.QApplication(sys.argv)
#     MainWindow = QtWidgets.QMainWindow()
#     app.setQuitOnLastWindowClosed(True)
#     ui = Ui_MainWindow()
#     ui.setupUi(MainWindow)
#     MainWindow.show()
#     sys.exit(app.exec_())
        



# if __name__ == "__main__":
#     import sys 
#     app= QtWidgets.QApplication(sys.argv)
#     Form = QtWidgets.QWidget()
#     app.setQuitOnLastWindowClosed(True)
#     ui = Ui_Form()
#     ui.setupUi(Form)
#     Form.show()
#     app.exec_()
#     name_player = ui.on_play_clicked()

if __name__ == "__main__":
    import sys 
    
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    app.setQuitOnLastWindowClosed(True)
    
    # Create an instance of your main window
    main_window = QtWidgets.QMainWindow()
    ui_main_window = Ui_MainWindow()
    ui_main_window.setupUi(main_window)
    main_window.show()
    
    # Pass the main window instance to the form
    ui = Ui_Form(main_window)
    ui.setupUi(Form)
    Form.show()
    
    sys.exit(app.exec_())