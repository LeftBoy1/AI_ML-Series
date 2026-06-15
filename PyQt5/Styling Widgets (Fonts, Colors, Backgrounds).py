import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QPushButton,
    QLineEdit, QVBoxLayout, QSizePolicy
)
from PyQt5.QtGui import QFont

def greet():
    name = input_box.text()
    label.setText(f"Acha {name} naam hai re tera")

app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle('Styled App')

# Widgets
label = QLabel('Naam Daal Na Re Bidu:')
label.setWordWrap(True)
label.setFont(QFont('Comic Sans MS', 14))
label.setStyleSheet("color: darkred;")

input_box = QLineEdit()
input_box.setFont(QFont('Arial', 12))
input_box.setStyleSheet("background-color: grey;")
input_box.setText('Enter Here')

button = QPushButton('Daal Diya')
button.setFont(QFont('Verdana', 12, QFont.Bold))
button.setStyleSheet("background-color:  red; color: white;")

button.clicked.connect(greet)

# Layout
layout = QVBoxLayout()
layout.addWidget(label)
layout.addWidget(input_box)
layout.addWidget(button)

window.setLayout(layout)
window.resize(400, 200)
window.show()

sys.exit(app.exec_())
