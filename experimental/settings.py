# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'settings.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import Color

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(641, 291)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        Dialog.setMinimumSize(QtCore.QSize(641, 291))
        Dialog.setMaximumSize(QtCore.QSize(641, 456))
        self.gridLayout = QtWidgets.QGridLayout(Dialog)
        self.gridLayout.setObjectName("gridLayout")

        self.scene_prev = QtWidgets.QGraphicsScene()
        self.scene_prev.setBackgroundBrush(QtGui.QColor(100,100,100))
        self.scene_prev.addText("Preview").setDefaultTextColor(QtCore.Qt.white)

        self.preview = QtWidgets.QGraphicsView(self.scene_prev, Dialog)
        self.preview.setObjectName("preview")
        self.gridLayout.addWidget(self.preview, 0, 0, 1, 1)
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")

        #Labels
        self.L = QtWidgets.QLabel(Dialog)
        self.L.setObjectName("L")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.L)
        self.A = QtWidgets.QLabel(Dialog)
        self.A.setObjectName("A")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.A)
        self.B = QtWidgets.QLabel(Dialog)
        self.B.setObjectName("B")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.B)
        self.C = QtWidgets.QLabel(Dialog)
        self.C.setObjectName("C")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.C)
        self.H = QtWidgets.QLabel(Dialog)
        self.H.setObjectName("H")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.H)

        #Values shown
        self.Lshow = QtWidgets.QLineEdit(Dialog)
        self.Lshow.setObjectName("Lshow")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.Lshow)

        self.Ashow = QtWidgets.QLineEdit(Dialog)
        self.Ashow.setObjectName("Ashow")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.Ashow)

        self.Bshow = QtWidgets.QLineEdit(Dialog)
        self.Bshow.setObjectName("Bshow")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.Bshow)

        self.Cshow = QtWidgets.QLineEdit(Dialog)
        self.Cshow.setObjectName("Cshow")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.Cshow)

        self.Hshow = QtWidgets.QLineEdit(Dialog)
        self.Hshow.setObjectName("Hshow")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.Hshow)
        self.gridLayout.addLayout(self.formLayout, 0, 1, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")

        self.Lshow.setAlignment(QtCore.Qt.AlignRight)
        self.Ashow.setAlignment(QtCore.Qt.AlignRight)
        self.Bshow.setAlignment(QtCore.Qt.AlignRight)
        self.Cshow.setAlignment(QtCore.Qt.AlignRight)
        self.Hshow.setAlignment(QtCore.Qt.AlignRight)

        self.Cshow.setReadOnly(True)
        self.Hshow.setReadOnly(True)

        self.Lshow.setValidator(QtGui.QDoubleValidator(0.0000, 100.0000, 4))
        self.Ashow.setValidator(QtGui.QDoubleValidator(-128.0000, 128.0000, 4))
        self.Bshow.setValidator(QtGui.QDoubleValidator(-128.0000, 128.0000, 4))


        #Buttons
        self.view = QtWidgets.QPushButton(Dialog)
        self.view.setObjectName("view")
        self.horizontalLayout.addWidget(self.view)

        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel | QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.horizontalLayout.addWidget(self.buttonBox)
        self.gridLayout.addLayout(self.horizontalLayout, 1, 0, 1, 2)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        self.color = Color.Color()

        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        self.view.clicked.connect(self.show_color)
        #self.buttonBox.accepted.connect(self.update_color)
        self.buttonBox.rejected.connect(self.reset_color)

    def update_L (self):
        L = self.Lshow.text()
        if L == '':
            self.color.L = 0.0
        else:
            self.color.L = float(L)

    def update_a (self):
        a = self.Ashow.text()
        if a == '':
            self.color.a = 0.0
        else:
            self.color.a = float(a)

    def update_b (self):
        b = self.Bshow.text()
        if b == '':
            self.color.b = 0.0
        else:
            self.color.b = float(b)

    def update_c (self):
        self.color.calc_c()
        self.Cshow.setText(str(format(self.color.c, '.4f')))

    def update_h (self):
        self.color.calc_h()
        self.Hshow.setText(str(format(self.color.h, '.4f')))

    def update_color (self):
        self.update_L()
        self.update_a()
        self.update_b()
        self.update_c()
        self.update_h()

    def show_color (self):
        self.update_color()
        R,G,B = self.color.Lab2rgb()
        self.scene_prev.setBackgroundBrush(QtGui.QColor(R, G, B))

    def reset_color (self):
        self.color.__init__()

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.L.setText(_translate("Dialog", "L*"))
        self.A.setText(_translate("Dialog", "A*"))
        self.B.setText(_translate("Dialog", "B*"))
        self.C.setText(_translate("Dialog", "C*"))
        self.H.setText(_translate("Dialog", "H*"))
        self.view.setText(_translate("Dialog", "View color"))


if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    app.exec_()
    sys.exit(app.exec_())

