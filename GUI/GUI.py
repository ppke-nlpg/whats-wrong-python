#!/usr/bin/env python3
# -*- coding: utf-8, vim: expandtab:ts=4 -*-

# Form implementation generated from reading ui file 'MainGUI_qtdraw.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8

    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)


class Ui_MainWindow:
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(800, 600)
        MainWindow.setSizeIncrement(QtCore.QSize(1, 1))
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.scrollArea_2 = QtGui.QScrollArea(self.centralwidget)
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollArea_2.setObjectName(_fromUtf8("scrollArea_2"))
        self.scrollAreaWidgetContents_2 = QtGui.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 774, 213))
        self.scrollAreaWidgetContents_2.setObjectName(_fromUtf8("scrollAreaWidgetContents_2"))
        self.gridLayout_2 = QtGui.QGridLayout(self.scrollAreaWidgetContents_2)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.graphicsView = QtGui.QGraphicsView(self.scrollAreaWidgetContents_2)
        self.graphicsView.setEnabled(True)
        self.graphicsView.setObjectName(_fromUtf8("graphicsView"))
        self.gridLayout_2.addWidget(self.graphicsView, 0, 0, 1, 1)
        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)
        self.verticalLayout.addWidget(self.scrollArea_2)
        self.scrollArea = QtGui.QScrollArea(self.centralwidget)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName(_fromUtf8("scrollArea"))
        self.scrollAreaWidgetContents = QtGui.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 774, 306))
        self.scrollAreaWidgetContents.setObjectName(_fromUtf8("scrollAreaWidgetContents"))
        self.gridLayout = QtGui.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setSizeConstraint(QtGui.QLayout.SetFixedSize)
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.verticalLayout_3 = QtGui.QVBoxLayout()
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.label_2 = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.verticalLayout_3.addWidget(self.label_2)
        self.ListViewSelectGuess = QtGui.QListWidget(self.scrollAreaWidgetContents)
        self.ListViewSelectGuess.setObjectName(_fromUtf8("ListViewSelectGuess"))
        self.verticalLayout_3.addWidget(self.ListViewSelectGuess)
        self.PushButtonAddGuess = QtGui.QPushButton(self.scrollAreaWidgetContents)
        self.PushButtonAddGuess.setObjectName(_fromUtf8("PushButtonAddGuess"))
        self.verticalLayout_3.addWidget(self.PushButtonAddGuess)
        self.horizontalLayout_4.addLayout(self.verticalLayout_3)
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.label = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout_2.addWidget(self.label)
        self.ListViewSelectGold = QtGui.QListWidget(self.scrollAreaWidgetContents)
        self.ListViewSelectGold.setProperty("isWrapping", False)
        self.ListViewSelectGold.setObjectName(_fromUtf8("ListViewSelectGold"))
        self.verticalLayout_2.addWidget(self.ListViewSelectGold)
        self.PushButtonAddGold = QtGui.QPushButton(self.scrollAreaWidgetContents)
        self.PushButtonAddGold.setObjectName(_fromUtf8("PushButtonAddGold"))
        self.verticalLayout_2.addWidget(self.PushButtonAddGold)
        self.horizontalLayout_4.addLayout(self.verticalLayout_2)
        self.gridLayout.addLayout(self.horizontalLayout_4, 3, 1, 1, 1)
        self.tabWidget = QtGui.QTabWidget(self.scrollAreaWidgetContents)
        self.tabWidget.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.tab)
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label_3 = QtGui.QLabel(self.tab)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.horizontalLayout.addWidget(self.label_3)
        self.horizontalSlider = QtGui.QSlider(self.tab)
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setObjectName(_fromUtf8("horizontalSlider"))
        self.horizontalLayout.addWidget(self.horizontalSlider)
        self.verticalLayout_4.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label_4 = QtGui.QLabel(self.tab)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.horizontalLayout_2.addWidget(self.label_4)
        self.horizontalSlider_2 = QtGui.QSlider(self.tab)
        self.horizontalSlider_2.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_2.setObjectName(_fromUtf8("horizontalSlider_2"))
        self.horizontalLayout_2.addWidget(self.horizontalSlider_2)
        self.verticalLayout_4.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.label_11 = QtGui.QLabel(self.tab)
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.horizontalLayout_3.addWidget(self.label_11)
        self.checkBox_2 = QtGui.QCheckBox(self.tab)
        self.checkBox_2.setObjectName(_fromUtf8("checkBox_2"))
        self.horizontalLayout_3.addWidget(self.checkBox_2)
        self.checkBox = QtGui.QCheckBox(self.tab)
        self.checkBox.setObjectName(_fromUtf8("checkBox"))
        self.horizontalLayout_3.addWidget(self.checkBox)
        self.verticalLayout_4.addLayout(self.horizontalLayout_3)
        self.tabWidget.addTab(self.tab, _fromUtf8(""))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.gridLayout_6 = QtGui.QGridLayout(self.tab_2)
        self.gridLayout_6.setObjectName(_fromUtf8("gridLayout_6"))
        self.label_5 = QtGui.QLabel(self.tab_2)
        self.label_5.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.label_5.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.gridLayout_6.addWidget(self.label_5, 0, 0, 1, 1)
        self.lineEdit = QtGui.QLineEdit(self.tab_2)
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.gridLayout_6.addWidget(self.lineEdit, 0, 1, 1, 1)
        self.label_6 = QtGui.QLabel(self.tab_2)
        self.label_6.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.label_6.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.gridLayout_6.addWidget(self.label_6, 1, 0, 1, 1)
        self.lineEdit_2 = QtGui.QLineEdit(self.tab_2)
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        self.gridLayout_6.addWidget(self.lineEdit_2, 1, 1, 1, 1)
        self.label_7 = QtGui.QLabel(self.tab_2)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.gridLayout_6.addWidget(self.label_7, 2, 0, 1, 1)
        self.checkBox_3 = QtGui.QCheckBox(self.tab_2)
        self.checkBox_3.setObjectName(_fromUtf8("checkBox_3"))
        self.gridLayout_6.addWidget(self.checkBox_3, 2, 1, 1, 1)
        self.checkBox_4 = QtGui.QCheckBox(self.tab_2)
        self.checkBox_4.setObjectName(_fromUtf8("checkBox_4"))
        self.gridLayout_6.addWidget(self.checkBox_4, 3, 1, 1, 1)
        self.checkBox_5 = QtGui.QCheckBox(self.tab_2)
        self.checkBox_5.setObjectName(_fromUtf8("checkBox_5"))
        self.gridLayout_6.addWidget(self.checkBox_5, 4, 1, 1, 1)
        self.tabWidget.addTab(self.tab_2, _fromUtf8(""))
        self.tab_3 = QtGui.QWidget()
        self.tab_3.setObjectName(_fromUtf8("tab_3"))
        self.gridLayout_3 = QtGui.QGridLayout(self.tab_3)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.label_8 = QtGui.QLabel(self.tab_3)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.gridLayout_3.addWidget(self.label_8, 0, 0, 1, 1)
        self.label_9 = QtGui.QLabel(self.tab_3)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.gridLayout_3.addWidget(self.label_9, 0, 1, 1, 1)
        self.listWidget = QtGui.QListWidget(self.tab_3)
        self.listWidget.setObjectName(_fromUtf8("listWidget"))
        self.gridLayout_3.addWidget(self.listWidget, 1, 0, 3, 1)
        self.lineEdit_3 = QtGui.QLineEdit(self.tab_3)
        self.lineEdit_3.setObjectName(_fromUtf8("lineEdit_3"))
        self.gridLayout_3.addWidget(self.lineEdit_3, 1, 1, 1, 1)
        self.label_10 = QtGui.QLabel(self.tab_3)
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.gridLayout_3.addWidget(self.label_10, 2, 1, 1, 1)
        self.checkBox_6 = QtGui.QCheckBox(self.tab_3)
        self.checkBox_6.setObjectName(_fromUtf8("checkBox_6"))
        self.gridLayout_3.addWidget(self.checkBox_6, 3, 1, 1, 1)
        self.tabWidget.addTab(self.tab_3, _fromUtf8(""))
        self.tab_4 = QtGui.QWidget()
        self.tab_4.setObjectName(_fromUtf8("tab_4"))
        self.gridLayout_5 = QtGui.QGridLayout(self.tab_4)
        self.gridLayout_5.setObjectName(_fromUtf8("gridLayout_5"))
        self.textBrowser = QtGui.QTextBrowser(self.tab_4)
        self.textBrowser.setObjectName(_fromUtf8("textBrowser"))
        self.gridLayout_5.addWidget(self.textBrowser, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab_4, _fromUtf8(""))
        self.tab_5 = QtGui.QWidget()
        self.tab_5.setObjectName(_fromUtf8("tab_5"))
        self.gridLayout_4 = QtGui.QGridLayout(self.tab_5)
        self.gridLayout_4.setObjectName(_fromUtf8("gridLayout_4"))
        self.lineEdit_4 = QtGui.QLineEdit(self.tab_5)
        self.lineEdit_4.setObjectName(_fromUtf8("lineEdit_4"))
        self.gridLayout_4.addWidget(self.lineEdit_4, 0, 0, 1, 1)
        self.pushButton = QtGui.QPushButton(self.tab_5)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.gridLayout_4.addWidget(self.pushButton, 0, 1, 1, 1)
        self.textBrowser_2 = QtGui.QTextBrowser(self.tab_5)
        self.textBrowser_2.setObjectName(_fromUtf8("textBrowser_2"))
        self.gridLayout_4.addWidget(self.textBrowser_2, 1, 0, 1, 2)
        self.tabWidget.addTab(self.tab_5, _fromUtf8(""))
        self.gridLayout.addWidget(self.tabWidget, 3, 0, 1, 1)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout.addWidget(self.scrollArea)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.actionImprt = QtGui.QAction(MainWindow)
        self.actionImprt.setObjectName(_fromUtf8("actionImprt"))
        self.actionAddGold = QtGui.QAction(MainWindow)
        self.actionAddGold.setCheckable(True)
        self.actionAddGold.setObjectName(_fromUtf8("actionAddGold"))
        self.menuFile.addAction(self.actionImprt)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.label_2.setText(_translate("MainWindow", "Select Guess", None))
        self.PushButtonAddGuess.setText(_translate("MainWindow", "Add", None))
        self.label.setText(_translate("MainWindow", "Select Gold", None))
        self.PushButtonAddGold.setText(_translate("MainWindow", "Add", None))
        self.label_3.setText(_translate("MainWindow", "Width:", None))
        self.label_4.setText(_translate("MainWindow", "Height:", None))
        self.label_11.setText(_translate("MainWindow", "Edges:", None))
        self.checkBox_2.setText(_translate("MainWindow", "Anitaliasing", None))
        self.checkBox.setText(_translate("MainWindow", "Curved", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Appearance", None))
        self.label_5.setText(_translate("MainWindow", "Label:", None))
        self.label_6.setText(_translate("MainWindow", "Token:", None))
        self.label_7.setText(_translate("MainWindow", "Options:", None))
        self.checkBox_3.setText(_translate("MainWindow", "Only Path", None))
        self.checkBox_4.setText(_translate("MainWindow", "Collaps", None))
        self.checkBox_5.setText(_translate("MainWindow", "Whole Words", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Edge Filter", None))
        self.label_8.setText(_translate("MainWindow", "Show Properties", None))
        self.label_9.setText(_translate("MainWindow", "Token:", None))
        self.label_10.setText(_translate("MainWindow", "Options:", None))
        self.checkBox_6.setText(_translate("MainWindow", "Whole Words", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "Token Filters", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("MainWindow", "Description", None))
        self.pushButton.setText(_translate("MainWindow", "Search", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), _translate("MainWindow", "Search Corpus", None))
        self.menuFile.setTitle(_translate("MainWindow", "File", None))
        self.actionImprt.setText(_translate("MainWindow", "Imprt", None))
        self.actionAddGold.setText(_translate("MainWindow", "AddGold", None))
        self.actionAddGold.setToolTip(_translate("MainWindow", "Add Gold File", None))
