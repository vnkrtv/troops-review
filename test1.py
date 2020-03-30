# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'test.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import os


PROJECT_ROOT = os.path.dirname(__file__)
BACKGROUND_IMAGES_DIR = os.path.dirname(__file__) + '/data/images/background'


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1039, 757)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(0, 0, 2, 2))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.backgroundImage = QtWidgets.QLabel(self.centralwidget)
        self.backgroundImage.setGeometry(QtCore.QRect(10, 70, 781, 631))
        self.backgroundImage.setStyleSheet(".brd {\n"
"    border: 4px double black; /* Параметры границы */\n"
"    background: #fc3; /* Цвет фона */\n"
"    padding: 10px; /* Поля вокруг текста */\n"
"}\n"
"  ")
        self.backgroundImage.setText("")
        self.backgroundImage.setPixmap(QtGui.QPixmap("data/images/background/example.jpg"))
        self.backgroundImage.setScaledContents(True)
        self.backgroundImage.setObjectName("backgroundImage")
        self.backImageChangeButton = QtWidgets.QPushButton(self.centralwidget)
        self.backImageChangeButton.setGeometry(QtCore.QRect(820, 130, 181, 25))
        self.backImageChangeButton.setObjectName("backImageChangeButton")
        self.chooseBackgroundImageLabel = QtWidgets.QLabel(self.centralwidget)
        self.chooseBackgroundImageLabel.setGeometry(QtCore.QRect(820, 70, 191, 17))
        self.chooseBackgroundImageLabel.setObjectName("chooseBackgroundImageLabel")
        self.backImagecomboBox = QtWidgets.QComboBox(self.centralwidget)
        self.backImagecomboBox.setGeometry(QtCore.QRect(820, 100, 181, 25))
        self.backImagecomboBox.setObjectName("backImagecomboBox")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(820, 170, 181, 17))
        self.label.setObjectName("label")
        self.treeView = QtWidgets.QTreeView(self.centralwidget)
        self.treeView.setGeometry(QtCore.QRect(820, 190, 181, 192))
        self.treeView.setObjectName("treeView")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1039, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.backImageChangeButton.setText(_translate("MainWindow", "Поменять"))
        self.chooseBackgroundImageLabel.setText(_translate("MainWindow", "Выберете фоновую карту"))
        self.label.setText(_translate("MainWindow", "Добавить фоновую карту"))



class FileBrowser(QtWidgets.QMainWindow, Ui_MainWindow):

    def __init__(self):
        super(FileBrowser, self).__init__()
        self.setupUi(self)
        self.populate()

    def populate(self):
        path = PROJECT_ROOT
        model = QtWidgets.QFileSystemModel()
        model.setRootPath(QtCore.QDir.rootPath())
        self.treeView.setModel(model)
        self.treeView.setRootIndex(model.index(path))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
