# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'uiRG.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_RegionGrowing(object):
    def setupUi(self, RegionGrowing):
        if not RegionGrowing.objectName():
            RegionGrowing.setObjectName(u"RegionGrowing")
        RegionGrowing.resize(460, 300)
        RegionGrowing.setMinimumSize(QSize(460, 300))
        RegionGrowing.setMaximumSize(QSize(460, 300))
        RegionGrowing.setBaseSize(QSize(380, 400))
        self.widget = QWidget(RegionGrowing)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(10, 20, 441, 271))
        self.verticalLayout_3 = QVBoxLayout(self.widget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.OtsuBGlabel = QLabel(self.widget)
        self.OtsuBGlabel.setObjectName(u"OtsuBGlabel")

        self.verticalLayout_2.addWidget(self.OtsuBGlabel)

        self.OtsuBGlabel_2 = QLabel(self.widget)
        self.OtsuBGlabel_2.setObjectName(u"OtsuBGlabel_2")

        self.verticalLayout_2.addWidget(self.OtsuBGlabel_2)

        self.OtsuBGlabel_3 = QLabel(self.widget)
        self.OtsuBGlabel_3.setObjectName(u"OtsuBGlabel_3")

        self.verticalLayout_2.addWidget(self.OtsuBGlabel_3)

        self.OtsuBGlabel_4 = QLabel(self.widget)
        self.OtsuBGlabel_4.setObjectName(u"OtsuBGlabel_4")

        self.verticalLayout_2.addWidget(self.OtsuBGlabel_4)


        self.horizontalLayout.addLayout(self.verticalLayout_2)

        self.horizontalSpacer = QSpacerItem(80, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(15)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.RGtEdit = QLineEdit(self.widget)
        self.RGtEdit.setObjectName(u"RGtEdit")

        self.verticalLayout.addWidget(self.RGtEdit)

        self.RGradiusEdit = QLineEdit(self.widget)
        self.RGradiusEdit.setObjectName(u"RGradiusEdit")

        self.verticalLayout.addWidget(self.RGradiusEdit)

        self.RGitermaxEdit = QLineEdit(self.widget)
        self.RGitermaxEdit.setObjectName(u"RGitermaxEdit")

        self.verticalLayout.addWidget(self.RGitermaxEdit)

        self.RGtypeBox = QComboBox(self.widget)
        self.RGtypeBox.addItem("")
        self.RGtypeBox.addItem("")
        self.RGtypeBox.setObjectName(u"RGtypeBox")

        self.verticalLayout.addWidget(self.RGtypeBox)


        self.horizontalLayout.addLayout(self.verticalLayout)

        self.horizontalLayout.setStretch(0, 4)
        self.horizontalLayout.setStretch(1, 1)
        self.horizontalLayout.setStretch(2, 4)

        self.verticalLayout_3.addLayout(self.horizontalLayout)

        self.affirmButton = QPushButton(self.widget)
        self.affirmButton.setObjectName(u"affirmButton")

        self.verticalLayout_3.addWidget(self.affirmButton)


        self.retranslateUi(RegionGrowing)

        QMetaObject.connectSlotsByName(RegionGrowing)
    # setupUi

    def retranslateUi(self, RegionGrowing):
        RegionGrowing.setWindowTitle(QCoreApplication.translate("RegionGrowing", u"Form", None))
        self.OtsuBGlabel.setText(QCoreApplication.translate("RegionGrowing", u"\u90bb\u57df\u9608\u503c", None))
        self.OtsuBGlabel_2.setText(QCoreApplication.translate("RegionGrowing", u"\u90bb\u57df\u534a\u5f84", None))
        self.OtsuBGlabel_3.setText(QCoreApplication.translate("RegionGrowing", u"\u8fed\u4ee3\u6b21\u6570\u4e0a\u9650", None))
        self.OtsuBGlabel_4.setText(QCoreApplication.translate("RegionGrowing", u"\u53bb\u7edd\u5bf9\u503c\u5904\u7406", None))
        self.RGtypeBox.setItemText(0, QCoreApplication.translate("RegionGrowing", u"\u5426", None))
        self.RGtypeBox.setItemText(1, QCoreApplication.translate("RegionGrowing", u"\u662f", None))

        self.affirmButton.setText(QCoreApplication.translate("RegionGrowing", u"\u786e\u5b9a", None))
    # retranslateUi

