# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'impact_table.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_dlgImpacts(object):
    def setupUi(self, dlgImp):
        dlgImp.setObjectName("dlgImp")
        dlgImp.resize(400, 300)
        self.tableimpacts = QtWidgets.QTableWidget(dlgImp)
        self.tableimpacts.setGeometry(QtCore.QRect(0, 0, 401, 301))
        self.tableimpacts.setAlternatingRowColors(True)
        self.tableimpacts.setObjectName("tableimpacts")
        self.tableimpacts.setColumnCount(3)
        self.tableimpacts.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableimpacts.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableimpacts.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableimpacts.setHorizontalHeaderItem(2, item)

        self.retranslateUi(dlgImp)
        QtCore.QMetaObject.connectSlotsByName(dlgImp)

    def retranslateUi(self, dlgImp):
        _translate = QtCore.QCoreApplication.translate
        dlgImp.setWindowTitle(_translate("dlgImp", "Impacts Tab"))
        item = self.tableimpacts.horizontalHeaderItem(0)
        item.setText(_translate("dlgImp", "Project"))
        item = self.tableimpacts.horizontalHeaderItem(1)
        item.setText(_translate("dlgImp", "Type"))
        item = self.tableimpacts.horizontalHeaderItem(2)
        item.setText(_translate("dlgImp", "Distance"))

