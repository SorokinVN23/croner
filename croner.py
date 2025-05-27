import random 

import settings.settings as sett
import database.database as db
import datetime

from PySide6.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QHeaderView
#import PySide6.QtWidgets as qw
from PySide6.QtCore import Slot, QDate
from windows.design import Ui_MainWindow
from core.core import Core

class MainWindow(QMainWindow):
    def __init__(self, core : Core):
        super().__init__()
        
        self.core = core
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.dates = tuple()

        self.ui.tableWidget.setColumnCount(3)
        self.ui.tableWidget.setHorizontalHeaderLabels(["Время", "Текст", "Идентификатор"])

        header = self.ui.tableWidget.verticalHeader()
        header.setStyleSheet("QHeaderView::section{Background-color:rgb(220,220,220);}")

        header = self.ui.tableWidget.horizontalHeader()
        header.setStyleSheet("QHeaderView::section{Background-color:rgb(220,220,220);}")

        self.ui.tableWidget.setColumnWidth(0, 130)
        header.setSectionResizeMode(0, QHeaderView.Fixed)

        self.ui.tableWidget.setColumnWidth(1, 500)
        header.setSectionResizeMode(1, QHeaderView.Stretch)

        header.setSectionResizeMode(2, QHeaderView.ResizeToContents)

        self.ui.pushButton.clicked.connect(self.save_text)
        self.ui.combo.beforePopup.connect(self.fill_combo)
        self.ui.combo.currentIndexChanged.connect(self.update_date)
        self.ui.dateEdit.dateChanged.connect(self.fill_table)

        self.combo_update_processing = False
        self.fill_combo()
        self.update_date()
        #self.fill_table()

    def generate_number(self):
        number = random.randint(1, 100)
        self.ui.label.setText(str(number))

    def save_text(self):
        text = self.ui.lineEdit.text()
        if text != "":
            self.core.save(text)
            self.ui.lineEdit.setText("")

        self.fill_table()
        self.ui.lineEdit.setFocus()

    @Slot()
    def fill_combo(self):
        record_dates = self.core.get_record_dates()

        if self.dates == record_dates:
            return

        self.dates = record_dates
        self.combo_update_processing = True
        self.ui.combo.clear()
        self.combo_update_processing = False
        self.ui.combo.addItems(record_dates)
    
    @Slot()
    def update_date(self):
        if self.combo_update_processing == False:
            text = self.ui.combo.currentText()
            date = QDate.fromString(text, "yyyy-MM-dd")
            self.ui.dateEdit.setDate(date)

    @Slot()    
    def fill_table(self):
        qdate = self.ui.dateEdit.date()
        date = datetime.date(qdate.year(), qdate.month(), qdate.day())

        records = self.core.get_date_records(date)
        row_count = len(records)
        self.ui.tableWidget.setRowCount(row_count)

        row_index = -1
        for row in records:
            row_index += 1

            col_index = -1
            for col in row:
                col_index += 1

                item = QTableWidgetItem(str(col))
                self.ui.tableWidget.setItem(row_index, col_index, item)

        #header = self.ui.tableWidget.horizontalHeader()
        #header.setSectionResizeMode(QHeaderView.ResizeToContents)
        
        #self.ui.tableWidget.setColumnWidth(1, 500)
        #header.setSectionResizeMode(1, QHeaderView.Fixed)
       
     

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