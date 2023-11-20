import io
import sys
import random

from PyQt5 import uic
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QApplication, QWidget


class YellowCircles(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi("UI.ui", self)
        self.setWindowTitle('Жёлтые круги')
        self.initUI()

    def initUI(self):
        self.setFixedSize(536, 573)
        self.click = False
        self.generateBtn.clicked.connect(self.generate)

    def generate(self):
        self.click = True
        self.repaint()

    def paintEvent(self, event):
        if self.click:
            qp = QPainter()
            qp.begin(self)
            self.draw_circle(qp)
            qp.end()
        self.click = False

    def draw_circle(self, qp):
        qp.setBrush(QColor(255, 255, 0))
        d = random.randint(10, 500)
        qp.drawEllipse(10, 10, d, d)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = YellowCircles()
    ex.show()
    sys.exit(app.exec())