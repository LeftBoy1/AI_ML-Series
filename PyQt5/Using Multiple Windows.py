# Many apps need login → dashboard or main window → settings popup. You can implement this by switching between windows.


#BASIC
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QLabel, QDialog

class LoginWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Login")
        self.button = QPushButton("Login")
        self.button.clicked.connect(self.open_dashboard)

        layout = QVBoxLayout()
        layout.addWidget(QLabel("This is the login window"))
        layout.addWidget(self.button)
        self.setLayout(layout)

    def open_dashboard(self):
        self.dashboard = DashboardWindow()
        self.dashboard.show()
        self.close()  # Optional: Close the login window

class DashboardWindow(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Dashboard")
        layout = QVBoxLayout()
        layout.addWidget(QLabel("Welcome to the Dashboard!"))
        self.setLayout(layout)

app = QApplication([])
window = LoginWindow()
window.show()
app.exec_()


