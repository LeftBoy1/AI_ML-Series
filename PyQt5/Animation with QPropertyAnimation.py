from PyQt5.QtWidgets import QApplication, QPushButton, QWidget
from PyQt5.QtCore import QPropertyAnimation, QRect

class AnimationWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Button Animation")
        self.resize(400, 300)

        self.button = QPushButton("Animate Me", self)
        self.button.setGeometry(50, 50, 120, 40)

        self.anim = QPropertyAnimation(self.button, b"geometry")
        self.anim.setDuration(1000)
        self.anim.setStartValue(QRect(50, 50, 120, 40))
        self.anim.setEndValue(QRect(200, 200, 120, 40))
        self.button.clicked.connect(self.anim.start)

app = QApplication([])
win = AnimationWindow()
win.show()
app.exec_()
