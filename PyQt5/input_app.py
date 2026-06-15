import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QLineEdit

# Case 1
def greet():
    name = input_box.text()
    label.setText(f"Hello, {name}!")

app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle('Greeting App')
window.setGeometry(550, 300, 350, 200)

# Label
label = QLabel('Enter your name:', window)
label.move(20, 20)

# Text Input
input_box = QLineEdit(window)
input_box.move(20, 50)
input_box.resize(200, 30)

# Button
button = QPushButton('Enter', window)
button.move(20, 90)
button.clicked.connect(greet)  # Connect button click to function

window.show()
sys.exit(app.exec_())








# Case 2
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QLineEdit
def greet1():
    name = text_input.text()
    label.setText(f"Acha {name} naam hai re tera Bidu")
    
app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle('Namaste Sabko!!!')
window.setGeometry(550, 300, 350, 200)

label = QLabel('Haa Re Shane, Kya Naam Hai Re Tera? Naam Daal Na Re Bidu: ', window)
label.move(20,20)
label.resize(400, 40) 
label.setWordWrap(True) 

text_input = QLineEdit(window)
text_input.move(20, 50)
text_input.resize(200, 30)

button = QPushButton('Daal Diya', window)
button.move(20,90)
button.clicked.connect(greet1)

 
window.show()
sys.exit(app.exec_())