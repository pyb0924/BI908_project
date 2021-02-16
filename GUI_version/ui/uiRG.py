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
        self.layoutWidget = QWidget(RegionGrowing)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(10, 20, 441, 271))
        self.verticalLayout_3 = QVBoxLayout(self.layoutWidget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.OtsuBGlabel = QLabel(self.layoutWidget)
        self.OtsuBGlabel.setObjectName(u"OtsuBGlabel")

        self.verticalLayout_2.addWidget(self.OtsuBGlabel)

        self.OtsuBGlabel_2 = QLabel(self.layoutWidget)
        self.OtsuBGlabel_2.setObjectName(u"OtsuBGlabel_2")

        self.verticalLayout_2.addWidget(self.OtsuBGlabel_2)

        self.OtsuBGlabel_3 = QLabel(self.layoutWidget)
        self.OtsuBGlabel_3.setObjectName(u"OtsuBGlabel_3")

        self.verticalLayout_2.addWidget(self.OtsuBGlabel_3)

        self.OtsuBGlabel_5 = QLabel(self.layoutWidget)
        self.OtsuBGlabel_5.setObjectName(u"OtsuBGlabel_5")

        self.verticalLayout_2.addWidget(self.OtsuBGlabel_5)

        self.OtsuBGlabel_4 = QLabel(self.layoutWidget)
        self.OtsuBGlabel_4.setObjectName(u"OtsuBGlabel_4")

        self.verticalLayout_2.addWidget(self.OtsuBGlabel_4)


        self.horizontalLayout.addLayout(self.verticalLayout_2)

        self.horizontalSpacer = QSpacerItem(80, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(15)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.RGtBox = QSpinBox(self.layoutWidget)
        self.RGtBox.setObjectName(u"RGtBox")
        self.RGtBox.setMinimum(1)

        self.verticalLayout.addWidget(self.RGtBox)

        self.RGradiusBox = QSpinBox(self.layoutWidget)
        self.RGradiusBox.setObjectName(u"RGradiusBox")
        self.RGradiusBox.setMinimum(1)

        self.verticalLayout.addWidget(self.RGradiusBox)

        self.RGitermaxEdit = QLineEdit(self.layoutWidget)
        self.RGitermaxEdit.setObjectName(u"RGitermaxEdit")

        self.verticalLayout.addWidget(self.RGitermaxEdit)

        self.RGseedEdit = QLineEdit(self.layoutWidget)
        self.RGseedEdit.setObjectName(u"RGseedEdit")

        self.verticalLayout.addWidget(self.RGseedEdit)

        self.RGtypeBox = QComboBox(self.layoutWidget)
        self.RGtypeBox.addItem("")
        self.RGtypeBox.addItem("")
        self.RGtypeBox.setObjectName(u"RGtypeBox")

        self.verticalLayout.addWidget(self.RGtypeBox)


        self.horizontalLayout.addLayout(self.verticalLayout)

        self.horizontalLayout.setStretch(0, 4)
        self.horizontalLayout.setStretch(1, 1)
        self.horizontalLayout.setStretch(2, 4)

        self.verticalLayout_3.addLayout(self.horizontalLayout)

        self.affirmButton = QPushButton(self.layoutWidget)
        self.affirmButton.setObjectName(u"affirmButton")

        self.verticalLayout_3.addWidget(self.affirmButton)


        self.retranslateUi(RegionGrowing)

        QMetaObject.connectSlotsByName(RegionGrowing)
    # setupUi

    def retranslateUi(self, RegionGrowing):
        RegionGrowing.setWindowTitle(QCoreApplication.translate("RegionGrowing", u"Region Growing", None))
        self.OtsuBGlabel.setText(QCoreApplication.translate("RegionGrowing", u"\u90bb\u57df\u9608\u503c", None))
        self.OtsuBGlabel_2.setText(QCoreApplication.translate("RegionGrowing", u"\u90bb\u57df\u534a\u5f84", None))
        self.OtsuBGlabel_3.setText(QCoreApplication.translate("RegionGrowing", u"\u8fed\u4ee3\u6b21\u6570\u4e0a\u9650", None))
        self.OtsuBGlabel_5.setText(QCoreApplication.translate("RegionGrowing", u"\u79cd\u5b50\u70b9\u4f4d\u7f6e", None))
        self.OtsuBGlabel_4.setText(QCoreApplication.translate("RegionGrowing", u"\u53bb\u7edd\u5bf9\u503c\u5904\u7406", None))
        self.RGitermaxEdit.setText("")
        self.RGitermaxEdit.setPlaceholderText("")
        self.RGseedEdit.setPlaceholderText(QCoreApplication.translate("RegionGrowing", u"\u4e09\u7ef4\u5750\u6807\uff0c\u4ee5\u9017\u53f7\u5206\u9694", None))
        self.RGtypeBox.setItemText(0, QCoreApplication.translate("RegionGrowing", u"\u5426", None))
        self.RGtypeBox.setItemText(1, QCoreApplication.translate("RegionGrowing", u"\u662f", None))

        self.affirmButton.setText(QCoreApplication.translate("RegionGrowing", u"\u786e\u5b9a", None))
    # retranslateUi

