from PyQt5.QtWidgets import QApplication, QLabel, QWidget, QVBoxLayout
from PyQt5.QtGui import QPixmap

class ImageWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Show Image")
        layout = QVBoxLayout()
        
        label = QLabel()
        pixmap = QPixmap("profile.png")  # Replace with your image path
        label.setPixmap(pixmap)
        layout.addWidget(label)

        self.setLayout(layout)

app = QApplication([])
win = ImageWindow()
win.show()
app.exec_()
