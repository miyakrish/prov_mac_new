# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'testFormMain.ui'
#
# Created: Tue May 22 15:08:26 2018
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1173, 558)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/favicon.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("background-color: rgb(170, 0, 0);")        
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.centralwidget.setStyleSheet("")
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setSpacing(2)
        self.horizontalLayout.setSizeConstraint(QtGui.QLayout.SetDefaultConstraint)
        self.horizontalLayout.setContentsMargins(2, 2, 2, 2)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.bookMarkCombo = QtGui.QComboBox(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.bookMarkCombo.sizePolicy().hasHeightForWidth())
        self.bookMarkCombo.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(10)
        font.setWeight(50)
        font.setItalic(False)
        font.setBold(False)
        self.bookMarkCombo.setFont(font)
        self.bookMarkCombo.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 10pt \"MS Shell Dlg 2\";\n"
"border-width: 2px;\n"
"border-radius: 10px;\n"
"\n"
"min-width: 15em;\n"
"padding: 10px;\n"
"border-color: rgb(170, 0, 0);\n"
"color: rgb(170, 0, 0);")
        self.bookMarkCombo.setEditable(True)
        #self.bookMarkCombo.setCurrentText("")
        self.bookMarkCombo.setFrame(True)
        self.bookMarkCombo.setObjectName("bookMarkCombo")
        self.horizontalLayout.addWidget(self.bookMarkCombo)
        self.label_provImage = QtGui.QLabel(self.centralwidget)
        self.label_provImage.setEnabled(True)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_provImage.sizePolicy().hasHeightForWidth())
        self.label_provImage.setSizePolicy(sizePolicy)
        #self.label_provImage.setMinimumSize(QtCore.QSize(100, 2000))
        self.label_provImage.setMaximumSize(QtCore.QSize(150, 3500))
        font = QtGui.QFont()
        self.label_provImage.setFont(font)
        self.label_provImage.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.label_provImage.setStyleSheet("")
        self.label_provImage.setText("")
        self.label_provImage.setPixmap(QtGui.QPixmap(":/icons/ProvLogoMain.png"))
        self.label_provImage.show()
        self.label_provImage.setAlignment(QtCore.Qt.AlignCenter)
        self.label_provImage.setWordWrap(True)
        self.label_provImage.setObjectName("label_provImage")
        self.label_provImage.setScaledContents(True)
        self.horizontalLayout.addWidget(self.label_provImage)
        self.Quit = QtGui.QPushButton(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Quit.sizePolicy().hasHeightForWidth())
        self.Quit.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setWeight(75)
        font.setBold(True)
        self.Quit.setFont(font)
        self.Quit.setStyleSheet("QPushButton#Quit {\n"
"background-color: rgb(141, 141, 141);\n"
"border-width: 2px;\n"
"border-radius: 10px;\n"
"border-color: #aa0000;\n"
"min-width: 8em;\n"
"padding: 4px;\n"
"color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton#Quit:pressed {\n"
"    background-color: rgb(224, 0, 0);    \n"
"    border-style: inset;\n"
"}\n"
"\n"
"")
        self.Quit.setObjectName("Quit")
        self.horizontalLayout.addWidget(self.Quit)
        self.horizontalLayout.setStretch(0, 4)
        self.horizontalLayout.setStretch(1, 2)
        self.horizontalLayout.setStretch(2, 1)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        self.tabWidget = QtGui.QTabWidget(self.centralwidget)
        self.tabWidget.setAutoFillBackground(False)
        self.tabWidget.setStyleSheet("QTabWidget  QTabBar::tab{\n"
"background-color: rgb(141, 141, 141);\n"
"border-width: 2px;\n"
"border-radius: 9px;\n"
"border-color: #aa0000;\n"
"min-width: 12em;\n"
"padding: 4px;\n"
"color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QTabWidget  QTabBar::tab:selected{\n"
"background-color: rgb(255, 255, 255);\n"
"font: 10pt \"MS Shell Dlg 2\";\n"
"color: rgb(170, 0, 0);\n"
"}\n"
"\n"
"")
        self.tabWidget.setElideMode(QtCore.Qt.ElideMiddle)
        self.tabWidget.setObjectName("tabWidget")
        self.test_console = QtGui.QWidget()
        self.test_console.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.test_console.setObjectName("test_console")
        self.tabWidget.addTab(self.test_console, "")
        self.search_option = QtGui.QWidget()
        self.search_option.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.search_option.setObjectName("search_option")
        self.formLayout = QtGui.QFormLayout(self.search_option)
        self.formLayout.setObjectName("formLayout")
        self.lineEdit = QtGui.QLineEdit(self.search_option)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit.sizePolicy().hasHeightForWidth())
        self.lineEdit.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setWeight(75)
        font.setItalic(True)
        font.setBold(True)
        self.lineEdit.setFont(font)
        self.lineEdit.setReadOnly(True)
        self.lineEdit.setObjectName("lineEdit")
        self.formLayout.setWidget(0, QtGui.QFormLayout.SpanningRole, self.lineEdit)
        self.tabWidget.addTab(self.search_option, "")
        self.gridLayout.addWidget(self.tabWidget, 1, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1173, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.bookMarkCombo.setCurrentIndex(-1)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QObject.connect(self.tabWidget, QtCore.SIGNAL("currentChanged(int)"), self.tabWidget.setCurrentIndex)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.Quit.setText(QtGui.QApplication.translate("MainWindow", "EXIT", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.test_console), QtGui.QApplication.translate("MainWindow", "Test Console", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEdit.setText(QtGui.QApplication.translate("MainWindow", "Look Here For Help", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.search_option), QtGui.QApplication.translate("MainWindow", "Search Option", None, QtGui.QApplication.UnicodeUTF8))

import icons_rc
