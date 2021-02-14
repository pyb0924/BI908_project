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


class Ui_Opening_Closing(object):
    def setupUi(self, Opening_Closing):
        if not Opening_Closing.objectName():
            Opening_Closing.setObjectName(u"Opening_Closing")
        Opening_Closing.resize(400, 300)
        self.layoutWidget = QWidget(Opening_Closing)
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

        self.radioButton = QRadioButton(self.layoutWidget)
        self.radioButton.setObjectName(u"radioButton")

        self.horizontalLayout.addWidget(self.radioButton)

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

        self.horizontalLayout_2.addWidget(self.radiusBox)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.affirmButton = QPushButton(self.layoutWidget)
        self.affirmButton.setObjectName(u"affirmButton")

        self.verticalLayout.addWidget(self.affirmButton)


        self.retranslateUi(Opening_Closing)

        QMetaObject.connectSlotsByName(Opening_Closing)
    # setupUi

    def retranslateUi(self, Opening_Closing):
        Opening_Closing.setWindowTitle(QCoreApplication.translate("Opening_Closing", u"Form", None))
        self.label.setText(QCoreApplication.translate("Opening_Closing", u"Type", None))
        self.radioButton.setText(QCoreApplication.translate("Opening_Closing", u"Opening", None))
        self.closingButton.setText(QCoreApplication.translate("Opening_Closing", u"Closing", None))
        self.label_2.setText(QCoreApplication.translate("Opening_Closing", u"Radius", None))
        self.affirmButton.setText(QCoreApplication.translate("Opening_Closing", u"\u786e\u5b9a", None))
    # retranslateUi

