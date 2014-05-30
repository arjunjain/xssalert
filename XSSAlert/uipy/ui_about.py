# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'XSSAlert/ui/about.ui'
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

class Ui_XSSAlert_about(object):
    def setupUi(self, XSSAlert_about):
        XSSAlert_about.setObjectName(_fromUtf8("XSSAlert_about"))
        XSSAlert_about.resize(388, 275)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/images/images/xssalert.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        XSSAlert_about.setWindowIcon(icon)
        XSSAlert_about.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.India))
        self.verticalLayout = QtGui.QVBoxLayout(XSSAlert_about)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.tabWidget = QtGui.QTabWidget(XSSAlert_about)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.about_tab = QtGui.QWidget()
        self.about_tab.setObjectName(_fromUtf8("about_tab"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.about_tab)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.label_2 = QtGui.QLabel(self.about_tab)
        self.label_2.setText(_fromUtf8(""))
        self.label_2.setPixmap(QtGui.QPixmap(_fromUtf8(":/images/images/xssalert.png")))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout_3.addWidget(self.label_2)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        spacerItem2 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem2)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        spacerItem3 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem3)
        self.label = QtGui.QLabel(self.about_tab)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout.addWidget(self.label)
        spacerItem4 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem4)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        spacerItem5 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem5)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        spacerItem6 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem6)
        self.verticalLayout_3 = QtGui.QVBoxLayout()
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.label_3 = QtGui.QLabel(self.about_tab)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.verticalLayout_3.addWidget(self.label_3)
        self.label_4 = QtGui.QLabel(self.about_tab)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.verticalLayout_3.addWidget(self.label_4)
        spacerItem7 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem7)
        self.horizontalLayout_4.addLayout(self.verticalLayout_3)
        spacerItem8 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem8)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.tabWidget.addTab(self.about_tab, _fromUtf8(""))
        self.License_tab = QtGui.QWidget()
        self.License_tab.setObjectName(_fromUtf8("License_tab"))
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.License_tab)
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.textBrowser_2 = QtGui.QTextBrowser(self.License_tab)
        self.textBrowser_2.setOpenExternalLinks(True)
        self.textBrowser_2.setObjectName(_fromUtf8("textBrowser_2"))
        self.verticalLayout_4.addWidget(self.textBrowser_2)
        self.tabWidget.addTab(self.License_tab, _fromUtf8(""))
        self.Credits_tab = QtGui.QWidget()
        self.Credits_tab.setObjectName(_fromUtf8("Credits_tab"))
        self.verticalLayout_5 = QtGui.QVBoxLayout(self.Credits_tab)
        self.verticalLayout_5.setObjectName(_fromUtf8("verticalLayout_5"))
        self.textBrowser = QtGui.QTextBrowser(self.Credits_tab)
        self.textBrowser.setOpenExternalLinks(True)
        self.textBrowser.setObjectName(_fromUtf8("textBrowser"))
        self.verticalLayout_5.addWidget(self.textBrowser)
        self.tabWidget.addTab(self.Credits_tab, _fromUtf8(""))
        self.verticalLayout.addWidget(self.tabWidget)
        spacerItem9 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem9)
        spacerItem10 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem10)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        spacerItem11 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem11)
        self.close_button = QtGui.QPushButton(XSSAlert_about)
        self.close_button.setObjectName(_fromUtf8("close_button"))
        self.horizontalLayout_2.addWidget(self.close_button)
        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.retranslateUi(XSSAlert_about)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QObject.connect(self.close_button, QtCore.SIGNAL(_fromUtf8("clicked()")), XSSAlert_about.close)
        QtCore.QMetaObject.connectSlotsByName(XSSAlert_about)

    def retranslateUi(self, XSSAlert_about):
        XSSAlert_about.setWindowTitle(QtGui.QApplication.translate("XSSAlert_about", "XSSAlert : About", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("XSSAlert_about", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt; font-weight:600; color:#000000;\">XSSAlert 1.0</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("XSSAlert_about", "Penetration Testing tool for Detecting Cross Side", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("XSSAlert_about", "Scripting attack holes present in web application", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.about_tab), QtGui.QApplication.translate("XSSAlert_about", "About", None, QtGui.QApplication.UnicodeUTF8))
        self.textBrowser_2.setHtml(QtGui.QApplication.translate("XSSAlert_about", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">XSSAlert is free software; you can redistribute it and/or modify it under the terms of the GNU General Public License as published bythe Free Software Foundation; either version 3 of the License, or (at your option) any later version.</p>\n"
"<p align=\"justify\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">XSSAlert is distributed in the hope that it will be useful , but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License  (<a href=\"http://www.gnu.org/licenses/gpl-3.0.txt\"><span style=\" text-decoration: underline; color:#0000ff;\">http://www.gnu.org/licenses/gpl-3.0.txt</span></a>)for more details.</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.License_tab), QtGui.QApplication.translate("XSSAlert_about", "License", None, QtGui.QApplication.UnicodeUTF8))
        self.textBrowser.setHtml(QtGui.QApplication.translate("XSSAlert_about", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Written by :</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Arjun Jain &lt; <a href=\"mailto:arjunjain08@gmail.com\"><span style=\" text-decoration: underline; color:#0000ff;\">arjunjain08@gmail.com </span></a>&gt;</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Credits_tab), QtGui.QApplication.translate("XSSAlert_about", "Credits", None, QtGui.QApplication.UnicodeUTF8))
        self.close_button.setText(QtGui.QApplication.translate("XSSAlert_about", "Close", None, QtGui.QApplication.UnicodeUTF8))

import xss_rc
import xss_rc
