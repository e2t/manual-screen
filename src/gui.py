# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui.ui'
#
# Created by: PyQt5 UI code generator 5.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(536, 185)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(Dialog)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.edt_width = QtWidgets.QLineEdit(Dialog)
        self.edt_width.setObjectName("edt_width")
        self.gridLayout.addWidget(self.edt_width, 0, 1, 1, 1)
        self.edt_length = QtWidgets.QLineEdit(Dialog)
        self.edt_length.setObjectName("edt_length")
        self.gridLayout.addWidget(self.edt_length, 1, 1, 1, 1)
        self.edt_gap = QtWidgets.QLineEdit(Dialog)
        self.edt_gap.setObjectName("edt_gap")
        self.gridLayout.addWidget(self.edt_gap, 2, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.btn_run = QtWidgets.QPushButton(Dialog)
        self.btn_run.setObjectName("btn_run")
        self.horizontalLayout.addWidget(self.btn_run)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2.addLayout(self.verticalLayout)
        self.txt_result = QtWidgets.QPlainTextEdit(Dialog)
        self.txt_result.setObjectName("txt_result")
        self.horizontalLayout_2.addWidget(self.txt_result)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_2.setText(_translate("Dialog", "Общая длина решетки, мм"))
        self.label_3.setText(_translate("Dialog", "Прозор, мм"))
        self.label.setText(_translate("Dialog", "Ширина решетки в канале, мм"))
        self.btn_run.setText(_translate("Dialog", "Расчет"))

