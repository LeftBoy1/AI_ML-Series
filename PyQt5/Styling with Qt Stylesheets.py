from PyQt5.QtWidgets import QApplication, QWidget, QPushButton

class StyledWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Styled Button")
        button = QPushButton("Click Me", self)
        button.setStyleSheet("""
            QPushButton {
                background-color: #4CAF50;
                color: white;
                font-size: 16px;
                padding: 10px;
                border-radius: 10px;
            }
            QPushButton:hover {
                background-color: #45a049;
            }
        """)
        button.move(50, 50)

app = QApplication([])
win = StyledWindow()
win.resize(200, 150)
win.show()
app.exec_()
