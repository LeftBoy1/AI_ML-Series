from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout
from PyQt5.QtCore import QTimer

class TimerWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Auto Close Example")

        layout = QVBoxLayout()
        layout.addWidget(QLabel("Window will close in 5 seconds"))
        self.setLayout(layout)

        timer = QTimer(self)
        timer.timeout.connect(self.close)
        timer.setSingleShot(True)
        timer.start(5000)  # 5 seconds

app = QApplication([])
win = TimerWindow()
win.show()
app.exec_()
