import sys

from PyQt5.QtGui import QPainter, QColor, QPainterPath
from PyQt5.QtWidgets import QMainWindow, QApplication
import random
from PyQt5.QtCore import Qt
import UI


class Window(QMainWindow, UI.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.flag = False
        self.pushButton.clicked.connect(self.result)

    def paintEvent(self, event):
        if self.flag:
            self.qp = QPainter()
            self.qp.begin(self)
            self.draw()
            self.qp.end()

    def draw(self):
        self.colors = [random.randrange(255), random.randrange(255), random.randrange(255)]
        self.coords = [random.randrange(596), random.randrange(727)]
        size = random.randrange(300)
        self.qp.setBrush(QColor(*self.colors))
        self.qp.drawEllipse(*self.coords, size, size)

    def result(self):
        self.flag = True
        self.update()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Window()
    ex.show()
    sys.exit(app.exec())
