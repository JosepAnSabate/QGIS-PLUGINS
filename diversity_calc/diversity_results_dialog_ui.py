# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'diversity_results_dialog_ui.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(487, 480)
        self.verticalLayoutWidget = QtWidgets.QWidget(Dialog)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 0, 481, 471))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.lytMain = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.lytMain.setContentsMargins(0, 0, 0, 0)
        self.lytMain.setObjectName("lytMain")
        self.trwResult = QtWidgets.QTreeWidget(self.verticalLayoutWidget)
        self.trwResult.setAlternatingRowColors(True)
        self.trwResult.setObjectName("trwResult")
        self.lytMain.addWidget(self.trwResult)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Diversity Results"))
        self.trwResult.headerItem().setText(0, _translate("Dialog", "Name"))
        self.trwResult.headerItem().setText(1, _translate("Dialog", "Count"))
        self.trwResult.headerItem().setText(2, _translate("Dialog", "Richness"))
        self.trwResult.headerItem().setText(3, _translate("Dialog", "Evenness"))
        self.trwResult.headerItem().setText(4, _translate("Dialog", "Simpsons"))

