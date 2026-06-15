# You can define custom signals using pyqtSignal, which is useful for communication between components.

from PyQt5.QtCore import pyqtSignal, QObject

class Communicate(QObject):
    speak = pyqtSignal(str)

def say_something(message):
    print("Signal received:", message)

com = Communicate()
com.speak.connect(say_something)
com.speak.emit("Hello from signal!")
