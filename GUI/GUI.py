# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainGUI.ui'
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

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(767, 628)
        MainWindow.setMinimumSize(QtCore.QSize(767, 628))
        MainWindow.setSizeIncrement(QtCore.QSize(1, 1))
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout_8 = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout_8.setObjectName(_fromUtf8("gridLayout_8"))
        self.scrollArea_2 = QtGui.QScrollArea(self.centralwidget)
        self.scrollArea_2.setMinimumSize(QtCore.QSize(0, 225))
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollArea_2.setObjectName(_fromUtf8("scrollArea_2"))
        self.scrollAreaWidgetContents_2 = QtGui.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 741, 223))
        self.scrollAreaWidgetContents_2.setObjectName(_fromUtf8("scrollAreaWidgetContents_2"))
        self.gridLayout_2 = QtGui.QGridLayout(self.scrollAreaWidgetContents_2)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))

        self.graphicsView = QtGui.QGraphicsView(self.scrollAreaWidgetContents_2)
        self.graphicsView.setEnabled(True)
        self.graphicsView.setObjectName(_fromUtf8("graphicsView"))
        self.gridLayout_2.addWidget(self.graphicsView, 0, 0, 1, 1)

        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)
        self.gridLayout_8.addWidget(self.scrollArea_2, 0, 0, 1, 1)
        self.scrollArea = QtGui.QScrollArea(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollArea.sizePolicy().hasHeightForWidth())
        self.scrollArea.setSizePolicy(sizePolicy)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName(_fromUtf8("scrollArea"))
        self.scrollAreaWidgetContents = QtGui.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 741, 294))
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
        self.selectGuessListWidget = QtGui.QListWidget(self.scrollAreaWidgetContents)
        self.selectGuessListWidget.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.selectGuessListWidget.setObjectName(_fromUtf8("selectGuessListWidget"))
        self.verticalLayout_3.addWidget(self.selectGuessListWidget)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.addGuessPushButton = QtGui.QPushButton(self.scrollAreaWidgetContents)
        self.addGuessPushButton.setObjectName(_fromUtf8("addGuessPushButton"))
        self.horizontalLayout.addWidget(self.addGuessPushButton)
        self.removeGuessPushButton = QtGui.QPushButton(self.scrollAreaWidgetContents)
        self.removeGuessPushButton.setObjectName(_fromUtf8("removeGuessPushButton"))
        self.horizontalLayout.addWidget(self.removeGuessPushButton)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.horizontalLayout_4.addLayout(self.verticalLayout_3)
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.label = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout_2.addWidget(self.label)
        self.selectGoldListWidget = QtGui.QListWidget(self.scrollAreaWidgetContents)
        self.selectGoldListWidget.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.selectGoldListWidget.setProperty("isWrapping", False)
        self.selectGoldListWidget.setObjectName(_fromUtf8("selectGoldListWidget"))
        self.verticalLayout_2.addWidget(self.selectGoldListWidget)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.pushButtonAddGold = QtGui.QPushButton(self.scrollAreaWidgetContents)
        self.pushButtonAddGold.setObjectName(_fromUtf8("pushButtonAddGold"))
        self.horizontalLayout_2.addWidget(self.pushButtonAddGold)
        self.removeGoldPushButton = QtGui.QPushButton(self.scrollAreaWidgetContents)
        self.removeGoldPushButton.setObjectName(_fromUtf8("removeGoldPushButton"))
        self.horizontalLayout_2.addWidget(self.removeGoldPushButton)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_4.addLayout(self.verticalLayout_2)
        self.gridLayout.addLayout(self.horizontalLayout_4, 3, 1, 1, 1)
        self.searchCorpusTab = QtGui.QTabWidget(self.scrollAreaWidgetContents)
        self.searchCorpusTab.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.searchCorpusTab.setObjectName(_fromUtf8("searchCorpusTab"))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.gridLayout_6 = QtGui.QGridLayout(self.tab_2)
        self.gridLayout_6.setObjectName(_fromUtf8("gridLayout_6"))
        self.collapsCheckBox = QtGui.QCheckBox(self.tab_2)
        self.collapsCheckBox.setObjectName(_fromUtf8("collapsCheckBox"))
        self.gridLayout_6.addWidget(self.collapsCheckBox, 12, 1, 1, 1)
        self.EdgeLabelLabel = QtGui.QLabel(self.tab_2)
        self.EdgeLabelLabel.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.EdgeLabelLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.EdgeLabelLabel.setObjectName(_fromUtf8("EdgeLabelLabel"))
        self.gridLayout_6.addWidget(self.EdgeLabelLabel, 8, 0, 1, 1)
        self.onlyPathCheckBox = QtGui.QCheckBox(self.tab_2)
        self.onlyPathCheckBox.setObjectName(_fromUtf8("onlyPathCheckBox"))
        self.gridLayout_6.addWidget(self.onlyPathCheckBox, 11, 1, 1, 1)
        self.EdgeFilterTokenLabel = QtGui.QLabel(self.tab_2)
        self.EdgeFilterTokenLabel.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.EdgeFilterTokenLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.EdgeFilterTokenLabel.setObjectName(_fromUtf8("EdgeFilterTokenLabel"))
        self.gridLayout_6.addWidget(self.EdgeFilterTokenLabel, 10, 0, 1, 1)
        self.edgeFilterTokenLineEdit = QtGui.QLineEdit(self.tab_2)
        self.edgeFilterTokenLineEdit.setObjectName(_fromUtf8("edgeFilterTokenLineEdit"))
        self.gridLayout_6.addWidget(self.edgeFilterTokenLineEdit, 10, 1, 1, 1)
        self.edgeFilterWholeWordsCheckBox = QtGui.QCheckBox(self.tab_2)
        self.edgeFilterWholeWordsCheckBox.setObjectName(_fromUtf8("edgeFilterWholeWordsCheckBox"))
        self.gridLayout_6.addWidget(self.edgeFilterWholeWordsCheckBox, 13, 1, 1, 1)
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.edgeTypeListWidget = QtGui.QListWidget(self.tab_2)
        self.edgeTypeListWidget.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.edgeTypeListWidget.setObjectName(_fromUtf8("edgeTypeListWidget"))
        self.horizontalLayout_5.addWidget(self.edgeTypeListWidget)
        self.verticalLayout_5 = QtGui.QVBoxLayout()
        self.verticalLayout_5.setSizeConstraint(QtGui.QLayout.SetDefaultConstraint)
        self.verticalLayout_5.setObjectName(_fromUtf8("verticalLayout_5"))
        self.matchesCheckBox = QtGui.QCheckBox(self.tab_2)
        self.matchesCheckBox.setObjectName(_fromUtf8("matchesCheckBox"))
        self.verticalLayout_5.addWidget(self.matchesCheckBox)
        self.falsePositiveCheckBox = QtGui.QCheckBox(self.tab_2)
        self.falsePositiveCheckBox.setObjectName(_fromUtf8("falsePositiveCheckBox"))
        self.verticalLayout_5.addWidget(self.falsePositiveCheckBox)
        self.falseNegativeCheckBox = QtGui.QCheckBox(self.tab_2)
        self.falseNegativeCheckBox.setObjectName(_fromUtf8("falseNegativeCheckBox"))
        self.verticalLayout_5.addWidget(self.falseNegativeCheckBox)
        self.horizontalLayout_5.addLayout(self.verticalLayout_5)
        self.gridLayout_6.addLayout(self.horizontalLayout_5, 1, 0, 1, 2)
        self.EdgeFilterOptionsLabel = QtGui.QLabel(self.tab_2)
        self.EdgeFilterOptionsLabel.setObjectName(_fromUtf8("EdgeFilterOptionsLabel"))
        self.gridLayout_6.addWidget(self.EdgeFilterOptionsLabel, 11, 0, 1, 1)
        self.labelLineEdit = QtGui.QLineEdit(self.tab_2)
        self.labelLineEdit.setObjectName(_fromUtf8("labelLineEdit"))
        self.gridLayout_6.addWidget(self.labelLineEdit, 8, 1, 1, 1)
        self.searchCorpusTab.addTab(self.tab_2, _fromUtf8(""))
        self.tab_3 = QtGui.QWidget()
        self.tab_3.setObjectName(_fromUtf8("tab_3"))
        self.gridLayout_3 = QtGui.QGridLayout(self.tab_3)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.tokenFilterWholeWordsCheckBox = QtGui.QCheckBox(self.tab_3)
        self.tokenFilterWholeWordsCheckBox.setObjectName(_fromUtf8("tokenFilterWholeWordsCheckBox"))
        self.gridLayout_3.addWidget(self.tokenFilterWholeWordsCheckBox, 4, 1, 1, 1)
        self.TokenFilterOptionsLabel = QtGui.QLabel(self.tab_3)
        self.TokenFilterOptionsLabel.setObjectName(_fromUtf8("TokenFilterOptionsLabel"))
        self.gridLayout_3.addWidget(self.TokenFilterOptionsLabel, 3, 1, 1, 1)
        self.tokenTypesListWidget = QtGui.QListWidget(self.tab_3)
        self.tokenTypesListWidget.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.tokenTypesListWidget.setObjectName(_fromUtf8("tokenTypesListWidget"))
        self.gridLayout_3.addWidget(self.tokenTypesListWidget, 1, 0, 6, 1)
        self.ShowPropertiesLabel = QtGui.QLabel(self.tab_3)
        self.ShowPropertiesLabel.setObjectName(_fromUtf8("ShowPropertiesLabel"))
        self.gridLayout_3.addWidget(self.ShowPropertiesLabel, 0, 0, 1, 1)
        self.TokenFiltersTokenLabel = QtGui.QLabel(self.tab_3)
        self.TokenFiltersTokenLabel.setObjectName(_fromUtf8("TokenFiltersTokenLabel"))
        self.gridLayout_3.addWidget(self.TokenFiltersTokenLabel, 0, 1, 1, 1)
        self.tokenFilterTokenLineEdit = QtGui.QLineEdit(self.tab_3)
        self.tokenFilterTokenLineEdit.setObjectName(_fromUtf8("tokenFilterTokenLineEdit"))
        self.gridLayout_3.addWidget(self.tokenFilterTokenLineEdit, 1, 1, 1, 1)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_3.addItem(spacerItem, 2, 1, 1, 1)
        self.searchCorpusTab.addTab(self.tab_3, _fromUtf8(""))
        self.tab_5 = QtGui.QWidget()
        self.tab_5.setObjectName(_fromUtf8("tab_5"))
        self.gridLayout_4 = QtGui.QGridLayout(self.tab_5)
        self.gridLayout_4.setObjectName(_fromUtf8("gridLayout_4"))
        self.searchCorpusLineEdit = QtGui.QLineEdit(self.tab_5)
        self.searchCorpusLineEdit.setObjectName(_fromUtf8("searchCorpusLineEdit"))
        self.gridLayout_4.addWidget(self.searchCorpusLineEdit, 0, 0, 1, 1)
        self.searchButton = QtGui.QPushButton(self.tab_5)
        self.searchButton.setObjectName(_fromUtf8("searchButton"))
        self.gridLayout_4.addWidget(self.searchButton, 0, 1, 1, 1)
        self.searchResultLisWidget = QtGui.QListWidget(self.tab_5)
        self.searchResultLisWidget.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.searchResultLisWidget.setObjectName(_fromUtf8("searchResultLisWidget"))
        self.gridLayout_4.addWidget(self.searchResultLisWidget, 1, 0, 1, 2)
        self.searchCorpusTab.addTab(self.tab_5, _fromUtf8(""))
        self.gridLayout.addWidget(self.searchCorpusTab, 3, 0, 1, 1)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout_8.addWidget(self.scrollArea, 6, 0, 1, 1)
        self.horizontalLayout_10 = QtGui.QHBoxLayout()
        self.horizontalLayout_10.setSizeConstraint(QtGui.QLayout.SetMinimumSize)
        self.horizontalLayout_10.setContentsMargins(-1, 0, 0, -1)
        self.horizontalLayout_10.setObjectName(_fromUtf8("horizontalLayout_10"))
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_10.addItem(spacerItem1)
        self.spinBox = QtGui.QSpinBox(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.spinBox.sizePolicy().hasHeightForWidth())
        self.spinBox.setSizePolicy(sizePolicy)
        self.spinBox.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.spinBox.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.spinBox.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.spinBox.setObjectName(_fromUtf8("spinBox"))
        self.horizontalLayout_10.addWidget(self.spinBox)
        self.SpinBoxLabel = QtGui.QLabel(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.SpinBoxLabel.sizePolicy().hasHeightForWidth())
        self.SpinBoxLabel.setSizePolicy(sizePolicy)
        self.SpinBoxLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.SpinBoxLabel.setIndent(-1)
        self.SpinBoxLabel.setObjectName(_fromUtf8("SpinBoxLabel"))
        self.horizontalLayout_10.addWidget(self.SpinBoxLabel)
        self.gridLayout_8.addLayout(self.horizontalLayout_10, 5, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 767, 22))
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
        self.actionExport = QtGui.QAction(MainWindow)
        self.actionExport.setObjectName(_fromUtf8("actionExport"))
        self.menuFile.addAction(self.actionExport)
        self.menubar.addAction(self.menuFile.menuAction())
        self.SpinBoxLabel.setBuddy(self.spinBox)

        self.retranslateUi(MainWindow)
        self.searchCorpusTab.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.label_2.setText(_translate("MainWindow", "Select Guess", None))
        self.addGuessPushButton.setText(_translate("MainWindow", "Add", None))
        self.removeGuessPushButton.setText(_translate("MainWindow", "Remove", None))
        self.label.setText(_translate("MainWindow", "Select Gold", None))
        self.pushButtonAddGold.setText(_translate("MainWindow", "Add", None))
        self.removeGoldPushButton.setText(_translate("MainWindow", "Remove", None))
        self.collapsCheckBox.setText(_translate("MainWindow", "Collaps", None))
        self.EdgeLabelLabel.setText(_translate("MainWindow", "Label:", None))
        self.onlyPathCheckBox.setText(_translate("MainWindow", "Only Path", None))
        self.EdgeFilterTokenLabel.setText(_translate("MainWindow", "Token:", None))
        self.edgeFilterWholeWordsCheckBox.setText(_translate("MainWindow", "Whole Words", None))
        self.matchesCheckBox.setText(_translate("MainWindow", "Matches", None))
        self.falsePositiveCheckBox.setText(_translate("MainWindow", "False Positive", None))
        self.falseNegativeCheckBox.setText(_translate("MainWindow", "False Negative", None))
        self.EdgeFilterOptionsLabel.setText(_translate("MainWindow", "Options:", None))
        self.searchCorpusTab.setTabText(self.searchCorpusTab.indexOf(self.tab_2), _translate("MainWindow", "Edge Filter", None))
        self.tokenFilterWholeWordsCheckBox.setText(_translate("MainWindow", "Whole Words", None))
        self.TokenFilterOptionsLabel.setText(_translate("MainWindow", "Options:", None))
        self.ShowPropertiesLabel.setText(_translate("MainWindow", "Show Properties", None))
        self.TokenFiltersTokenLabel.setText(_translate("MainWindow", "Token:", None))
        self.searchCorpusTab.setTabText(self.searchCorpusTab.indexOf(self.tab_3), _translate("MainWindow", "Token Filters", None))
        self.searchButton.setText(_translate("MainWindow", "Search", None))
        self.searchCorpusTab.setTabText(self.searchCorpusTab.indexOf(self.tab_5), _translate("MainWindow", "Search Corpus", None))
        self.SpinBoxLabel.setText(_translate("MainWindow", "of 0", None))
        self.menuFile.setTitle(_translate("MainWindow", "File", None))
        self.actionImprt.setText(_translate("MainWindow", "Imprt", None))
        self.actionAddGold.setText(_translate("MainWindow", "AddGold", None))
        self.actionAddGold.setToolTip(_translate("MainWindow", "Add Gold File", None))
        self.actionExport.setText(_translate("MainWindow", "Export", None))

