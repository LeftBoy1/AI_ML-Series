from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QLineEdit
from PyQt5.QtGui import QFont

class LoginApp(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi(r"F:\Devansh Gupta\AI + ML\PyQt5\Projects\login.ui", self)

        # Optional: Change font for better visuals
        # self.setFont(QFont("Comic Sans MS", 14))
        
        #STYLING
        self.setStyleSheet("background-color: lightgrey;")
        
        self.lineEdit_username.setStyleSheet("background-color: white;")
        self.lineEdit_password.setStyleSheet("background-color: white;")
        
        self.label_message.setStyleSheet("color: red; font-weight: bold;")

        self.pushButton_login.setStyleSheet("""
    QPushButton {
        background-color: green;     
        color: white;
        padding: 8px;
        border-radius: 6px;
    }
    QPushButton:hover {
        background-color: darkgreen;     
    }
""")
        

        self.label_message.move(270,380)

        self.label_message.setStyleSheet("""
    font-size: 18px;
    font-weight: bold;
""")

        # Connect button
        self.pushButton_login.clicked.connect(self.handle_login)


    def handle_login(self):
        username = self.lineEdit_username.text()
        password = self.lineEdit_password.text()

        # Simple check (you can later use file/db check here)
        if username == "admin" and password == "1234":
            self.label_message.setText("✅ Login Successful!")
            self.label_message.setStyleSheet("color: green; font-size: 18px; font-weight: bold;")
        else:
            self.label_message.setText("❌ Invalid Credentials")
            self.label_message.setStyleSheet("color: red; font-size: 18px; font-weight: bold;")

app = QApplication([])
window = LoginApp()
window.show()
app.exec_()
