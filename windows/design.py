# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'design.ui'
##
## Created by: Qt User Interface Compiler version 6.9.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect, Signal,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon, QMouseEvent,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QDateEdit, QHeaderView, QLineEdit,
    QMainWindow, QMenuBar, QPushButton, QSizePolicy, QComboBox, QHBoxLayout, QVBoxLayout,
    QStatusBar, QTableWidget, QTableWidgetItem, QWidget)

class CustomComboBox(QComboBox):

    beforePopup = Signal()

    def __init__(self, parent=None):
        super().__init__(parent)
        self.view().installEventFilter(self)  # Устанавливаем фильтр событий для выпадающего списка
        #self._is_dropdown_open = False # Флаг для отслеживания состояния выпадающего списка

    def mousePressEvent(self, event: QMouseEvent):
        """Перехватываем события мыши."""
        if self.isEditable(): # Если комбобокс редактируемый, то не проверяем нажатие на кнопку
           super().mousePressEvent(event)
           return

        arrow_rect = self.get_arrow_rect() # Получаем прямоугольник кнопки

        if arrow_rect.contains(event.pos()):
            # Клик произошел в области кнопки раскрытия списка
            self.beforePopup.emit()
            #self._is_dropdown_open = True
            self.showPopup() # Вызываем showPopup вручную, т.к. клик "съеден"
            #if not self._is_dropdown_open:
            #    print("Кнопка раскрытия списка нажата (открытие)")
            #    
            #else:
            #    print("Кнопка раскрытия списка нажата (закрытие)")
            #    self._is_dropdown_open = False # Сбрасываем флаг.
            #    self.hidePopup()
        else:
            super().mousePressEvent(event) # Передаем событие дальше

    def get_arrow_rect(self):
        """Определяет прямоугольник кнопки раскрытия списка."""
        # Это может потребовать адаптации в зависимости от стиля QComboBox
        # width = self.style().pixelMetric(self.style().PM_MenuButtonIndicator, self)
        width = self.width()
        height = self.height()
        #x = self.width() - width
        x = 0
        y = 0
        return QRect(x, y, width, height)

    def eventFilter(self, obj, event):
        """Фильтруем события для выпадающего списка."""
        if obj == self.view() and event.type() == QMouseEvent.MouseButtonRelease:
            self._is_dropdown_open = False  # Сбрасываем флаг при закрытии списка
        return super().eventFilter(obj, event)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow : QMainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)

        
        central_widget = QWidget(MainWindow)
        MainWindow.setCentralWidget(central_widget)

        vbox = QVBoxLayout(central_widget)

        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        vbox.addWidget(self.menubar)

        hbox1 = QHBoxLayout(central_widget)
        self.dateEdit = QDateEdit(MainWindow)
        self.dateEdit.setObjectName(u"dateEdit")
        hbox1.addWidget(self.dateEdit)
        self.combo = CustomComboBox(MainWindow)
        self.combo.setObjectName(u"combo")
        hbox1.addWidget(self.combo)
        vbox.addLayout(hbox1)

        self.tableWidget = QTableWidget(MainWindow)
        self.tableWidget.setObjectName(u"tableWidget")
        vbox.addWidget(self.tableWidget)

        hbox2 = QHBoxLayout()
        self.lineEdit = QLineEdit(MainWindow)
        self.lineEdit.setObjectName(u"lineEdit")
        hbox2.addWidget(self.lineEdit)
        self.pushButton = QPushButton(MainWindow)
        self.pushButton.setObjectName(u"pushButton")
        hbox2.addWidget(self.pushButton)
        vbox.addLayout(hbox2)

        
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")

        MainWindow.setStatusBar(self.statusbar)

        MainWindow.setLayout(vbox)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Croner", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", "Сохранить", None))
    # retranslateUi

