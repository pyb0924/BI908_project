# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'uiOC.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_OC(object):
    def setupUi(self, OC):
        if not OC.objectName():
            OC.setObjectName(u"OC")
        OC.resize(400, 300)
        self.layoutWidget = QWidget(OC)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(20, 30, 361, 221))
        self.verticalLayout = QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(self.layoutWidget)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.openingButton = QRadioButton(self.layoutWidget)
        self.openingButton.setObjectName(u"openingButton")

        self.horizontalLayout.addWidget(self.openingButton)

        self.closingButton = QRadioButton(self.layoutWidget)
        self.closingButton.setObjectName(u"closingButton")

        self.horizontalLayout.addWidget(self.closingButton)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_2 = QLabel(self.layoutWidget)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_2.addWidget(self.label_2)

        self.radiusBox = QSpinBox(self.layoutWidget)
        self.radiusBox.setObjectName(u"radiusBox")
        self.radiusBox.setMinimum(1)

        self.horizontalLayout_2.addWidget(self.radiusBox)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.affirmButton = QPushButton(self.layoutWidget)
        self.affirmButton.setObjectName(u"affirmButton")

        self.verticalLayout.addWidget(self.affirmButton)


        self.retranslateUi(OC)

        QMetaObject.connectSlotsByName(OC)
    # setupUi

    def retranslateUi(self, OC):
        OC.setWindowTitle(QCoreApplication.translate("OC", u"Opening/Closing", None))
        self.label.setText(QCoreApplication.translate("OC", u"Type", None))
        self.openingButton.setText(QCoreApplication.translate("OC", u"Opening", None))
        self.closingButton.setText(QCoreApplication.translate("OC", u"Closing", None))
        self.label_2.setText(QCoreApplication.translate("OC", u"Radius", None))
        self.affirmButton.setText(QCoreApplication.translate("OC", u"\u786e\u5b9a", None))
    # retranslateUi

