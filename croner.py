import random 

import settings.settings as sett
import database.database as db

from PySide6.QtWidgets import QApplication, QMainWindow
from windows.design import Ui_MainWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.pushButton.clicked.connect(self.generate_number)

    def generate_number(self):
        number = random.randint(1, 100)
        self.ui.label.setText(str(number))

def main():
    settings = sett.Settings()
    database = db.DataBase(settings)

    app = QApplication()
    window = MainWindow()
    window.show()
    app.exec()

if __name__ == "__main__":
    main()