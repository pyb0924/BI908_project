# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'uiOtsu.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Otsu(object):
    def setupUi(self, Otsu):
        if not Otsu.objectName():
            Otsu.setObjectName(u"Otsu")
        Otsu.resize(400, 200)
        Otsu.setMinimumSize(QSize(200, 100))
        Otsu.setMaximumSize(QSize(400, 200))
        self.widget = QWidget(Otsu)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(12, 12, 371, 171))
        self.verticalLayout = QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.OtsuBGlabel = QLabel(self.widget)
        self.OtsuBGlabel.setObjectName(u"OtsuBGlabel")
        self.OtsuBGlabel.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.OtsuBGlabel)

        self.OtsuBGEdit = QLineEdit(self.widget)
        self.OtsuBGEdit.setObjectName(u"OtsuBGEdit")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.OtsuBGEdit.sizePolicy().hasHeightForWidth())
        self.OtsuBGEdit.setSizePolicy(sizePolicy)

        self.horizontalLayout.addWidget(self.OtsuBGEdit)

        self.horizontalLayout.setStretch(0, 4)
        self.horizontalLayout.setStretch(1, 2)

        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")

        self.horizontalLayout_3.addWidget(self.label)

        self.TradButton = QRadioButton(self.widget)
        self.TradButton.setObjectName(u"TradButton")

        self.horizontalLayout_3.addWidget(self.TradButton)

        self.NewButton = QRadioButton(self.widget)
        self.NewButton.setObjectName(u"NewButton")

        self.horizontalLayout_3.addWidget(self.NewButton)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)

        self.pushButton = QPushButton(self.widget)
        self.pushButton.setObjectName(u"pushButton")

        self.horizontalLayout_2.addWidget(self.pushButton)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)


        self.verticalLayout.addLayout(self.horizontalLayout_2)


        self.retranslateUi(Otsu)

        QMetaObject.connectSlotsByName(Otsu)
    # setupUi

    def retranslateUi(self, Otsu):
        Otsu.setWindowTitle(QCoreApplication.translate("Otsu", u"Form", None))
        self.OtsuBGlabel.setText(QCoreApplication.translate("Otsu", u"\u5ffd\u7565\u7684\u7070\u5ea6\u4e0a\u9650", None))
        self.label.setText(QCoreApplication.translate("Otsu", u"Type", None))
        self.TradButton.setText(QCoreApplication.translate("Otsu", u"Traditional", None))
        self.NewButton.setText(QCoreApplication.translate("Otsu", u"New", None))
        self.pushButton.setText(QCoreApplication.translate("Otsu", u"\u786e\u5b9a", None))
    # retranslateUi
