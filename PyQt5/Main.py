import sys
from PyQt5.QtWidgets import QApplication, QLabel, QWidget

app = QApplication(sys.argv)  # Create app
window = QWidget()            # Create main window
window.setWindowTitle('Hello PyQt5')  # Set window title
window.setGeometry(550, 300, 300, 200)  # x, y, width, height

label = QLabel('<h2>Welcome to PyQt5!</h2>', parent=window)  # Add a label
label.move(60, 80)  # Position label

window.show()  # Show the window
sys.exit(app.exec_())  # Run the app
