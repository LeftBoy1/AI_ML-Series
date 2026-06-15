from PyQt5.QtWidgets import QApplication, QLabel, QWidget, QVBoxLayout

class CustomLabel(QLabel):
    def __init__(self, text):
        super().__init__(text)
        self.setStyleSheet("color: blue; font-size: 20px; font-weight: bold;")

class CustomWidgetDemo(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Custom Widget")
        layout = QVBoxLayout()
        layout.addWidget(CustomLabel("Hello from Custom Widget!"))
        self.setLayout(layout)

app = QApplication([])
win = CustomWidgetDemo()
win.show()
app.exec_()
