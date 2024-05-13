from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
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
        self.label.setGeometry(QtCore.QRect(100, 80, 311, 61))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(40, 83, 175);\n"
"")
        self.label.setObjectName("label")
        self.frame = QtWidgets.QFrame(self.groupBox)
        self.frame.setGeometry(QtCore.QRect(30, 19, 311, 51))
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
        
        
        self.user_input = ""

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton.setText(_translate("Form", "Jouer "))
        self.label.setText(_translate("Form", "Nouveau Joueur "))
        
    def on_play_clicked(self):
        # Get the text from the QLineEdit and store it in the variable
        self.user_input = self.lineEdit.text()
        return self.user_input



if __name__ == "__main__":
    import sys 
    app= QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    app.setQuitOnLastWindowClosed(True)
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    app.exec_()
    name_player = ui.on_play_clicked()
    