from PyQt5.QtWidgets import QApplication, QWidget, QStackedWidget, QVBoxLayout, QPushButton, QLabel

class PageOne(QWidget):
    def __init__(self, stack):
        super().__init__()
        self.stack = stack
        layout = QVBoxLayout()
        layout.addWidget(QLabel("This is Page One"))
        btn = QPushButton("Go to Page Two")
        btn.clicked.connect(lambda: self.stack.setCurrentIndex(1))
        layout.addWidget(btn)
        self.setLayout(layout)

class PageTwo(QWidget):
    def __init__(self, stack):
        super().__init__()
        self.stack = stack
        layout = QVBoxLayout()
        layout.addWidget(QLabel("This is Page Two"))
        btn = QPushButton("Go to Page One")
        btn.clicked.connect(lambda: self.stack.setCurrentIndex(0))
        layout.addWidget(btn)
        self.setLayout(layout)

app = QApplication([])
stack = QStackedWidget()
stack.addWidget(PageOne(stack))
stack.addWidget(PageTwo(stack))
stack.setCurrentIndex(0)
stack.resize(300, 200)
stack.show()
app.exec_()
