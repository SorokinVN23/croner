import random 

import settings.settings as sett
import database.database as db

from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtCore import Slot, QDate
from windows.design import Ui_MainWindow
from core.core import Core

class MainWindow(QMainWindow):
    def __init__(self, core : Core):
        super().__init__()
        
        self.core = core
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.pushButton.clicked.connect(self.save_text)
        self.ui.combo.beforePopup.connect(self.fill_combo)
        self.ui.combo.currentIndexChanged.connect(self.update_date)

        self.combo_update_processing = False
        self.fill_combo()
        self.update_date()

    def generate_number(self):
        number = random.randint(1, 100)
        self.ui.label.setText(str(number))

    def save_text(self):
        text = self.ui.lineEdit.text()
        self.core.save(text)
        self.ui.lineEdit.setText("")

    @Slot()
    def fill_combo(self):
        self.combo_update_processing = True
        record_dates = self.core.get_record_dates()
        self.ui.combo.clear()
        self.combo_update_processing = False
        self.ui.combo.addItems(record_dates)
    
    @Slot()
    def update_date(self):
        if self.combo_update_processing == False:
            text = self.ui.combo.currentText()
            date = QDate.fromString(text, "yyyy-MM-dd")
            self.ui.dateEdit.setDate(date)
         

def main():
    settings = sett.Settings()
    database = db.DataBase(settings)
    core = Core(database)

    app = QApplication()
    window = MainWindow(core)
    window.show()
    app.exec()

if __name__ == "__main__":
    main()