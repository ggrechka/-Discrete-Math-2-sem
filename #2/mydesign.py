# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Grechka\Desktop\Университет\itog.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(600, 800)
        MainWindow.setMinimumSize(QtCore.QSize(600, 800))
        MainWindow.setMaximumSize(QtCore.QSize(600, 800))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("favicon.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("\n"
"background-color: #171717;\n"
"")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(440, 130, 141, 41))
        font = QtGui.QFont()
        font.setFamily("Montserrat ExtraBold")
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("QPushButton{\n"
"color:#cccccc;\n"
"background-color: #9900ff ;\n"
"border:none;\n"
"}\n"
"QPushButton:Hover{\n"
"color:#9900ff;\n"
"background-color: #171717 ;\n"
"border:none;\n"
"}")
        self.pushButton.setObjectName("pushButton")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(140, 50, 350, 20))
        self.label_3.setMinimumSize(QtCore.QSize(350, 20))
        self.label_3.setMaximumSize(QtCore.QSize(350, 20))
        font = QtGui.QFont()
        font.setFamily("Montserrat ExtraBold")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color:rgb(204, 204, 204);")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(20, 100, 450, 20))
        self.label_4.setMinimumSize(QtCore.QSize(450, 20))
        self.label_4.setMaximumSize(QtCore.QSize(380, 20))
        font = QtGui.QFont()
        font.setFamily("Montserrat ExtraBold")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color:rgb(204, 204, 204);")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(20, 120, 340, 20))
        self.label_5.setMinimumSize(QtCore.QSize(340, 20))
        self.label_5.setMaximumSize(QtCore.QSize(295, 20))
        font = QtGui.QFont()
        font.setFamily("Montserrat ExtraBold")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color:rgb(204, 204, 204);")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(20, 140, 360, 20))
        self.label_6.setMinimumSize(QtCore.QSize(360, 20))
        self.label_6.setMaximumSize(QtCore.QSize(360, 20))
        font = QtGui.QFont()
        font.setFamily("Montserrat ExtraBold")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("color:rgb(204, 204, 204);")
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(20, 160, 305, 20))
        self.label_7.setMinimumSize(QtCore.QSize(305, 20))
        self.label_7.setMaximumSize(QtCore.QSize(305, 20))
        font = QtGui.QFont()
        font.setFamily("Montserrat ExtraBold")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("color:rgb(204, 204, 204);")
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(110, 210, 410, 20))
        self.label_8.setMinimumSize(QtCore.QSize(410, 20))
        self.label_8.setMaximumSize(QtCore.QSize(410, 20))
        font = QtGui.QFont()
        font.setFamily("Montserrat ExtraBold")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("color:rgb(204, 204, 204);")
        self.label_8.setObjectName("label_8")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(230, 260, 151, 41))
        font = QtGui.QFont()
        font.setFamily("Montserrat ExtraBold")
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("QPushButton{\n"
"color:#cccccc;\n"
"background-color: #9900ff ;\n"
"border:none;\n"
"}\n"
"QPushButton:Hover{\n"
"color:#9900ff;\n"
"background-color: #171717 ;\n"
"border:none;\n"
"}")
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(210, 10, 260, 20))
        self.label_9.setMinimumSize(QtCore.QSize(260, 20))
        self.label_9.setMaximumSize(QtCore.QSize(260, 20))
        font = QtGui.QFont()
        font.setFamily("Montserrat ExtraBold")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setStyleSheet("color:rgb(204, 204, 204);")
        self.label_9.setObjectName("label_9")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(180, 320, 241, 41))
        font = QtGui.QFont()
        font.setFamily("Montserrat ExtraBold")
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet("QPushButton{\n"
"color:#000000;\n"
"background-color: #cccccc ;\n"
"border:none;\n"
"}\n"
"QPushButton:Hover{\n"
"color:#9900ff;\n"
"background-color: #171717 ;\n"
"border:none;\n"
"}")
        self.pushButton_3.setObjectName("pushButton_3")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(0, 390, 600, 380))
        self.widget.setMinimumSize(QtCore.QSize(600, 380))
        self.widget.setMaximumSize(QtCore.QSize(600, 380))
        self.widget.setObjectName("widget")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Поиск Гамильтонового цикла"))
        self.pushButton.setText(_translate("MainWindow", "Выбрать файл"))
        self.label_3.setText(_translate("MainWindow", "Выберите файл с входными данными"))
        self.label_4.setText(_translate("MainWindow", "Первая строка должна содержать 2 значения через пробел: "))
        self.label_5.setText(_translate("MainWindow", "количество вершин N и количество ребёр M."))
        self.label_6.setText(_translate("MainWindow", "Следующие M-строк содержат описания рёбер - "))
        self.label_7.setText(_translate("MainWindow", "два числа (номера вершин) через пробел."))
        self.label_8.setText(_translate("MainWindow", "Выберите файл для записи выходных данных"))
        self.pushButton_2.setText(_translate("MainWindow", "Выбрать файл"))
        self.label_9.setText(_translate("MainWindow", "Здрасте, Сан Саныч♥"))
        self.pushButton_3.setText(_translate("MainWindow", "Найти Гамильтонов цикл"))
