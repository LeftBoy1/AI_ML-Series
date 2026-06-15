# GUI Design Without Coding
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QWidget

app = QApplication([])
window = uic.loadUi("form.ui")  # Load the saved UI file
window.show()
app.exec_()
