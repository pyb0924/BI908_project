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


class Ui_Segmentation_Tool(object):
    def setupUi(self, Segmentation_Tool):
        if not Segmentation_Tool.objectName():
            Segmentation_Tool.setObjectName(u"Segmentation_Tool")
        Segmentation_Tool.resize(800, 620)
        Segmentation_Tool.setMinimumSize(QSize(800, 620))
        Segmentation_Tool.setMaximumSize(QSize(800, 620))
        self.actionOpen = QAction(Segmentation_Tool)
        self.actionOpen.setObjectName(u"actionOpen")
        self.actionSave = QAction(Segmentation_Tool)
        self.actionSave.setObjectName(u"actionSave")
        self.actionClose = QAction(Segmentation_Tool)
        self.actionClose.setObjectName(u"actionClose")
        self.actionNone = QAction(Segmentation_Tool)
        self.actionNone.setObjectName(u"actionNone")
        self.actionGuass_Filter = QAction(Segmentation_Tool)
        self.actionGuass_Filter.setObjectName(u"actionGuass_Filter")
        self.actionLoG_Filter = QAction(Segmentation_Tool)
        self.actionLoG_Filter.setObjectName(u"actionLoG_Filter")
        self.actionNoPre = QAction(Segmentation_Tool)
        self.actionNoPre.setObjectName(u"actionNoPre")
        self.actionLoG = QAction(Segmentation_Tool)
        self.actionLoG.setObjectName(u"actionLoG")
        self.actionOtsu = QAction(Segmentation_Tool)
        self.actionOtsu.setObjectName(u"actionOtsu")
        self.actionOtsuNew = QAction(Segmentation_Tool)
        self.actionOtsuNew.setObjectName(u"actionOtsuNew")
        self.actionRG = QAction(Segmentation_Tool)
        self.actionRG.setObjectName(u"actionRG")
        self.actionOpening = QAction(Segmentation_Tool)
        self.actionOpening.setObjectName(u"actionOpening")
        self.actionClosing = QAction(Segmentation_Tool)
        self.actionClosing.setObjectName(u"actionClosing")
        self.centralwidget = QWidget(Segmentation_Tool)
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

        self.preButton = QPushButton(self.layoutWidget)
        self.preButton.setObjectName(u"preButton")

        self.verticalLayout.addWidget(self.preButton)

        self.otsuButton = QPushButton(self.layoutWidget)
        self.otsuButton.setObjectName(u"otsuButton")

        self.verticalLayout.addWidget(self.otsuButton)

        self.rgButton = QPushButton(self.layoutWidget)
        self.rgButton.setObjectName(u"rgButton")

        self.verticalLayout.addWidget(self.rgButton)

        self.openingButton = QPushButton(self.layoutWidget)
        self.openingButton.setObjectName(u"openingButton")

        self.verticalLayout.addWidget(self.openingButton)

        self.closingButton = QPushButton(self.layoutWidget)
        self.closingButton.setObjectName(u"closingButton")

        self.verticalLayout.addWidget(self.closingButton)

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
        Segmentation_Tool.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(Segmentation_Tool)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 22))
        self.menu = QMenu(self.menubar)
        self.menu.setObjectName(u"menu")
        self.menuEdit = QMenu(self.menubar)
        self.menuEdit.setObjectName(u"menuEdit")
        self.menuPreprocessing = QMenu(self.menuEdit)
        self.menuPreprocessing.setObjectName(u"menuPreprocessing")
        self.menuSegmentation = QMenu(self.menuEdit)
        self.menuSegmentation.setObjectName(u"menuSegmentation")
        self.menuPostprocessing = QMenu(self.menuEdit)
        self.menuPostprocessing.setObjectName(u"menuPostprocessing")
        Segmentation_Tool.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(Segmentation_Tool)
        self.statusbar.setObjectName(u"statusbar")
        Segmentation_Tool.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menu.addAction(self.actionOpen)
        self.menu.addAction(self.actionSave)
        self.menu.addAction(self.actionClose)
        self.menuEdit.addAction(self.menuPreprocessing.menuAction())
        self.menuEdit.addAction(self.menuSegmentation.menuAction())
        self.menuEdit.addAction(self.menuPostprocessing.menuAction())
        self.menuPreprocessing.addAction(self.actionNoPre)
        self.menuPreprocessing.addAction(self.actionLoG)
        self.menuSegmentation.addAction(self.actionOtsu)
        self.menuSegmentation.addSeparator()
        self.menuSegmentation.addAction(self.actionRG)
        self.menuPostprocessing.addAction(self.actionOpening)
        self.menuPostprocessing.addAction(self.actionClosing)

        self.retranslateUi(Segmentation_Tool)

        QMetaObject.connectSlotsByName(Segmentation_Tool)
    # setupUi

    def retranslateUi(self, Segmentation_Tool):
        Segmentation_Tool.setWindowTitle(QCoreApplication.translate("Segmentation_Tool", u"MainWindow", None))
        self.actionOpen.setText(QCoreApplication.translate("Segmentation_Tool", u"Open", None))
        self.actionSave.setText(QCoreApplication.translate("Segmentation_Tool", u"Save", None))
        self.actionClose.setText(QCoreApplication.translate("Segmentation_Tool", u"Close", None))
        self.actionNone.setText(QCoreApplication.translate("Segmentation_Tool", u"None", None))
        self.actionGuass_Filter.setText(QCoreApplication.translate("Segmentation_Tool", u"Guass Filter", None))
        self.actionLoG_Filter.setText(QCoreApplication.translate("Segmentation_Tool", u"LoG Filter", None))
        self.actionNoPre.setText(QCoreApplication.translate("Segmentation_Tool", u"None", None))
        self.actionLoG.setText(QCoreApplication.translate("Segmentation_Tool", u"LoG Filter", None))
        self.actionOtsu.setText(QCoreApplication.translate("Segmentation_Tool", u"Otsu(Original)", None))
        self.actionOtsuNew.setText(QCoreApplication.translate("Segmentation_Tool", u"Otsu(New)", None))
        self.actionRG.setText(QCoreApplication.translate("Segmentation_Tool", u"Region Growing", None))
        self.actionOpening.setText(QCoreApplication.translate("Segmentation_Tool", u"Opening", None))
        self.actionClosing.setText(QCoreApplication.translate("Segmentation_Tool", u"Closing", None))
        self.graphicsLabel.setText("")
        self.newButton.setText(QCoreApplication.translate("Segmentation_Tool", u"Open", None))
        self.preButton.setText(QCoreApplication.translate("Segmentation_Tool", u"LoG Filter", None))
        self.otsuButton.setText(QCoreApplication.translate("Segmentation_Tool", u"Otsu", None))
        self.rgButton.setText(QCoreApplication.translate("Segmentation_Tool", u"Region Growing", None))
        self.openingButton.setText(QCoreApplication.translate("Segmentation_Tool", u"Opening", None))
        self.closingButton.setText(QCoreApplication.translate("Segmentation_Tool", u"Closing", None))
        self.saveButton.setText(QCoreApplication.translate("Segmentation_Tool", u"Save", None))
        self.exitButton.setText(QCoreApplication.translate("Segmentation_Tool", u"Close", None))
        self.menu.setTitle(QCoreApplication.translate("Segmentation_Tool", u"File", None))
        self.menuEdit.setTitle(QCoreApplication.translate("Segmentation_Tool", u"Edit", None))
        self.menuPreprocessing.setTitle(QCoreApplication.translate("Segmentation_Tool", u"Preprocessing", None))
        self.menuSegmentation.setTitle(QCoreApplication.translate("Segmentation_Tool", u"Segmentation", None))
        self.menuPostprocessing.setTitle(QCoreApplication.translate("Segmentation_Tool", u"Postprocessing", None))
    # retranslateUi

