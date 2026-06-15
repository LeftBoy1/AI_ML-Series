from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QIcon

class AppIconWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Window with Icon")
        self.setGeometry(100, 100, 300, 200)

        self.setWindowIcon(QIcon("profile.png"))  # Top-left window icon

app = QApplication([])
win = AppIconWindow()
win.show()
app.exec_()
