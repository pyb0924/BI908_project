# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'uiValid.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Validation(object):
    def setupUi(self, Validation):
        if not Validation.objectName():
            Validation.setObjectName(u"Validation")
        Validation.resize(495, 375)
        self.centralwidget = QWidget(Validation)
        self.centralwidget.setObjectName(u"centralwidget")
        self.layoutWidget = QWidget(self.centralwidget)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(240, 15, 181, 271))
        self.verticalLayout = QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.senEdit = QLineEdit(self.layoutWidget)
        self.senEdit.setObjectName(u"senEdit")

        self.verticalLayout.addWidget(self.senEdit)

        self.preEdit = QLineEdit(self.layoutWidget)
        self.preEdit.setObjectName(u"preEdit")

        self.verticalLayout.addWidget(self.preEdit)

        self.accEdit = QLineEdit(self.layoutWidget)
        self.accEdit.setObjectName(u"accEdit")

        self.verticalLayout.addWidget(self.accEdit)

        self.iouEdit = QLineEdit(self.layoutWidget)
        self.iouEdit.setObjectName(u"iouEdit")

        self.verticalLayout.addWidget(self.iouEdit)

        self.diceEdit = QLineEdit(self.layoutWidget)
        self.diceEdit.setObjectName(u"diceEdit")

        self.verticalLayout.addWidget(self.diceEdit)

        self.layoutWidget_2 = QWidget(self.centralwidget)
        self.layoutWidget_2.setObjectName(u"layoutWidget_2")
        self.layoutWidget_2.setGeometry(QRect(70, 305, 341, 41))
        self.horizontalLayout = QHBoxLayout(self.layoutWidget_2)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.openButton = QPushButton(self.layoutWidget_2)
        self.openButton.setObjectName(u"openButton")

        self.horizontalLayout.addWidget(self.openButton)

        self.saveButton = QPushButton(self.layoutWidget_2)
        self.saveButton.setObjectName(u"saveButton")

        self.horizontalLayout.addWidget(self.saveButton)

        self.closeButton = QPushButton(self.layoutWidget_2)
        self.closeButton.setObjectName(u"closeButton")

        self.horizontalLayout.addWidget(self.closeButton)

        self.layoutWidget_3 = QWidget(self.centralwidget)
        self.layoutWidget_3.setObjectName(u"layoutWidget_3")
        self.layoutWidget_3.setGeometry(QRect(60, 20, 131, 241))
        self.verticalLayout_2 = QVBoxLayout(self.layoutWidget_3)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label_1 = QLabel(self.layoutWidget_3)
        self.label_1.setObjectName(u"label_1")

        self.verticalLayout_2.addWidget(self.label_1)

        self.label_4 = QLabel(self.layoutWidget_3)
        self.label_4.setObjectName(u"label_4")

        self.verticalLayout_2.addWidget(self.label_4)

        self.label_5 = QLabel(self.layoutWidget_3)
        self.label_5.setObjectName(u"label_5")

        self.verticalLayout_2.addWidget(self.label_5)

        self.label_2 = QLabel(self.layoutWidget_3)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout_2.addWidget(self.label_2)

        self.label_3 = QLabel(self.layoutWidget_3)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout_2.addWidget(self.label_3)

        Validation.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(Validation)
        self.statusbar.setObjectName(u"statusbar")
        Validation.setStatusBar(self.statusbar)

        self.retranslateUi(Validation)

        QMetaObject.connectSlotsByName(Validation)
    # setupUi

    def retranslateUi(self, Validation):
        Validation.setWindowTitle(QCoreApplication.translate("Validation", u"Validation", None))
        self.openButton.setText(QCoreApplication.translate("Validation", u"Open(Label)", None))
        self.saveButton.setText(QCoreApplication.translate("Validation", u"Save", None))
        self.closeButton.setText(QCoreApplication.translate("Validation", u"Close", None))
        self.label_1.setText(QCoreApplication.translate("Validation", u"Sensitivity", None))
        self.label_4.setText(QCoreApplication.translate("Validation", u"Precision", None))
        self.label_5.setText(QCoreApplication.translate("Validation", u"Accuracy", None))
        self.label_2.setText(QCoreApplication.translate("Validation", u"IoU", None))
        self.label_3.setText(QCoreApplication.translate("Validation", u"Dice", None))
    # retranslateUi

