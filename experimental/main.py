# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui_test.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import helper as hp
import os
#import numpy as np
#import pyqtgraph as pg
import settings
import colorDiff
from Color import *
from colour import SpectralDistribution

global data, specs, ill

data = None
specs = 0
ill = 'A'

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(868, 570)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(868, 570))
        MainWindow.setMaximumSize(QtCore.QSize(868, 570))

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(9, 43, 154, 478))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")

        #Images
        self.scene_sample = QtWidgets.QGraphicsScene(self.centralwidget)
        self.scene_sample.setBackgroundBrush(QtGui.QColor(200,200,200))
        self.sample = QtWidgets.QGraphicsView(self.scene_sample, self.verticalLayoutWidget)
        self.sample.setObjectName("sample")
        self.verticalLayout.addWidget(self.sample)

        self.scene_master = QtWidgets.QGraphicsScene(self.centralwidget)
        self.scene_master.setBackgroundBrush(QtGui.QColor(200,200,200))
        self.master = QtWidgets.QGraphicsView(self.scene_master, self.verticalLayoutWidget)
        self.master.setObjectName("master")
        self.verticalLayout.addWidget(self.master)

        self.scene_sample.addText("Sample").setDefaultTextColor(QtCore.Qt.white)
        self.scene_master.addText("Master").setDefaultTextColor(QtCore.Qt.white)


        #Combo Box
        self.illuminants_list = QtWidgets.QComboBox(self.centralwidget)
        self.illuminants_list.setGeometry(QtCore.QRect(9, 10, 151, 25))
        self.illuminants_list.setObjectName("illuminants_list")
        self.illuminants_list.addItem("")
        self.illuminants_list.addItem("")
        self.illuminants_list.addItem("")
        self.illuminants_list.addItem("")
        self.illuminants_list.addItem("")
        self.illuminants_list.addItem("")
        self.illuminants_list.addItem("")
        self.illuminants_list.addItem("")
        self.illuminants_list.addItem("")
        self.illuminants_list.addItem("")
        self.illuminants_list.addItem("")
        self.illuminants_list.addItem("")

        #Main Image
        self.scene = QtWidgets.QGraphicsScene()
        self.scene.setBackgroundBrush(QtGui.QColor(100,100,100))
        self.image = QtWidgets.QGraphicsView(self.scene, self.centralwidget)
        self.image.setGeometry(QtCore.QRect(169, 9, 512, 512))
        self.image.setMinimumSize(QtCore.QSize(515, 515))
        self.image.setMaximumSize(QtCore.QSize(515, 515))
        self.image.setObjectName("image")
        self.image.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.CrossCursor))
        self.image.setMouseTracking(True)

        #Events
        self.image.mousePressEvent = self.mousePressEvent
        self.image.mouseMoveEvent = self.mouseMoveEvent


        #Slider
        self.slider = QtWidgets.QSlider(self.centralwidget)
        self.slider.setGeometry(QtCore.QRect(10, 530, 851, 17))
        self.slider.setOrientation(QtCore.Qt.Horizontal)
        self.slider.setObjectName("horizontalSlider")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(690, 120, 171, 171))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")

        self.slider.setMaximum(203) # adjusted for IQ camera

        #Parameters
        self.Bshow = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.Bshow.setObjectName("Bshow")
        self.gridLayout.addWidget(self.Bshow, 2, 1, 1, 1)
        self.Ashow = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.Ashow.setObjectName("Ashow")
        self.gridLayout.addWidget(self.Ashow, 1, 1, 1, 1)
        self.Lshow = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.Lshow.setObjectName("Lshow")
        self.gridLayout.addWidget(self.Lshow, 0, 1, 1, 1)
        self.Hshow = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.Hshow.setObjectName("textEdit_5")
        self.gridLayout.addWidget(self.Hshow, 4, 1, 1, 1)
        self.Cshow = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.Cshow.setObjectName("textEdit_4")
        self.gridLayout.addWidget(self.Cshow, 3, 1, 1, 1)
        self.H = QtWidgets.QLabel(self.gridLayoutWidget)
        self.H.setObjectName("H")
        self.gridLayout.addWidget(self.H, 4, 0, 1, 1)
        self.C = QtWidgets.QLabel(self.gridLayoutWidget)
        self.C.setObjectName("C")
        self.gridLayout.addWidget(self.C, 3, 0, 1, 1)
        self.B = QtWidgets.QLabel(self.gridLayoutWidget)
        self.B.setObjectName("B")
        self.gridLayout.addWidget(self.B, 2, 0, 1, 1)
        self.A = QtWidgets.QLabel(self.gridLayoutWidget)
        self.A.setObjectName("A")
        self.gridLayout.addWidget(self.A, 1, 0, 1, 1)
        self.L = QtWidgets.QLabel(self.gridLayoutWidget)
        self.L.setObjectName("L")
        self.gridLayout.addWidget(self.L, 0, 0, 1, 1)
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(690, 310, 171, 206))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")

        self.Lshow.setAlignment(QtCore.Qt.AlignRight)
        self.Ashow.setAlignment(QtCore.Qt.AlignRight)
        self.Bshow.setAlignment(QtCore.Qt.AlignRight)
        self.Cshow.setAlignment(QtCore.Qt.AlignRight)
        self.Hshow.setAlignment(QtCore.Qt.AlignRight)
        self.Lshow.setReadOnly(True)
        self.Ashow.setReadOnly(True)
        self.Bshow.setReadOnly(True)
        self.Cshow.setReadOnly(True)
        self.Hshow.setReadOnly(True)


        #Buttons
        self.load = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.load.setObjectName("load")
        self.verticalLayout_2.addWidget(self.load)

        self.settings = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.settings.setObjectName("settings")
        self.verticalLayout_2.addWidget(self.settings)

        self.calc = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.calc.setObjectName("calc")
        self.verticalLayout_2.addWidget(self.calc)

        self.diff = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.diff.setObjectName("diff")
        self.verticalLayout_2.addWidget(self.diff)

        self.plot = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.plot.setObjectName("plot")
        self.verticalLayout_2.addWidget(self.plot)

        self.save = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.save.setObjectName("save colors")
        self.verticalLayout_2.addWidget(self.save)

        self.export = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.export.setObjectName("export")
        self.verticalLayout_2.addWidget(self.export)

        self.clear = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.clear.setObjectName("clear")
        self.verticalLayout_2.addWidget(self.clear)

        #Labels
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(690, 100, 71, 17))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(700, 10, 151, 71))
        self.label_2.setText("")
        dirname = os.path.dirname(__file__)
        self.label_2.setPixmap(QtGui.QPixmap(os.path.join(dirname, 'resources/ISent-logo-CMYK-color.png')))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        MainWindow.setCentralWidget(self.centralwidget)

        #Status Bar
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.directory = None

        self.sampleColor = Color()
        self.masterColor = Color()

        #self.graph_plot = pg.plot(title='Sample spectra')
        #self.graph_plot.addLegend()

        # set properties
        #self.graph_plot.setLabel('left', 'R')
        #self.graph_plot.setLabel('bottom', 'Wavelength', units='nm')
        #self.graph_plot.setXRange(400, 1000)

        self.x = 256
        self.y = 256

        #Buttons state
        self.setButtons()

        # Signals/Slots
        # for buttons
        self.load.clicked.connect(self.on_load_clicked)
        self.calc.clicked.connect(self.on_calc_clicked)
        self.plot.clicked.connect(self.on_plot_clicked)
        self.settings.clicked.connect(self.on_settings_clicked)
        self.diff.clicked.connect(self.on_diff_clicked)
        self.save.clicked.connect(self.on_save_clicked)
        self.clear.clicked.connect(self.on_clear_clicked)
        self.export.clicked.connect(self.on_export_clicked)

        #for ComboBox
        self.illuminants_list.currentIndexChanged.connect(self.illuminant)

        #for slider
        self.slider.sliderReleased.connect(self.show_band)

        #self.winPlot = pg.GraphicsWindow()  # Automatically generates grids with multiple items


    #EVENT HANDLERS
    def mouseMoveEvent (self, event):
        if self.calc.isEnabled():
            self.statusbar.showMessage("Mouse coords: (%d : %d)" % (event.x(),event.y()))
        else:
            event.accept()

    def mousePressEvent (self, event):
        if self.calc.isEnabled():
            self.x = event.x()
            self.y = event.y()
            self.statusbar.showMessage('coords: (%d : %d)' % (self.x,self.y))
            r = QtCore.QRectF(QtCore.QPointF(self.x - 25.0, self.y - 25.0), QtCore.QSizeF(50.0, 50.0))
            pix = QtGui.QPixmap.fromImage(self.image)
            p = QtGui.QPainter()
            p.begin(pix)
            p.setPen(QtGui.QPen(QtCore.Qt.lightGray, 5, QtCore.Qt.SolidLine))
            p.drawRect(r)
            self.scene.addPixmap(pix)
            p.end()
            #self.scene.addItem(QtWidgets.QGraphicsRectItem(r))
        else:
            event.accept()

    #AUX FUNC
    def setButtons (self):
        global data
        self.export.setEnabled(False)

        if data is not None:
            self.calc.setEnabled(True)
            self.plot.setEnabled(True)
            self.slider.setEnabled(True)
            self.clear.setEnabled(True)
        else:
            self.calc.setEnabled(False)
            self.plot.setEnabled(False)
            self.slider.setEnabled(False)
            self.clear.setEnabled(False)

        if self.sampleColor.L == 0 and self.sampleColor.a == 0 and self.sampleColor.b == 0:
            self.diff.setEnabled(False)
        else:
            self.diff.setEnabled(True)

        if self.masterColor.L == 0 and self.masterColor.a == 0 and self.masterColor.b == 0:
            self.save.setEnabled(False)
        else:
            if self.diff.isEnabled():
                self.save.setEnabled(True)
            else:self.save.setEnabled(False)

    #SLOTS
    def on_load_clicked (self):
        #Opens File
        self.statusbar.showMessage('Loading...')
        global data
        f = QtWidgets.QFileDialog()
        filename, _ = f.getOpenFileName(None, 'Open file', '', 'Raw files (*.raw *.hdr)')
        if hp.isEmpty(filename):
            pass
        else:
            self.directory = hp.Dir(filename)
            data = hp.read_data(filename)
            print("File loaded: ", filename)
            self.setButtons()
            self.statusbar.showMessage('Data Loaded')

            self.show_band()

    def on_calc_clicked (self):
        global data,ill

        col, row, bands = data.shape
        #Pre-processing
        #blurred = hp.blur_img(data,7)

        #SPD creation
        cdo = np.linspace(400,1000,bands).tolist()
        mn = hp.mean(self.x, self.y, data)
        px = mn.tolist() # before was: blurred[self.x, self.y] instead of mn
        spd = createSPD(cdo, px)

        #sd1 = colour.SpectralDistribution(dict(zip(cdo,px)))
        #plot_spec(sd1)

        XYZ = color_perception(spd,'CIE 2012 10 Degree Standard Observer',ill)
        LAB = xyz2lab(XYZ)

        self.sampleColor.L = float(LAB[0])
        self.sampleColor.a = float(LAB[1])
        self.sampleColor.b = float(LAB[2])
        self.sampleColor.calc_c()
        self.sampleColor.calc_h()

        R, G, B = xyz2rgb(XYZ)

        self.sampleColor.R = R
        self.sampleColor.G = G
        self.sampleColor.B = B

        self.scene_sample.setBackgroundBrush(QtGui.QColor(R, G, B))

        self.Lshow.setText(format(self.sampleColor.L, '.4f'))
        self.Ashow.setText(format(self.sampleColor.a, '.4f'))
        self.Bshow.setText(format(self.sampleColor.b, '.4f'))
        self.Cshow.setText(format(self.sampleColor.c, '.4f'))
        self.Hshow.setText(format(self.sampleColor.h, '.4f'))
        self.setButtons()

        self.statusbar.showMessage('Calculation finished')

    def on_plot_clicked (self):
        global data, specs
        self.statusbar.showMessage('Plotting')

        #plotting
        #blurred = hp.blur_img(data,7)

        mn = hp.mean(self.x, self.y, data)#blurred)

        cdo = np.linspace(400,1000,data.shape[2])
        px = mn #blurred[self.x, self.y]

        #spd = createSPD(cdo, px)

        spd = SpectralDistribution(dict(zip(cdo, px)))
        plot_spec(spd)

        #self.graph_plot.plot(wv,px,pen=(specs,100))

        #specs = specs + 1


    def on_settings_clicked (self):
        self.statusbar.showMessage('Settings')
        Dialog = QtWidgets.QDialog()
        ui = settings.Ui_Dialog()
        ui.setupUi(Dialog)
        Dialog.show()
        Dialog.exec_()
        #showuing color
        self.masterColor = ui.color
        R, G, B = self.masterColor.Lab2rgb()
        self.scene_master.setBackgroundBrush(QtGui.QColor(R,G,B))
        self.setButtons()
        #self.m_color = ui.color

    def on_diff_clicked (self):
        Lab1 = np.array([self.masterColor.L, self.masterColor.a, self.masterColor.b])
        Lab2 = np.array([self.sampleColor.L, self.sampleColor.a, self.sampleColor.b])
        Dialog = QtWidgets.QDialog()
        ui = colorDiff.Ui_Dialog()
        ui.setupUi(Dialog)
        ui.diffs.dE = calc_dE(Lab1,Lab2)
        ui.diffs.dL = float(self.sampleColor.L - self.masterColor.L)
        print(self.sampleColor.b)
        print(self.masterColor.b)
        ui.diffs.da = float(self.sampleColor.a - self.masterColor.a)
        ui.diffs.db = float(self.sampleColor.b - self.masterColor.b)
        ui.diffs.dc = float(self.sampleColor.c - self.masterColor.c)
        ui.diffs.dh = float(self.sampleColor.h - self.masterColor.h)
        ui.show_vals()
        Dialog.show()
        Dialog.exec_()

    def on_save_clicked (self):
        f = QtWidgets.QFileDialog()
        filename, _ = f.getSaveFileName(None, 'Save as... File', self.directory,
                                                    filter='PNG Files(*.png);; JPG Files(*.jpg)')
        Rm, Gm, Bm = self.masterColor.Lab2rgb()
        Rs, Gs, Bs = self.sampleColor.Lab2rgb()

        hp.save_colors((Bm, Gm, Rm), (Bs, Gs, Rs), filename)

    def on_export_clicked (self):
        pass

    def on_clear_clicked (self):
        global data
        data = hp.clear_data()
        self.scene_master.setBackgroundBrush(QtGui.QColor(200,200,200))
        self.scene_sample.setBackgroundBrush(QtGui.QColor(200,200,200))
        self.scene.clear()
        self.sampleColor.__init__()
        self.masterColor.__init__()
        self.x = 256
        self.y = 256
        self.Lshow.setText(format(self.sampleColor.L, '.4f'))
        self.Ashow.setText(format(self.sampleColor.a, '.4f'))
        self.Bshow.setText(format(self.sampleColor.b, '.4f'))
        self.Cshow.setText(format(self.sampleColor.c, '.4f'))
        self.Hshow.setText(format(self.sampleColor.h, '.4f'))
        self.setButtons()
        self.statusbar.showMessage('Data Cleared')

    def illuminant (self):
        global ill
        self.statusbar.showMessage('Current illuminant: %s' % self.illuminants_list.currentText())
        ill = self.illuminants_list.currentText()

    def show_band (self):
        global data

        band = self.slider.value()
        wv = format((band*600/203)+400, '.2f')
        self.statusbar.showMessage('Band: %f nm' % float(wv))

        col,row,bands = data.shape

        print(data.shape)
        band_img = data[:,:,band]

        self.image = self.data2img(band_img, row, col)
        self.scene.addPixmap(QtGui.QPixmap.fromImage(self.image))

    def data2img(self, img, row, col):
        return QtGui.QImage(hp.uint8_img(img).data, col,row,col,QtGui.QImage.Format_Indexed8)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "ISent ColorCheck v1.0"))
        self.illuminants_list.setItemText(0, _translate("MainWindow", "A"))
        self.illuminants_list.setItemText(1, _translate("MainWindow", "D50"))
        self.illuminants_list.setItemText(2, _translate("MainWindow", "D55"))
        self.illuminants_list.setItemText(3, _translate("MainWindow", "D65"))
        self.illuminants_list.setItemText(4, _translate("MainWindow", "D75"))
        self.illuminants_list.setItemText(5, _translate("MainWindow", "FL1"))
        self.illuminants_list.setItemText(6, _translate("MainWindow", "FL2"))
        self.illuminants_list.setItemText(7, _translate("MainWindow", "FL3"))
        self.illuminants_list.setItemText(8, _translate("MainWindow", "FL7"))
        self.illuminants_list.setItemText(9, _translate("MainWindow", "FL11"))
        self.illuminants_list.setItemText(10, _translate("MainWindow", "HP1"))
        self.illuminants_list.setItemText(11, _translate("MainWindow", "HP2"))
        self.H.setText(_translate("MainWindow", "H*"))
        self.C.setText(_translate("MainWindow", "C*"))
        self.B.setText(_translate("MainWindow", "B*"))
        self.A.setText(_translate("MainWindow", "A*"))
        self.L.setText(_translate("MainWindow", "L*"))
        self.load.setText(_translate("MainWindow", "Load data"))
        self.calc.setText(_translate("MainWindow", "Calculate color"))
        self.plot.setText(_translate("MainWindow", "Plot spectrum"))
        self.settings.setText(_translate("MainWindow", "Settings"))
        self.save.setText(_translate("MainWindow","Save Colors"))
        self.export.setText(_translate("MainWindow", "export to excel"))
        self.diff.setText(_translate("MainWindow", "Color difference"))
        self.clear.setText(_translate("MainWindow", "Clear data"))
        self.label.setText(_translate("MainWindow", "Parameters"))

if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    app.setStyle("Fusion")
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    app.exec_()
