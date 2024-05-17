from PyQt5 import QtCore, QtGui, QtWidgets
import pokemons_final as pk
import page_combat as cf
import sys


pokemons = pk.pokemon_sauvage
pok_sauvage = 0


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
        self.label.setGeometry(QtCore.QRect(80, 80, 221, 51))
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
        self.label_2.setPixmap(QtGui.QPixmap("image/pokemon.png"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
       
        
        # Connecte le signal clicked du bouton à fermer_et_ouvrir_fenêtres pour fermer cette fenêtre et ouvrir la fenêtre principale
        self.pushButton.clicked.connect(self.fermer_et_ouvrir_fenetres)
        

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton.setText(_translate("Form", "Jouer "))
        self.label.setText(_translate("Form", "Nouveau Joueur "))
        
    def on_play_clicked(self):
        """
        Conserve le nom du joueur

        Returns
        -------
        TYPE: string
            DESCRIPTION.

        """
        
        self.user_input = self.lineEdit.text()
        return self.user_input
    
   
    def fermer_et_ouvrir_fenetres(self):
        """
        Ferme la fenêtre de formulaire et ouvre la carte

        Returns
        -------
        None.

        """
        self.main_window.show()  # Affiche la fenêtre principale
        self.Form.close()  # Ferme la fenêtre actuelle





class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1400, 1400)
        
        
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        
        
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(9,9,1400, 1400))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        
        pixmap = QtGui.QPixmap("image/GRASS.PNG")
        self.label1 = QtWidgets.QLabel(self.frame)
        self.label1.setGeometry(QtCore.QRect(9, 19, 1400, 1400)) 
        self.label1.setPixmap(pixmap) 
        self.label1.setScaledContents(True)
        self.label1.setObjectName("label")

        
        # Ajoute tous les pokémons à la carte 
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
            label.setStyleSheet("color: rgba( 0, 0, 0, 0);")
            label.setScaledContents(True)
            label.setObjectName(f"label_{idx}")
            label.setText(nom)
            self.pokemon_labels.append(label)
            
        # Carré rouge représentant le joueur
        self.square = Mouvement(self, self.frame)
        self.square.setGeometry(QtCore.QRect(600, 300, 30, 30))  # Position et taille du carré rouge
        self.square.setStyleSheet("background-color: red")  
        self.square.setObjectName("square")
        
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
        
    def ouvrir_page_combat(self):
        """
        Ouvre la page combat lorsque le joueur trouve un pokémon

        Returns
        -------
        None.

        """
        print("Opening combat page with:")
        self.combat_window = QtWidgets.QMainWindow()
        self.mainWin = cf.XXXXWindow()
        self.mainWin.show()

    
        
class Mouvement(QtWidgets.QLabel):
    def __init__(self, main_window, parent=None):
        super(Mouvement, self).__init__(parent)
        self.main_window = main_window
        self.timer = QtCore.QTimer(self)  
        self.timer.timeout.connect(self.reset_label_color)
        self.timer.setSingleShot(True)
        self.is_stopped = False
 
    def keyPressEvent(self, event):
        # Récupérer la position actuelle du joueur
        current_pos = self.pos()

        # Déplacer le joueur en fonction de la touche appuyée
        if event.key() == QtCore.Qt.Key_Left:
            self.move(current_pos.x() - 10, current_pos.y())
        elif event.key() == QtCore.Qt.Key_Right:
            self.move(current_pos.x() + 10, current_pos.y())
        elif event.key() == QtCore.Qt.Key_Up:
            self.move(current_pos.x(), current_pos.y() - 10)
        elif event.key() == QtCore.Qt.Key_Down:
            self.move(current_pos.x(), current_pos.y() + 10)
            
        # Vérifier la distance entre le joueur et chaque Pokémon
        for label in self.main_window.pokemon_labels:
            pokemon_pos = label.pos()
            
            distance = ((current_pos.x() - pokemon_pos.x()) ** 2 + (current_pos.y() - pokemon_pos.y()) ** 2) ** 0.5
            if distance < 20: 
                label.setStyleSheet("color: yellow")  # Change la couleur du nom du Pokémon en jaune
                self.main_window.ouvrir_page_combat()
                
            else:
                label.setStyleSheet("color: rgba( 0, 0, 0, 0);")  # Remet la couleur du nom du Pokémon à transparent
            
        self.current_pos = self.pos()
        return current_pos
    
    def reset_label_color(self):
        for label in self.main_window.pokemon_labels:
            label.setStyleSheet("color: rgba( 0, 0, 0, 0);")  # Remet la couleur du nom du Pokémon à transparent
        self.is_stopped = False
            
    def eventFilter(self, source, event):
        if event.type() == QtCore.QEvent.KeyPress:
            self.keyPressEvent(event)
            return True
        return super().eventFilter(source, event)
    
    
    
        
def run_app():
    
    app = QtWidgets.QApplication(sys.argv)
    
    # Create main window
    main_window = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(main_window)
    
    # Create and show the initial form
    Form = QtWidgets.QWidget()
    ui_form = Ui_Form(main_window)  # Pass the main window to the Ui_Form
    ui_form.setupUi(Form)
    Form.show()
    
    sys.exit(app.exec_())

if __name__ == "__main__":
    run_app()      
    


