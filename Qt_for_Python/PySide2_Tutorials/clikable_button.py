# A simple clickable button tutorial
import sys
from PySide2.QtWidgets import QApplication, QPushButton


# Greetings
def say_hello():
    print("Button clicked, Hello!")


if __name__ == "__main__":
    # Create the Qt Application
    app = QApplication(sys.argv)
    # Create a button
    button = QPushButton("Exit")
    # Connect the button "clicked" signal to the exit() method
    # that finishes the QApplication
    button.clicked.connect(app.exit)
    # Show the button
    button.show()
    # Run the main Qt loop
    app.exec_()
