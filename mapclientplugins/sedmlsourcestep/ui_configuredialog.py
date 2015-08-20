# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'qt/configuredialog.ui'
#
# Created: Thu Aug 20 16:38:36 2015
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_ConfigureDialog(object):
    def setupUi(self, ConfigureDialog):
        ConfigureDialog.setObjectName("ConfigureDialog")
        ConfigureDialog.resize(507, 212)
        self.gridLayout = QtGui.QGridLayout(ConfigureDialog)
        self.gridLayout.setObjectName("gridLayout")
        self.buttonBox = QtGui.QDialogButtonBox(ConfigureDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout.addWidget(self.buttonBox, 2, 0, 1, 1)
        self.configGroupBox = QtGui.QGroupBox(ConfigureDialog)
        self.configGroupBox.setTitle("")
        self.configGroupBox.setObjectName("configGroupBox")
        self.gridLayout_2 = QtGui.QGridLayout(self.configGroupBox)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label1 = QtGui.QLabel(self.configGroupBox)
        self.label1.setObjectName("label1")
        self.gridLayout_2.addWidget(self.label1, 1, 0, 1, 1)
        self.label0 = QtGui.QLabel(self.configGroupBox)
        self.label0.setObjectName("label0")
        self.gridLayout_2.addWidget(self.label0, 0, 0, 1, 1)
        self.lineEditIdentifier = QtGui.QLineEdit(self.configGroupBox)
        self.lineEditIdentifier.setObjectName("lineEditIdentifier")
        self.gridLayout_2.addWidget(self.lineEditIdentifier, 0, 1, 1, 1)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.lineEditLocation = QtGui.QLineEdit(self.configGroupBox)
        self.lineEditLocation.setObjectName("lineEditLocation")
        self.horizontalLayout.addWidget(self.lineEditLocation)
        self.pushButtonLocation = QtGui.QPushButton(self.configGroupBox)
        self.pushButtonLocation.setObjectName("pushButtonLocation")
        self.horizontalLayout.addWidget(self.pushButtonLocation)
        self.gridLayout_2.addLayout(self.horizontalLayout, 1, 1, 1, 1)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem, 2, 1, 1, 1)
        self.gridLayout.addWidget(self.configGroupBox, 1, 0, 1, 1)

        self.retranslateUi(ConfigureDialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), ConfigureDialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("rejected()"), ConfigureDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(ConfigureDialog)

    def retranslateUi(self, ConfigureDialog):
        ConfigureDialog.setWindowTitle(QtGui.QApplication.translate("ConfigureDialog", "ConfigureDialog", None, QtGui.QApplication.UnicodeUTF8))
        self.label1.setText(QtGui.QApplication.translate("ConfigureDialog", "Location:  ", None, QtGui.QApplication.UnicodeUTF8))
        self.label0.setText(QtGui.QApplication.translate("ConfigureDialog", "identifier:  ", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonLocation.setText(QtGui.QApplication.translate("ConfigureDialog", "...", None, QtGui.QApplication.UnicodeUTF8))

