# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'XSSAlert/ui/result_display.ui'
#
# Created: Mon May 23 17:31:14 2011
#      by: PyQt4 UI code generator 4.8.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_resultxss(object):
    def setupUi(self, resultxss):
        resultxss.setObjectName(_fromUtf8("resultxss"))
        resultxss.resize(508, 535)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/images/images/icon.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        resultxss.setWindowIcon(icon)
        resultxss.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.India))
        self.centralwidget = QtGui.QWidget(resultxss)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.outputxss = QtGui.QTableWidget(self.centralwidget)
        self.outputxss.setAutoFillBackground(True)
        self.outputxss.setStyleSheet(_fromUtf8("background-color: rgb(0, 0, 0);\n"
"color: rgb(255, 0, 0);"))
        self.outputxss.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.India))
        self.outputxss.setFrameShape(QtGui.QFrame.StyledPanel)
        self.outputxss.setFrameShadow(QtGui.QFrame.Sunken)
        self.outputxss.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.outputxss.setWordWrap(True)
        self.outputxss.setCornerButtonEnabled(False)
        self.outputxss.setObjectName(_fromUtf8("outputxss"))
        self.outputxss.setColumnCount(3)
        self.outputxss.setRowCount(1)
        item = QtGui.QTableWidgetItem()
        self.outputxss.setVerticalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.outputxss.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.outputxss.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.outputxss.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.outputxss.setItem(0, 0, item)
        self.outputxss.horizontalHeader().setVisible(True)
        self.outputxss.horizontalHeader().setCascadingSectionResizes(False)
        self.outputxss.horizontalHeader().setHighlightSections(True)
        self.outputxss.horizontalHeader().setStretchLastSection(True)
        self.outputxss.verticalHeader().setVisible(False)
        self.verticalLayout.addWidget(self.outputxss)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        spacerItem = QtGui.QSpacerItem(158, 28, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setStyleSheet(_fromUtf8("color: rgb(255, 0, 0);\n"
"background-color: rgb(0, 0, 0);\n"
"font: 75 14pt \"Bitstream Vera Sans Mono\";"))
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout.addWidget(self.label)
        spacerItem1 = QtGui.QSpacerItem(158, 28, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.gridLayout.addLayout(self.horizontalLayout, 1, 0, 1, 1)
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.outputsuccessfull_vectors = QtGui.QTableWidget(self.centralwidget)
        self.outputsuccessfull_vectors.setStyleSheet(_fromUtf8("background-color: rgb(0, 0, 0);\n"
"color: rgb(255, 0, 0);"))
        self.outputsuccessfull_vectors.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.India))
        self.outputsuccessfull_vectors.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.outputsuccessfull_vectors.setCornerButtonEnabled(False)
        self.outputsuccessfull_vectors.setObjectName(_fromUtf8("outputsuccessfull_vectors"))
        self.outputsuccessfull_vectors.setColumnCount(1)
        self.outputsuccessfull_vectors.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.outputsuccessfull_vectors.setHorizontalHeaderItem(0, item)
        self.outputsuccessfull_vectors.horizontalHeader().setSortIndicatorShown(True)
        self.outputsuccessfull_vectors.horizontalHeader().setStretchLastSection(True)
        self.outputsuccessfull_vectors.verticalHeader().setVisible(False)
        self.outputsuccessfull_vectors.verticalHeader().setHighlightSections(True)
        self.verticalLayout_2.addWidget(self.outputsuccessfull_vectors)
        self.gridLayout.addLayout(self.verticalLayout_2, 2, 0, 1, 1)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setStyleSheet(_fromUtf8("background-color: rgb(0, 0, 0);\n"
"font: 75 12pt \"Bitstream Vera Sans Mono\";\n"
"color: rgb(255, 0, 0);"))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout_3.addWidget(self.label_2)
        self.total_vectors = QtGui.QLabel(self.centralwidget)
        self.total_vectors.setStyleSheet(_fromUtf8("font: 75 14pt \"Bitstream Vera Sans Mono\";\n"
"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);\n"
""))
        self.total_vectors.setObjectName(_fromUtf8("total_vectors"))
        self.horizontalLayout_3.addWidget(self.total_vectors)
        spacerItem2 = QtGui.QSpacerItem(0, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem2)
        self.label_6 = QtGui.QLabel(self.centralwidget)
        self.label_6.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.label_6.setStyleSheet(_fromUtf8("background-color: rgb(0, 0, 0);\n"
"font: 75 12pt \"Bitstream Vera Sans Mono\";\n"
"color: rgb(255, 0, 0);"))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.horizontalLayout_3.addWidget(self.label_6)
        self.total_time = QtGui.QLabel(self.centralwidget)
        self.total_time.setStyleSheet(_fromUtf8("font: 75 14pt \"Bitstream Vera Sans Mono\";\n"
"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);\n"
""))
        self.total_time.setObjectName(_fromUtf8("total_time"))
        self.horizontalLayout_3.addWidget(self.total_time)
        self.gridLayout.addLayout(self.horizontalLayout_3, 3, 0, 1, 1)
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.label_8 = QtGui.QLabel(self.centralwidget)
        self.label_8.setStyleSheet(_fromUtf8("background-color: rgb(0, 0, 0);\n"
"font: 75 12pt \"Bitstream Vera Sans Mono\";\n"
"color: rgb(255, 0, 0);"))
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.horizontalLayout_5.addWidget(self.label_8)
        self.successfull_vectors = QtGui.QLabel(self.centralwidget)
        self.successfull_vectors.setStyleSheet(_fromUtf8("font: 75 14pt \"Bitstream Vera Sans Mono\";\n"
"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);\n"
""))
        self.successfull_vectors.setObjectName(_fromUtf8("successfull_vectors"))
        self.horizontalLayout_5.addWidget(self.successfull_vectors)
        spacerItem3 = QtGui.QSpacerItem(0, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem3)
        self.label_10 = QtGui.QLabel(self.centralwidget)
        self.label_10.setStyleSheet(_fromUtf8("background-color: rgb(0, 0, 0);\n"
"font: 75 12pt \"Bitstream Vera Sans Mono\";\n"
"color: rgb(255, 0, 0);"))
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.horizontalLayout_5.addWidget(self.label_10)
        self.failed_vectors = QtGui.QLabel(self.centralwidget)
        self.failed_vectors.setStyleSheet(_fromUtf8("font: 75 14pt \"Bitstream Vera Sans Mono\";\n"
"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);\n"
""))
        self.failed_vectors.setObjectName(_fromUtf8("failed_vectors"))
        self.horizontalLayout_5.addWidget(self.failed_vectors)
        self.gridLayout.addLayout(self.horizontalLayout_5, 4, 0, 1, 1)
        self.resultprogressbar = QtGui.QProgressBar(self.centralwidget)
        self.resultprogressbar.setProperty(_fromUtf8("value"), 0)
        self.resultprogressbar.setObjectName(_fromUtf8("resultprogressbar"))
        self.gridLayout.addWidget(self.resultprogressbar, 5, 0, 1, 1)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        spacerItem4 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem4)
        self.start_button = QtGui.QPushButton(self.centralwidget)
        self.start_button.setStyleSheet(_fromUtf8("\n"
"font: 14pt \"Abyssinica SIL\";\n"
""))
        self.start_button.setObjectName(_fromUtf8("start_button"))
        self.horizontalLayout_2.addWidget(self.start_button)
        spacerItem5 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem5)
        self.quit_button = QtGui.QPushButton(self.centralwidget)
        self.quit_button.setStyleSheet(_fromUtf8("\n"
"font: 14pt \"Abyssinica SIL\";\n"
""))
        self.quit_button.setObjectName(_fromUtf8("quit_button"))
        self.horizontalLayout_2.addWidget(self.quit_button)
        spacerItem6 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem6)
        self.BrowserButton = QtGui.QPushButton(self.centralwidget)
        self.BrowserButton.setStyleSheet(_fromUtf8("\n"
"font: 14pt \"Abyssinica SIL\";\n"
""))
        self.BrowserButton.setObjectName(_fromUtf8("BrowserButton"))
        self.horizontalLayout_2.addWidget(self.BrowserButton)
        spacerItem7 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem7)
        self.gridLayout.addLayout(self.horizontalLayout_2, 6, 0, 1, 1)
        resultxss.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(resultxss)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 508, 27))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        resultxss.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(resultxss)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        resultxss.setStatusBar(self.statusbar)

        self.retranslateUi(resultxss)
        QtCore.QObject.connect(self.quit_button, QtCore.SIGNAL(_fromUtf8("pressed()")), resultxss.close)
        QtCore.QMetaObject.connectSlotsByName(resultxss)

    def retranslateUi(self, resultxss):
        resultxss.setWindowTitle(QtGui.QApplication.translate("resultxss", "Result", None, QtGui.QApplication.UnicodeUTF8))
        self.outputxss.setSortingEnabled(True)
        self.outputxss.verticalHeaderItem(0).setText(QtGui.QApplication.translate("resultxss", "New Row", None, QtGui.QApplication.UnicodeUTF8))
        self.outputxss.horizontalHeaderItem(0).setText(QtGui.QApplication.translate("resultxss", "URL", None, QtGui.QApplication.UnicodeUTF8))
        self.outputxss.horizontalHeaderItem(1).setText(QtGui.QApplication.translate("resultxss", "HTTP-Code", None, QtGui.QApplication.UnicodeUTF8))
        self.outputxss.horizontalHeaderItem(2).setText(QtGui.QApplication.translate("resultxss", "Result", None, QtGui.QApplication.UnicodeUTF8))
        __sortingEnabled = self.outputxss.isSortingEnabled()
        self.outputxss.setSortingEnabled(False)
        self.outputxss.setSortingEnabled(__sortingEnabled)
        self.label.setText(QtGui.QApplication.translate("resultxss", "Possible XSS Injections", None, QtGui.QApplication.UnicodeUTF8))
        self.outputsuccessfull_vectors.horizontalHeaderItem(0).setText(QtGui.QApplication.translate("resultxss", "URL", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("resultxss", " Total Attack Vectors   ", None, QtGui.QApplication.UnicodeUTF8))
        self.total_vectors.setText(QtGui.QApplication.translate("resultxss", "00", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("resultxss", "      Total Time  ", None, QtGui.QApplication.UnicodeUTF8))
        self.total_time.setText(QtGui.QApplication.translate("resultxss", "00", None, QtGui.QApplication.UnicodeUTF8))
        self.label_8.setText(QtGui.QApplication.translate("resultxss", " Successful Vectors     ", None, QtGui.QApplication.UnicodeUTF8))
        self.successfull_vectors.setText(QtGui.QApplication.translate("resultxss", "00", None, QtGui.QApplication.UnicodeUTF8))
        self.label_10.setText(QtGui.QApplication.translate("resultxss", " Failed Vectors   ", None, QtGui.QApplication.UnicodeUTF8))
        self.failed_vectors.setText(QtGui.QApplication.translate("resultxss", "00", None, QtGui.QApplication.UnicodeUTF8))
        self.start_button.setText(QtGui.QApplication.translate("resultxss", "Start", None, QtGui.QApplication.UnicodeUTF8))
        self.quit_button.setText(QtGui.QApplication.translate("resultxss", "Quit", None, QtGui.QApplication.UnicodeUTF8))
        self.BrowserButton.setText(QtGui.QApplication.translate("resultxss", "Open Results In Browser", None, QtGui.QApplication.UnicodeUTF8))

import xss_rc
