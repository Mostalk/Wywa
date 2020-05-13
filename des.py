# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.setEnabled(True)
        Form.resize(255, 130)
        self.folder = QtWidgets.QPushButton(Form)
        self.folder.setGeometry(QtCore.QRect(40, 10, 191, 31))
        self.folder.setObjectName("folder")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(40, 50, 71, 21))
        self.label.setObjectName("label")
        self.start = QtWidgets.QPushButton(Form)
        self.start.setEnabled(False)
        self.start.setGeometry(QtCore.QRect(40, 80, 191, 31))
        self.start.setMouseTracking(False)
        self.start.setAcceptDrops(False)
        self.start.setAutoFillBackground(False)
        self.start.setInputMethodHints(QtCore.Qt.ImhNone)
        self.start.setCheckable(False)
        self.start.setChecked(False)
        self.start.setAutoRepeat(False)
        self.start.setAutoExclusive(False)
        self.start.setAutoDefault(False)
        self.start.setDefault(False)
        self.start.setFlat(False)
        self.start.setObjectName("start")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(130, 50, 101, 21))
        self.label_2.setObjectName("label_2")
        self.len = QtWidgets.QLabel(Form)
        self.len.setGeometry(QtCore.QRect(108, 50, 21, 21))
        self.len.setAlignment(QtCore.Qt.AlignCenter)
        self.len.setObjectName("len")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.folder.setText(_translate("Form", "Выбрать папку"))
        self.label.setText(_translate("Form", "Найдено:"))
        self.start.setText(_translate("Form", "Начать распознование"))
        self.label_2.setText(_translate("Form", "изображений"))
        self.len.setText(_translate("Form", "0"))
