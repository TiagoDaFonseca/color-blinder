# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'colorDiff.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from Color import Diff

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(647, 116)
        self.gridLayout = QtWidgets.QGridLayout(Dialog)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2, 0, QtCore.Qt.AlignHCenter)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label, 0, QtCore.Qt.AlignHCenter)
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_2.addWidget(self.label_3, 0, QtCore.Qt.AlignHCenter)
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_2.addWidget(self.label_4, 0, QtCore.Qt.AlignHCenter)
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_2.addWidget(self.label_5, 0, QtCore.Qt.AlignHCenter)
        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_2.addWidget(self.label_6, 0, QtCore.Qt.AlignHCenter)
        self.gridLayout.addLayout(self.horizontalLayout_2, 0, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.dE = QtWidgets.QLineEdit(Dialog)
        self.dE.setObjectName("dE")
        self.horizontalLayout.addWidget(self.dE)
        self.dL = QtWidgets.QLineEdit(Dialog)
        self.dL.setObjectName("dL")
        self.horizontalLayout.addWidget(self.dL)
        self.dA = QtWidgets.QLineEdit(Dialog)
        self.dA.setObjectName("dA")
        self.horizontalLayout.addWidget(self.dA)
        self.dB = QtWidgets.QLineEdit(Dialog)
        self.dB.setObjectName("dB")
        self.horizontalLayout.addWidget(self.dB)
        self.dC = QtWidgets.QLineEdit(Dialog)
        self.dC.setObjectName("dC")
        self.horizontalLayout.addWidget(self.dC)
        self.dH = QtWidgets.QLineEdit(Dialog)
        self.dH.setObjectName("dH")
        self.horizontalLayout.addWidget(self.dH)
        self.gridLayout.addLayout(self.horizontalLayout, 1, 0, 1, 1)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout.addWidget(self.buttonBox, 2, 0, 1, 1)

        self.diffs = Diff()

        self.dE.setAlignment(QtCore.Qt.AlignCenter)
        self.dL.setAlignment(QtCore.Qt.AlignCenter)
        self.dA.setAlignment(QtCore.Qt.AlignCenter)
        self.dB.setAlignment(QtCore.Qt.AlignCenter)
        self.dC.setAlignment(QtCore.Qt.AlignCenter)
        self.dH.setAlignment(QtCore.Qt.AlignCenter)

        self.dE.setReadOnly(True)
        self.dA.setReadOnly(True)
        self.dB.setReadOnly(True)
        self.dC.setReadOnly(True)
        self.dH.setReadOnly(True)

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def show_vals(self):
        # dE
        self.dE.setText(str(format(self.diffs.dE, '.4f')))
        # dL
        self.dL.setText(str(format(self.diffs.dL, '.4f')))
        # dC
        self.dC.setText(str(format(self.diffs.dc, '.4f')))
        # dh
        self.dH.setText(str(format(self.diffs.dh, '.4f')))
        # da
        self.dA.setText(str(format(self.diffs.da, '.4f')))
        # db
        self.dB.setText(str(format(self.diffs.db, '.4f')))

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Color Differences"))
        self.label_2.setText(_translate("Dialog", "dE*"))
        self.label.setText(_translate("Dialog", "dL*"))
        self.label_3.setText(_translate("Dialog", "dA*"))
        self.label_4.setText(_translate("Dialog", "dB*"))
        self.label_5.setText(_translate("Dialog", "dC*"))
        self.label_6.setText(_translate("Dialog", "dH*"))



