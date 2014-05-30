# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'XSSAlert/ui/update.ui'
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

class Ui_Update_Dialog(object):
    def setupUi(self, Update_Dialog):
        Update_Dialog.setObjectName(_fromUtf8("Update_Dialog"))
        Update_Dialog.resize(371, 236)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/images/images/icon.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Update_Dialog.setWindowIcon(icon)
        Update_Dialog.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.India))
        self.verticalLayout_2 = QtGui.QVBoxLayout(Update_Dialog)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.version_label = QtGui.QLabel(Update_Dialog)
        self.version_label.setObjectName(_fromUtf8("version_label"))
        self.verticalLayout.addWidget(self.version_label)
        self.initial_progressBar = QtGui.QProgressBar(Update_Dialog)
        self.initial_progressBar.setProperty(_fromUtf8("value"), 0)
        self.initial_progressBar.setObjectName(_fromUtf8("initial_progressBar"))
        self.verticalLayout.addWidget(self.initial_progressBar)
        self.updatevectors = QtGui.QTextEdit(Update_Dialog)
        self.updatevectors.setStyleSheet(_fromUtf8("\n"
"color: rgb(255, 0, 0);\n"
"background-color: rgb(0, 0, 0);"))
        self.updatevectors.setReadOnly(True)
        self.updatevectors.setObjectName(_fromUtf8("updatevectors"))
        self.verticalLayout.addWidget(self.updatevectors)
        self.complete_bar = QtGui.QProgressBar(Update_Dialog)
        self.complete_bar.setProperty(_fromUtf8("value"), 0)
        self.complete_bar.setObjectName(_fromUtf8("complete_bar"))
        self.verticalLayout.addWidget(self.complete_bar)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.updateButton = QtGui.QPushButton(Update_Dialog)
        self.updateButton.setObjectName(_fromUtf8("updateButton"))
        self.horizontalLayout.addWidget(self.updateButton)
        self.checkButton = QtGui.QPushButton(Update_Dialog)
        self.checkButton.setObjectName(_fromUtf8("checkButton"))
        self.horizontalLayout.addWidget(self.checkButton)
        self.cancelButton = QtGui.QPushButton(Update_Dialog)
        self.cancelButton.setObjectName(_fromUtf8("cancelButton"))
        self.horizontalLayout.addWidget(self.cancelButton)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.retranslateUi(Update_Dialog)
        QtCore.QObject.connect(self.cancelButton, QtCore.SIGNAL(_fromUtf8("pressed()")), Update_Dialog.close)
        QtCore.QMetaObject.connectSlotsByName(Update_Dialog)

    def retranslateUi(self, Update_Dialog):
        Update_Dialog.setWindowTitle(QtGui.QApplication.translate("Update_Dialog", "Update", None, QtGui.QApplication.UnicodeUTF8))
        self.version_label.setText(QtGui.QApplication.translate("Update_Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt; font-weight:600;\">XSSAlert-1.0</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.updateButton.setText(QtGui.QApplication.translate("Update_Dialog", "Update", None, QtGui.QApplication.UnicodeUTF8))
        self.checkButton.setText(QtGui.QApplication.translate("Update_Dialog", "Check", None, QtGui.QApplication.UnicodeUTF8))
        self.cancelButton.setText(QtGui.QApplication.translate("Update_Dialog", "Cancel", None, QtGui.QApplication.UnicodeUTF8))

import xss_rc
