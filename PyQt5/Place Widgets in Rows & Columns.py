import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QLineEdit, QPushButton, QGridLayout
)

def greet():
    name = input_box.text()
    output_label.setText(f"Namaste {name} bhai!")

app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle("Grid Layout App")

# Widgets
name_label = QLabel("Naam:")
input_box = QLineEdit()

submit_btn = QPushButton("Daal Diya")
submit_btn.clicked.connect(greet)

output_label = QLabel("")
output_label.setWordWrap(True)

# Grid Layout
layout = QGridLayout()

layout.addWidget(name_label,    0, 0)
layout.addWidget(input_box,     0, 1)
layout.addWidget(submit_btn,    1, 0, 1, 2)  # spans 2 columns
layout.addWidget(output_label,  2, 0, 1, 2)

window.setLayout(layout)
window.resize(400, 200)
window.show()

sys.exit(app.exec_())
