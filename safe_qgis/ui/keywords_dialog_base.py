# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'keywords_dialog_base.ui'
#
# Created: Thu Feb 20 13:24:44 2014
#      by: PyQt4 UI code generator 4.9.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_KeywordsDialogBase(object):
    def setupUi(self, KeywordsDialogBase):
        KeywordsDialogBase.setObjectName(_fromUtf8("KeywordsDialogBase"))
        KeywordsDialogBase.resize(597, 865)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(KeywordsDialogBase.sizePolicy().hasHeightForWidth())
        KeywordsDialogBase.setSizePolicy(sizePolicy)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/plugins/inasafe/icon.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        KeywordsDialogBase.setWindowIcon(icon)
        self.verticalLayout = QtGui.QVBoxLayout(KeywordsDialogBase)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.lblLayerName = QtGui.QLabel(KeywordsDialogBase)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lblLayerName.sizePolicy().hasHeightForWidth())
        self.lblLayerName.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.lblLayerName.setFont(font)
        self.lblLayerName.setText(_fromUtf8(""))
        self.lblLayerName.setWordWrap(True)
        self.lblLayerName.setObjectName(_fromUtf8("lblLayerName"))
        self.verticalLayout.addWidget(self.lblLayerName)
        self.grpSimple = QtGui.QGroupBox(KeywordsDialogBase)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.grpSimple.sizePolicy().hasHeightForWidth())
        self.grpSimple.setSizePolicy(sizePolicy)
        self.grpSimple.setObjectName(_fromUtf8("grpSimple"))
        self.gridLayout_2 = QtGui.QGridLayout(self.grpSimple)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.cboElderRatioAttribute = QtGui.QComboBox(self.grpSimple)
        self.cboElderRatioAttribute.setObjectName(_fromUtf8("cboElderRatioAttribute"))
        self.gridLayout_2.addWidget(self.cboElderRatioAttribute, 13, 2, 1, 1)
        self.leSource = QtGui.QLineEdit(self.grpSimple)
        self.leSource.setDragEnabled(True)
        self.leSource.setObjectName(_fromUtf8("leSource"))
        self.gridLayout_2.addWidget(self.leSource, 2, 2, 1, 1)
        self.lblAggregationAttribute = QtGui.QLabel(self.grpSimple)
        self.lblAggregationAttribute.setEnabled(True)
        self.lblAggregationAttribute.setObjectName(_fromUtf8("lblAggregationAttribute"))
        self.gridLayout_2.addWidget(self.lblAggregationAttribute, 6, 0, 1, 2)
        self.cboAggregationAttribute = QtGui.QComboBox(self.grpSimple)
        self.cboAggregationAttribute.setObjectName(_fromUtf8("cboAggregationAttribute"))
        self.gridLayout_2.addWidget(self.cboAggregationAttribute, 6, 2, 1, 1)
        self.cboSubcategory = QtGui.QComboBox(self.grpSimple)
        self.cboSubcategory.setObjectName(_fromUtf8("cboSubcategory"))
        self.gridLayout_2.addWidget(self.cboSubcategory, 5, 2, 1, 1)
        self.lblFemaleRatioAttribute = QtGui.QLabel(self.grpSimple)
        self.lblFemaleRatioAttribute.setObjectName(_fromUtf8("lblFemaleRatioAttribute"))
        self.gridLayout_2.addWidget(self.lblFemaleRatioAttribute, 7, 0, 1, 2)
        self.lblSubcategory = QtGui.QLabel(self.grpSimple)
        self.lblSubcategory.setObjectName(_fromUtf8("lblSubcategory"))
        self.gridLayout_2.addWidget(self.lblSubcategory, 5, 0, 1, 1)
        self.lblFemaleRatioDefault = QtGui.QLabel(self.grpSimple)
        self.lblFemaleRatioDefault.setObjectName(_fromUtf8("lblFemaleRatioDefault"))
        self.gridLayout_2.addWidget(self.lblFemaleRatioDefault, 8, 0, 1, 1)
        self.lblSource = QtGui.QLabel(self.grpSimple)
        self.lblSource.setObjectName(_fromUtf8("lblSource"))
        self.gridLayout_2.addWidget(self.lblSource, 2, 0, 1, 1)
        self.dsbFemaleRatioDefault = QtGui.QDoubleSpinBox(self.grpSimple)
        self.dsbFemaleRatioDefault.setAccelerated(True)
        self.dsbFemaleRatioDefault.setMaximum(1.0)
        self.dsbFemaleRatioDefault.setSingleStep(0.01)
        self.dsbFemaleRatioDefault.setProperty("value", 0.0)
        self.dsbFemaleRatioDefault.setObjectName(_fromUtf8("dsbFemaleRatioDefault"))
        self.gridLayout_2.addWidget(self.dsbFemaleRatioDefault, 8, 2, 1, 1)
        self.cboFemaleRatioAttribute = QtGui.QComboBox(self.grpSimple)
        self.cboFemaleRatioAttribute.setObjectName(_fromUtf8("cboFemaleRatioAttribute"))
        self.gridLayout_2.addWidget(self.cboFemaleRatioAttribute, 7, 2, 1, 1)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.radHazard = QtGui.QRadioButton(self.grpSimple)
        self.radHazard.setObjectName(_fromUtf8("radHazard"))
        self.horizontalLayout_3.addWidget(self.radHazard)
        self.radExposure = QtGui.QRadioButton(self.grpSimple)
        self.radExposure.setChecked(True)
        self.radExposure.setObjectName(_fromUtf8("radExposure"))
        self.horizontalLayout_3.addWidget(self.radExposure)
        self.radPostprocessing = QtGui.QRadioButton(self.grpSimple)
        self.radPostprocessing.setObjectName(_fromUtf8("radPostprocessing"))
        self.horizontalLayout_3.addWidget(self.radPostprocessing)
        self.gridLayout_2.addLayout(self.horizontalLayout_3, 4, 2, 1, 1)
        self.lblTitle = QtGui.QLabel(self.grpSimple)
        self.lblTitle.setObjectName(_fromUtf8("lblTitle"))
        self.gridLayout_2.addWidget(self.lblTitle, 1, 0, 1, 1)
        self.lblCategory = QtGui.QLabel(self.grpSimple)
        self.lblCategory.setObjectName(_fromUtf8("lblCategory"))
        self.gridLayout_2.addWidget(self.lblCategory, 4, 0, 1, 1)
        self.leTitle = QtGui.QLineEdit(self.grpSimple)
        self.leTitle.setObjectName(_fromUtf8("leTitle"))
        self.gridLayout_2.addWidget(self.leTitle, 1, 2, 1, 1)
        self.dsbAdultRatioDefault = QtGui.QDoubleSpinBox(self.grpSimple)
        self.dsbAdultRatioDefault.setObjectName(_fromUtf8("dsbAdultRatioDefault"))
        self.gridLayout_2.addWidget(self.dsbAdultRatioDefault, 12, 2, 1, 1)
        self.cboYouthRatioAttribute = QtGui.QComboBox(self.grpSimple)
        self.cboYouthRatioAttribute.setObjectName(_fromUtf8("cboYouthRatioAttribute"))
        self.gridLayout_2.addWidget(self.cboYouthRatioAttribute, 9, 2, 1, 1)
        self.dsbYouthRatioDefault = QtGui.QDoubleSpinBox(self.grpSimple)
        self.dsbYouthRatioDefault.setObjectName(_fromUtf8("dsbYouthRatioDefault"))
        self.gridLayout_2.addWidget(self.dsbYouthRatioDefault, 10, 2, 1, 1)
        self.cboAdultRatioAttribute = QtGui.QComboBox(self.grpSimple)
        self.cboAdultRatioAttribute.setObjectName(_fromUtf8("cboAdultRatioAttribute"))
        self.gridLayout_2.addWidget(self.cboAdultRatioAttribute, 11, 2, 1, 1)
        self.dsbElderRatioDefault = QtGui.QDoubleSpinBox(self.grpSimple)
        self.dsbElderRatioDefault.setObjectName(_fromUtf8("dsbElderRatioDefault"))
        self.gridLayout_2.addWidget(self.dsbElderRatioDefault, 14, 2, 1, 1)
        self.lblElderRatioDefault = QtGui.QLabel(self.grpSimple)
        self.lblElderRatioDefault.setObjectName(_fromUtf8("lblElderRatioDefault"))
        self.gridLayout_2.addWidget(self.lblElderRatioDefault, 14, 0, 1, 1)
        self.lblElderRatioAttribute = QtGui.QLabel(self.grpSimple)
        self.lblElderRatioAttribute.setObjectName(_fromUtf8("lblElderRatioAttribute"))
        self.gridLayout_2.addWidget(self.lblElderRatioAttribute, 13, 0, 1, 1)
        self.lblAdultRatioDefault = QtGui.QLabel(self.grpSimple)
        self.lblAdultRatioDefault.setObjectName(_fromUtf8("lblAdultRatioDefault"))
        self.gridLayout_2.addWidget(self.lblAdultRatioDefault, 12, 0, 1, 1)
        self.lblAdultRatioAttribute = QtGui.QLabel(self.grpSimple)
        self.lblAdultRatioAttribute.setObjectName(_fromUtf8("lblAdultRatioAttribute"))
        self.gridLayout_2.addWidget(self.lblAdultRatioAttribute, 11, 0, 1, 1)
        self.lblYouthRatioDefault = QtGui.QLabel(self.grpSimple)
        self.lblYouthRatioDefault.setObjectName(_fromUtf8("lblYouthRatioDefault"))
        self.gridLayout_2.addWidget(self.lblYouthRatioDefault, 10, 0, 1, 1)
        self.lblYouthRatioAttribute = QtGui.QLabel(self.grpSimple)
        self.lblYouthRatioAttribute.setObjectName(_fromUtf8("lblYouthRatioAttribute"))
        self.gridLayout_2.addWidget(self.lblYouthRatioAttribute, 9, 0, 1, 1)
        self.verticalLayout.addWidget(self.grpSimple)
        self.pbnAdvanced = QtGui.QPushButton(KeywordsDialogBase)
        self.pbnAdvanced.setCheckable(True)
        self.pbnAdvanced.setObjectName(_fromUtf8("pbnAdvanced"))
        self.verticalLayout.addWidget(self.pbnAdvanced)
        self.grpAdvanced = QtGui.QGroupBox(KeywordsDialogBase)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.grpAdvanced.sizePolicy().hasHeightForWidth())
        self.grpAdvanced.setSizePolicy(sizePolicy)
        self.grpAdvanced.setObjectName(_fromUtf8("grpAdvanced"))
        self.gridLayout = QtGui.QGridLayout(self.grpAdvanced)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.radPredefined = QtGui.QRadioButton(self.grpAdvanced)
        self.radPredefined.setObjectName(_fromUtf8("radPredefined"))
        self.horizontalLayout_4.addWidget(self.radPredefined)
        self.radUserDefined = QtGui.QRadioButton(self.grpAdvanced)
        self.radUserDefined.setObjectName(_fromUtf8("radUserDefined"))
        self.horizontalLayout_4.addWidget(self.radUserDefined)
        self.gridLayout.addLayout(self.horizontalLayout_4, 0, 0, 1, 1)
        self.framePredefined = QtGui.QFrame(self.grpAdvanced)
        self.framePredefined.setFrameShape(QtGui.QFrame.StyledPanel)
        self.framePredefined.setFrameShadow(QtGui.QFrame.Raised)
        self.framePredefined.setObjectName(_fromUtf8("framePredefined"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.framePredefined)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label_4 = QtGui.QLabel(self.framePredefined)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.horizontalLayout.addWidget(self.label_4)
        self.cboKeyword = QtGui.QComboBox(self.framePredefined)
        self.cboKeyword.setObjectName(_fromUtf8("cboKeyword"))
        self.cboKeyword.addItem(_fromUtf8(""))
        self.cboKeyword.setItemText(0, _fromUtf8("subcategory"))
        self.cboKeyword.addItem(_fromUtf8(""))
        self.cboKeyword.setItemText(1, _fromUtf8("unit"))
        self.cboKeyword.addItem(_fromUtf8(""))
        self.cboKeyword.setItemText(2, _fromUtf8("datatype"))
        self.cboKeyword.addItem(_fromUtf8(""))
        self.cboKeyword.setItemText(3, _fromUtf8("key_attribute"))
        self.horizontalLayout.addWidget(self.cboKeyword)
        self.label_5 = QtGui.QLabel(self.framePredefined)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.horizontalLayout.addWidget(self.label_5)
        self.lePredefinedValue = QtGui.QLineEdit(self.framePredefined)
        self.lePredefinedValue.setObjectName(_fromUtf8("lePredefinedValue"))
        self.horizontalLayout.addWidget(self.lePredefinedValue)
        self.pbnAddToList1 = QtGui.QPushButton(self.framePredefined)
        self.pbnAddToList1.setObjectName(_fromUtf8("pbnAddToList1"))
        self.horizontalLayout.addWidget(self.pbnAddToList1)
        self.gridLayout.addWidget(self.framePredefined, 1, 0, 1, 1)
        self.frameUserDefined = QtGui.QFrame(self.grpAdvanced)
        self.frameUserDefined.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frameUserDefined.setFrameShadow(QtGui.QFrame.Raised)
        self.frameUserDefined.setObjectName(_fromUtf8("frameUserDefined"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.frameUserDefined)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label_6 = QtGui.QLabel(self.frameUserDefined)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.horizontalLayout_2.addWidget(self.label_6)
        self.leKey = QtGui.QLineEdit(self.frameUserDefined)
        self.leKey.setObjectName(_fromUtf8("leKey"))
        self.horizontalLayout_2.addWidget(self.leKey)
        self.label_7 = QtGui.QLabel(self.frameUserDefined)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.horizontalLayout_2.addWidget(self.label_7)
        self.leValue = QtGui.QLineEdit(self.frameUserDefined)
        self.leValue.setObjectName(_fromUtf8("leValue"))
        self.horizontalLayout_2.addWidget(self.leValue)
        self.pbnAddToList2 = QtGui.QPushButton(self.frameUserDefined)
        self.pbnAddToList2.setObjectName(_fromUtf8("pbnAddToList2"))
        self.horizontalLayout_2.addWidget(self.pbnAddToList2)
        self.gridLayout.addWidget(self.frameUserDefined, 2, 0, 1, 1)
        self.label_8 = QtGui.QLabel(self.grpAdvanced)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.gridLayout.addWidget(self.label_8, 3, 0, 1, 1)
        self.lstKeywords = QtGui.QListWidget(self.grpAdvanced)
        self.lstKeywords.setAlternatingRowColors(True)
        self.lstKeywords.setSelectionMode(QtGui.QAbstractItemView.ExtendedSelection)
        self.lstKeywords.setObjectName(_fromUtf8("lstKeywords"))
        self.gridLayout.addWidget(self.lstKeywords, 4, 0, 1, 1)
        self.lblMessage = QtGui.QLabel(self.grpAdvanced)
        self.lblMessage.setStyleSheet(_fromUtf8("color: red;"))
        self.lblMessage.setText(_fromUtf8(""))
        self.lblMessage.setTextFormat(QtCore.Qt.RichText)
        self.lblMessage.setWordWrap(True)
        self.lblMessage.setObjectName(_fromUtf8("lblMessage"))
        self.gridLayout.addWidget(self.lblMessage, 5, 0, 1, 1)
        self.pbnRemove = QtGui.QPushButton(self.grpAdvanced)
        self.pbnRemove.setObjectName(_fromUtf8("pbnRemove"))
        self.gridLayout.addWidget(self.pbnRemove, 6, 0, 1, 1)
        self.verticalLayout.addWidget(self.grpAdvanced)
        self.buttonBox = QtGui.QDialogButtonBox(KeywordsDialogBase)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.buttonBox.sizePolicy().hasHeightForWidth())
        self.buttonBox.setSizePolicy(sizePolicy)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Help|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setCenterButtons(False)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.verticalLayout.addWidget(self.buttonBox)
        self.lblSubcategory.setBuddy(self.cboSubcategory)
        self.label_4.setBuddy(self.cboKeyword)
        self.label_6.setBuddy(self.leKey)
        self.label_7.setBuddy(self.leValue)
        self.label_8.setBuddy(self.lstKeywords)

        self.retranslateUi(KeywordsDialogBase)
        QtCore.QObject.connect(self.radPredefined, QtCore.SIGNAL(_fromUtf8("toggled(bool)")), self.frameUserDefined.setHidden)
        QtCore.QObject.connect(self.radUserDefined, QtCore.SIGNAL(_fromUtf8("toggled(bool)")), self.framePredefined.setHidden)
        QtCore.QObject.connect(self.radPredefined, QtCore.SIGNAL(_fromUtf8("toggled(bool)")), self.framePredefined.setVisible)
        QtCore.QObject.connect(self.radUserDefined, QtCore.SIGNAL(_fromUtf8("toggled(bool)")), self.frameUserDefined.setVisible)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), KeywordsDialogBase.reject)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), KeywordsDialogBase.accept)
        QtCore.QMetaObject.connectSlotsByName(KeywordsDialogBase)
        KeywordsDialogBase.setTabOrder(self.leTitle, self.leSource)
        KeywordsDialogBase.setTabOrder(self.leSource, self.radHazard)
        KeywordsDialogBase.setTabOrder(self.radHazard, self.radExposure)
        KeywordsDialogBase.setTabOrder(self.radExposure, self.radPostprocessing)
        KeywordsDialogBase.setTabOrder(self.radPostprocessing, self.cboSubcategory)
        KeywordsDialogBase.setTabOrder(self.cboSubcategory, self.cboAggregationAttribute)
        KeywordsDialogBase.setTabOrder(self.cboAggregationAttribute, self.cboFemaleRatioAttribute)
        KeywordsDialogBase.setTabOrder(self.cboFemaleRatioAttribute, self.dsbFemaleRatioDefault)
        KeywordsDialogBase.setTabOrder(self.dsbFemaleRatioDefault, self.pbnAdvanced)
        KeywordsDialogBase.setTabOrder(self.pbnAdvanced, self.radPredefined)
        KeywordsDialogBase.setTabOrder(self.radPredefined, self.radUserDefined)
        KeywordsDialogBase.setTabOrder(self.radUserDefined, self.cboKeyword)
        KeywordsDialogBase.setTabOrder(self.cboKeyword, self.lePredefinedValue)
        KeywordsDialogBase.setTabOrder(self.lePredefinedValue, self.pbnAddToList1)
        KeywordsDialogBase.setTabOrder(self.pbnAddToList1, self.leKey)
        KeywordsDialogBase.setTabOrder(self.leKey, self.leValue)
        KeywordsDialogBase.setTabOrder(self.leValue, self.pbnAddToList2)
        KeywordsDialogBase.setTabOrder(self.pbnAddToList2, self.lstKeywords)
        KeywordsDialogBase.setTabOrder(self.lstKeywords, self.pbnRemove)
        KeywordsDialogBase.setTabOrder(self.pbnRemove, self.buttonBox)

    def retranslateUi(self, KeywordsDialogBase):
        KeywordsDialogBase.setWindowTitle(QtGui.QApplication.translate("KeywordsDialogBase", "InaSAFE - Keyword Editor", None, QtGui.QApplication.UnicodeUTF8))
        self.grpSimple.setTitle(QtGui.QApplication.translate("KeywordsDialogBase", "Quick edit", None, QtGui.QApplication.UnicodeUTF8))
        self.lblAggregationAttribute.setText(QtGui.QApplication.translate("KeywordsDialogBase", "Aggregation attribute", None, QtGui.QApplication.UnicodeUTF8))
        self.cboSubcategory.setToolTip(QtGui.QApplication.translate("KeywordsDialogBase", "A subcategory represents the type of hazard.", None, QtGui.QApplication.UnicodeUTF8))
        self.lblFemaleRatioAttribute.setText(QtGui.QApplication.translate("KeywordsDialogBase", "Female ratio attribute", None, QtGui.QApplication.UnicodeUTF8))
        self.lblSubcategory.setText(QtGui.QApplication.translate("KeywordsDialogBase", "Subcategory", None, QtGui.QApplication.UnicodeUTF8))
        self.lblFemaleRatioDefault.setText(QtGui.QApplication.translate("KeywordsDialogBase", "Female ratio default", None, QtGui.QApplication.UnicodeUTF8))
        self.lblSource.setText(QtGui.QApplication.translate("KeywordsDialogBase", "Source", None, QtGui.QApplication.UnicodeUTF8))
        self.radHazard.setToolTip(QtGui.QApplication.translate("KeywordsDialogBase", "A hazard is a situation that poses a level of threat to life, health, property, or environment. (Wikipedia)", None, QtGui.QApplication.UnicodeUTF8))
        self.radHazard.setText(QtGui.QApplication.translate("KeywordsDialogBase", "Hazard", None, QtGui.QApplication.UnicodeUTF8))
        self.radExposure.setToolTip(QtGui.QApplication.translate("KeywordsDialogBase", "Where people and property are situated.", None, QtGui.QApplication.UnicodeUTF8))
        self.radExposure.setText(QtGui.QApplication.translate("KeywordsDialogBase", "Exposure", None, QtGui.QApplication.UnicodeUTF8))
        self.radPostprocessing.setText(QtGui.QApplication.translate("KeywordsDialogBase", "Postprocessing", None, QtGui.QApplication.UnicodeUTF8))
        self.lblTitle.setText(QtGui.QApplication.translate("KeywordsDialogBase", "Title", None, QtGui.QApplication.UnicodeUTF8))
        self.lblCategory.setText(QtGui.QApplication.translate("KeywordsDialogBase", "Category", None, QtGui.QApplication.UnicodeUTF8))
        self.lblElderRatioDefault.setText(QtGui.QApplication.translate("KeywordsDialogBase", "Elder ratio default", None, QtGui.QApplication.UnicodeUTF8))
        self.lblElderRatioAttribute.setText(QtGui.QApplication.translate("KeywordsDialogBase", "Elder ratio attribute", None, QtGui.QApplication.UnicodeUTF8))
        self.lblAdultRatioDefault.setText(QtGui.QApplication.translate("KeywordsDialogBase", "Adult ratio default", None, QtGui.QApplication.UnicodeUTF8))
        self.lblAdultRatioAttribute.setText(QtGui.QApplication.translate("KeywordsDialogBase", "Adult ratio attribute", None, QtGui.QApplication.UnicodeUTF8))
        self.lblYouthRatioDefault.setText(QtGui.QApplication.translate("KeywordsDialogBase", "Youth ratio default", None, QtGui.QApplication.UnicodeUTF8))
        self.lblYouthRatioAttribute.setText(QtGui.QApplication.translate("KeywordsDialogBase", "Youth ratio attribute", None, QtGui.QApplication.UnicodeUTF8))
        self.pbnAdvanced.setText(QtGui.QApplication.translate("KeywordsDialogBase", "Show advanced editor", None, QtGui.QApplication.UnicodeUTF8))
        self.grpAdvanced.setTitle(QtGui.QApplication.translate("KeywordsDialogBase", "Advanced editor", None, QtGui.QApplication.UnicodeUTF8))
        self.radPredefined.setText(QtGui.QApplication.translate("KeywordsDialogBase", "Predefined", None, QtGui.QApplication.UnicodeUTF8))
        self.radUserDefined.setText(QtGui.QApplication.translate("KeywordsDialogBase", "User defined", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("KeywordsDialogBase", "Keyword", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("KeywordsDialogBase", "Value", None, QtGui.QApplication.UnicodeUTF8))
        self.pbnAddToList1.setText(QtGui.QApplication.translate("KeywordsDialogBase", "Add to list", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("KeywordsDialogBase", "Key", None, QtGui.QApplication.UnicodeUTF8))
        self.label_7.setText(QtGui.QApplication.translate("KeywordsDialogBase", "Value", None, QtGui.QApplication.UnicodeUTF8))
        self.pbnAddToList2.setText(QtGui.QApplication.translate("KeywordsDialogBase", "Add to list", None, QtGui.QApplication.UnicodeUTF8))
        self.label_8.setText(QtGui.QApplication.translate("KeywordsDialogBase", "Current keywords", None, QtGui.QApplication.UnicodeUTF8))
        self.pbnRemove.setText(QtGui.QApplication.translate("KeywordsDialogBase", "Remove selected", None, QtGui.QApplication.UnicodeUTF8))

import resources_rc
