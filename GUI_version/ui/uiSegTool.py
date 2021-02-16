# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'uiSegTool.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_SegTool(object):
    def setupUi(self, SegTool):
        if not SegTool.objectName():
            SegTool.setObjectName(u"SegTool")
        SegTool.resize(800, 620)
        SegTool.setMinimumSize(QSize(800, 620))
        SegTool.setMaximumSize(QSize(800, 620))
        self.actionOpen = QAction(SegTool)
        self.actionOpen.setObjectName(u"actionOpen")
        self.actionSave = QAction(SegTool)
        self.actionSave.setObjectName(u"actionSave")
        self.actionClose = QAction(SegTool)
        self.actionClose.setObjectName(u"actionClose")
        self.actionNone = QAction(SegTool)
        self.actionNone.setObjectName(u"actionNone")
        self.actionGuass_Filter = QAction(SegTool)
        self.actionGuass_Filter.setObjectName(u"actionGuass_Filter")
        self.actionLoG_Filter = QAction(SegTool)
        self.actionLoG_Filter.setObjectName(u"actionLoG_Filter")
        self.actionNoPre = QAction(SegTool)
        self.actionNoPre.setObjectName(u"actionNoPre")
        self.actionLoG = QAction(SegTool)
        self.actionLoG.setObjectName(u"actionLoG")
        self.actionOtsu = QAction(SegTool)
        self.actionOtsu.setObjectName(u"actionOtsu")
        self.actionOtsuNew = QAction(SegTool)
        self.actionOtsuNew.setObjectName(u"actionOtsuNew")
        self.actionRG = QAction(SegTool)
        self.actionRG.setObjectName(u"actionRG")
        self.actionOpening = QAction(SegTool)
        self.actionOpening.setObjectName(u"actionOpening")
        self.actionClosing = QAction(SegTool)
        self.actionClosing.setObjectName(u"actionClosing")
        self.centralwidget = QWidget(SegTool)
        self.centralwidget.setObjectName(u"centralwidget")
        self.layoutWidget = QWidget(self.centralwidget)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(20, 10, 741, 531))
        self.horizontalLayout = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setSizeConstraint(QLayout.SetNoConstraint)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.graphicsLabel = QLabel(self.layoutWidget)
        self.graphicsLabel.setObjectName(u"graphicsLabel")

        self.horizontalLayout.addWidget(self.graphicsLabel)

        self.graphicsScroll = QScrollBar(self.layoutWidget)
        self.graphicsScroll.setObjectName(u"graphicsScroll")
        self.graphicsScroll.setOrientation(Qt.Vertical)

        self.horizontalLayout.addWidget(self.graphicsScroll)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(4)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.newButton = QPushButton(self.layoutWidget)
        self.newButton.setObjectName(u"newButton")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.newButton.sizePolicy().hasHeightForWidth())
        self.newButton.setSizePolicy(sizePolicy)

        self.verticalLayout.addWidget(self.newButton)

        self.otsuButton = QPushButton(self.layoutWidget)
        self.otsuButton.setObjectName(u"otsuButton")

        self.verticalLayout.addWidget(self.otsuButton)

        self.rgButton = QPushButton(self.layoutWidget)
        self.rgButton.setObjectName(u"rgButton")

        self.verticalLayout.addWidget(self.rgButton)

        self.ocButton = QPushButton(self.layoutWidget)
        self.ocButton.setObjectName(u"ocButton")

        self.verticalLayout.addWidget(self.ocButton)

        self.validButton = QPushButton(self.layoutWidget)
        self.validButton.setObjectName(u"validButton")

        self.verticalLayout.addWidget(self.validButton)

        self.saveButton = QPushButton(self.layoutWidget)
        self.saveButton.setObjectName(u"saveButton")

        self.verticalLayout.addWidget(self.saveButton)

        self.exitButton = QPushButton(self.layoutWidget)
        self.exitButton.setObjectName(u"exitButton")

        self.verticalLayout.addWidget(self.exitButton)


        self.horizontalLayout.addLayout(self.verticalLayout)

        self.horizontalLayout.setStretch(0, 5)
        self.horizontalLayout.setStretch(1, 1)
        self.horizontalLayout.setStretch(2, 2)
        SegTool.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(SegTool)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 22))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        self.menuEdit = QMenu(self.menubar)
        self.menuEdit.setObjectName(u"menuEdit")
        SegTool.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(SegTool)
        self.statusbar.setObjectName(u"statusbar")
        SegTool.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionClose)
        self.menuEdit.addAction(self.actionOtsu)
        self.menuEdit.addAction(self.actionRG)
        self.menuEdit.addAction(self.actionOpening)

        self.retranslateUi(SegTool)

        QMetaObject.connectSlotsByName(SegTool)
    # setupUi

    def retranslateUi(self, SegTool):
        SegTool.setWindowTitle(QCoreApplication.translate("SegTool", u"SegTool", None))
        self.actionOpen.setText(QCoreApplication.translate("SegTool", u"Open", None))
        self.actionSave.setText(QCoreApplication.translate("SegTool", u"Save", None))
        self.actionClose.setText(QCoreApplication.translate("SegTool", u"Close", None))
        self.actionNone.setText(QCoreApplication.translate("SegTool", u"None", None))
        self.actionGuass_Filter.setText(QCoreApplication.translate("SegTool", u"Guass Filter", None))
        self.actionLoG_Filter.setText(QCoreApplication.translate("SegTool", u"LoG Filter", None))
        self.actionNoPre.setText(QCoreApplication.translate("SegTool", u"None", None))
        self.actionLoG.setText(QCoreApplication.translate("SegTool", u"LoG Filter", None))
        self.actionOtsu.setText(QCoreApplication.translate("SegTool", u"Otsu", None))
        self.actionOtsuNew.setText(QCoreApplication.translate("SegTool", u"Otsu(New)", None))
        self.actionRG.setText(QCoreApplication.translate("SegTool", u"Region Growing", None))
        self.actionOpening.setText(QCoreApplication.translate("SegTool", u"Opening/Closing", None))
        self.actionClosing.setText(QCoreApplication.translate("SegTool", u"Closing", None))
        self.graphicsLabel.setText("")
        self.newButton.setText(QCoreApplication.translate("SegTool", u"Open", None))
        self.otsuButton.setText(QCoreApplication.translate("SegTool", u"Otsu", None))
        self.rgButton.setText(QCoreApplication.translate("SegTool", u"Region Growing", None))
        self.ocButton.setText(QCoreApplication.translate("SegTool", u"Opening/Closing", None))
        self.validButton.setText(QCoreApplication.translate("SegTool", u"Result Validation", None))
        self.saveButton.setText(QCoreApplication.translate("SegTool", u"Save", None))
        self.exitButton.setText(QCoreApplication.translate("SegTool", u"Close", None))
        self.menuFile.setTitle(QCoreApplication.translate("SegTool", u"File", None))
        self.menuEdit.setTitle(QCoreApplication.translate("SegTool", u"Edit", None))
    # retranslateUi

