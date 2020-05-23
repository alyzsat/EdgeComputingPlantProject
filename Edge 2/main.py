from PyQt5.QtWidgets import QWidget, QApplication
from threading import Thread
import sys
import socket


class PlantGUI(QWidget):
    def __init__(self):
        super().__init__()

        # Set the stylesheet to customize the GUI
        with open("stylesheet.css") as file:
            self.setStyleSheet(file.read())

        # Connection information
        self.host = socket.socket()

        self.display_plant_info()
        self.display_plant_status()
        self.show()

    def display_plant_info(self):
        """Displays information about the plant"""
        # Plant Name
        # Time Last Watered
        # Temperature
        # Ideal Humidity for Temperature
        # Estimated Time Until Watering Again
        # Estimated time Until Refill
        pass

    def display_plant_status(self):
        """Display whether or not the plant needs to be watered"""

        pass


if __name__ == "__main__":
    app = QApplication(sys.argv)
    gui = PlantGUI()
    sys.exit(app.exec_())
