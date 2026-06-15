from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtGui import QIcon

class IconButtonWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Button with Icon")
        self.setGeometry(100, 100, 300, 200)

        button = QPushButton("Login", self)
        button.setIcon(QIcon("profile.png"))  # Make sure login.png is in the same folder
        button.setIconSize(button.sizeHint())  # Optional: scale icon to button size
        button.move(100, 80)

app = QApplication([])
win = IconButtonWindow()
win.show()
app.exec_()
