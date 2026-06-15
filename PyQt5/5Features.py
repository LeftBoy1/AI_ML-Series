from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QLineEdit
from PyQt5.QtGui import QPixmap, QIcon
from PyQt5.QtCore import QPropertyAnimation

class LoginApp(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi(r"F:\Devansh Gupta\AI + ML\PyQt5\Projects\login.ui", self)

        # Set background and styling
        self.setStyleSheet("background-color: #f0f0f0;")
        self.lineEdit_username.setStyleSheet("background-color: white;")
        self.lineEdit_password.setStyleSheet("background-color: white;")

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

        # Profile picture (optional)
        pixmap = QPixmap(r"F:\Devansh Gupta\AI + ML\PyQt5\profile.png")
        self.label_profile.setPixmap(pixmap)
        self.label_profile.setScaledContents(True)

        # Password visibility toggle
        self.checkBox_show.stateChanged.connect(self.toggle_password)

        # Login button click
        self.pushButton_login.clicked.connect(self.handle_login)

        # Attempt tracking
        self.login_attempts = 0
        self.max_attempts = 3

    def toggle_password(self):
        if self.checkBox_show.isChecked():
            self.lineEdit_password.setEchoMode(QLineEdit.Normal)
        else:
            self.lineEdit_password.setEchoMode(QLineEdit.Password)

    def fade_message(self):
        animation = QPropertyAnimation(self.label_message, b"windowOpacity")
        animation.setDuration(800)
        animation.setStartValue(0)
        animation.setEndValue(1)
        animation.start()

    def handle_login(self):
        username = self.lineEdit_username.text()
        password = self.lineEdit_password.text()

        if username == "admin" and password == "1234":
            self.label_message.setText("✅ Login Successful!")
            self.label_message.setStyleSheet("color: green; font-size: 18px; font-weight: bold;")
            self.fade_message()
            self.login_attempts = 0
            self.lineEdit_username.clear()      #username fields getting cleared after clicking the login button
            self.lineEdit_password.clear()      #password fields getting cleared after clicking the login button
        else:
            self.login_attempts += 1
            remaining = self.max_attempts - self.login_attempts
            self.label_message.setText(f"❌ Invalid Credentials ({remaining} left)")
            self.label_message.setStyleSheet("color: red; font-size: 18px; font-weight: bold;")
            self.fade_message()
            self.lineEdit_password.clear()

            if self.login_attempts >= self.max_attempts:
                self.label_message.setText("🚫 Too many attempts! Access blocked.")
                self.pushButton_login.setEnabled(False)

# Run the App
app = QApplication([])
window = LoginApp()
window.show()
app.exec_()
