import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QLineEdit, QVBoxLayout, QHBoxLayout, QSizePolicy


def greet():
    name = input_box.text()
    label.setText(f"Acha {name} naam hai re tera")

app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle('Namaste Layout Wale App 2')

# Create Widgets
label = QLabel('Haa Re Shane, Kya Naam Tera? Naam Daal Na Re Bidu:')
input_box = QLineEdit()
button = QPushButton('Daal Diya')
label.setWordWrap(True)
label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)  # <-- Let label expand

# Connect signal
button.clicked.connect(greet)

# Layout
layout = QHBoxLayout()
layout.addWidget(label)
layout.addWidget(input_box)
layout.addWidget(button)

# Apply layout to window
window.setLayout(layout)
window.resize(1920, 1080)
window.show()

sys.exit(app.exec_())
