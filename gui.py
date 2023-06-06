from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import *
import sys
import main


#Класс окна приложения с объявляением всех элементов
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(400, 150)
        MainWindow.setMinimumSize(QtCore.QSize(400, 150))
        MainWindow.setMaximumSize(QtCore.QSize(400, 150))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 10, 41, 17))
        self.label.setObjectName("label")
        self.path_line = QtWidgets.QLineEdit(self.centralwidget)
        self.path_line.setGeometry(QtCore.QRect(60, 10, 241, 25))
        self.path_line.setObjectName("path_line")
        self.ruRadio = QtWidgets.QRadioButton(self.centralwidget)
        self.ruRadio.setGeometry(QtCore.QRect(20, 50, 41, 23))
        self.ruRadio.setObjectName("ruRadio")
        self.enRadio = QtWidgets.QRadioButton(self.centralwidget)
        self.enRadio.setGeometry(QtCore.QRect(80, 50, 41, 23))
        self.enRadio.setObjectName("enRadio")
        self.startButton = QtWidgets.QPushButton(self.centralwidget)
        self.startButton.setGeometry(QtCore.QRect(330, 50, 51, 25))
        self.startButton.setObjectName("startButton")
        self.fileButton = QtWidgets.QPushButton(self.centralwidget)
        self.fileButton.setShortcut('Ctrl+O')
        self.fileButton.setGeometry(QtCore.QRect(310, 10, 31, 25))
        self.fileButton.setObjectName("fileButton")
        self.FAQButton = QtWidgets.QPushButton(self.centralwidget)
        self.FAQButton.setGeometry(QtCore.QRect(350, 10, 31, 25))
        self.FAQButton.setObjectName("FAQButton")
        self.alert_label = QtWidgets.QLabel(self.centralwidget)
        self.alert_label.setGeometry(QtCore.QRect(10, 90, 371, 20))
        self.alert_label.setAlignment(QtCore.Qt.AlignCenter)
        self.alert_label.setObjectName("alert_label")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.func()



    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "iMP3rtor"))
        self.label.setText(_translate("MainWindow", "Path :"))
        self.ruRadio.setText(_translate("MainWindow", "RU"))
        self.enRadio.setText(_translate("MainWindow", "EN"))
        self.startButton.setText(_translate("MainWindow", "START"))
        self.fileButton.setText(_translate("MainWindow", "📁"))
        self.FAQButton.setText(_translate("MainWindow", "❓"))
        self.alert_label.setText(_translate("MainWindow", ""))

#Действия всех кнопок(элементов)

    def func(self):
        self.FAQButton.clicked.connect(lambda: self.FAQ())
        self.fileButton.clicked.connect(lambda: self.showDialog())
        self.ruRadio.clicked.connect(lambda: self.setLang("ru"))
        self.enRadio.clicked.connect(lambda: self.setLang("en"))
        self.startButton.clicked.connect(lambda: self.start_func())

#Открытие файлового менеджера для выбора файла

    def showDialog(self):
        fname = QFileDialog.getOpenFileName(None, 'Open file', '/home', 'PDF Files(*.pdf)')[0]
        self.path_line.setText(fname)

#Вывод инструкции

    def FAQ(self):
        self.alert_label.setText("PATH(📁) >> LANG(RU/EN) >> START")

#Выбор языка файла

    def setLang(self, text):
        main.language = text

#Функция старта обработки файла

    def start_func(self):
        self.alert_label.setText(print(main.convertation(main.f_path, main.language)))
        main.f_path = self.path_line.text()
        status_ok = main.convertation(main.f_path, main.language)
        self.alert_label.setText(status_ok)


#Запуск приложения

def application():
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())