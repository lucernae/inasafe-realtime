# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'minimum_needs_base.ui'
#
# Created: Sun Jan 20 16:24:49 2013
#      by: PyQt4 UI code generator 4.9.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_MinimumNeedsBase(object):
    def setupUi(self, MinimumNeedsBase):
        MinimumNeedsBase.setObjectName(_fromUtf8("MinimumNeedsBase"))
        MinimumNeedsBase.resize(400, 302)
        self.gridLayout = QtGui.QGridLayout(MinimumNeedsBase)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label_2 = QtGui.QLabel(MinimumNeedsBase)
        self.label_2.setWordWrap(True)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label = QtGui.QLabel(MinimumNeedsBase)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout.addWidget(self.label)
        self.cboPolygonLayers = QtGui.QComboBox(MinimumNeedsBase)
        self.cboPolygonLayers.setObjectName(_fromUtf8("cboPolygonLayers"))
        self.horizontalLayout.addWidget(self.cboPolygonLayers)
        self.gridLayout.addLayout(self.horizontalLayout, 1, 0, 1, 1)
        self.buttonBox = QtGui.QDialogButtonBox(MinimumNeedsBase)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.gridLayout.addWidget(self.buttonBox, 2, 0, 1, 1)

        self.retranslateUi(MinimumNeedsBase)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), MinimumNeedsBase.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), MinimumNeedsBase.reject)
        QtCore.QMetaObject.connectSlotsByName(MinimumNeedsBase)

    def retranslateUi(self, MinimumNeedsBase):
        MinimumNeedsBase.setWindowTitle(QtGui.QApplication.translate("MinimumNeedsBase", "Dialog", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("MinimumNeedsBase", "Select a layer that is already loaded in QGIS and that contains a field named \'pengungsi\'.", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("MinimumNeedsBase", "Affected People Layer", None, QtGui.QApplication.UnicodeUTF8))

