import sys
import PyQt5
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QPainter, QBrush, QColor
from PyQt5.QtCore import Qt

class GameMap(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Game Map")
        self.setGeometry(100, 100, 800, 600)

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)

        # Dessiner les arbres
        painter.setBrush(QBrush(Qt.green))
        painter.drawEllipse(100, 100, 50, 50)
        painter.drawEllipse(200, 200, 50, 50)

        # Dessiner les chemins
        painter.setBrush(QBrush(Qt.gray))
        painter.drawRect(50, 50, 700, 500)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    event = PyQt5.QtGui.QPainter()
    gm = GameMap()
    gm.paintEvent(event)
    event.show()
    sys.exit(app.exec_())

