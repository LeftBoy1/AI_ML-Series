from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox

class PopupExample(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Popup Demo")
        button = QPushButton("Show Popup", self)
        button.clicked.connect(self.show_popup)

    def show_popup(self):
        msg = QMessageBox()
        msg.setWindowTitle("Warning")
        msg.setText("Incorrect Password")
        msg.setIcon(QMessageBox.Warning)
        msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        msg.exec_()

app = QApplication([])
win = PopupExample()
win.show()
app.exec_()
