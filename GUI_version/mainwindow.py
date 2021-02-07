from ui.uiSegTool import Ui_Segmentation_Tool
from PySide2 import QtWidgets
from PySide2.QtGui import QPixmap, QImage
from subwindow.otsuwindow import OtsuWindow
from subwindow.rgwindow import RGWindow
from subwindow.ocwindow import OCWindow
from utils import *


class MainWindow(QtWidgets.QMainWindow, Ui_Segmentation_Tool):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.oc_window = OCWindow()
        self.otsu_window = OtsuWindow()
        self.rg_window = RGWindow()
        self.filedialog = QtWidgets.QFileDialog()
        self.img = None

        # menu action
        self.actionOpen.triggered.connect(self.open_img)
        self.actionSave.triggered.connect(self.save_img)
        self.actionClose.triggered.connect(self.close)
        self.actionOtsu.triggered.connect(self.beginOtsu)
        self.actionRG.triggered.connect(self.beginRG)

        # button & scroll
        self.newButton.clicked.connect(self.open_img)
        self.otsuButton.clicked.connect(self.beginOtsu)
        self.rgButton.clicked.connect(self.beginRG)
        self.saveButton.clicked.connect(self.save_img)
        self.exitButton.clicked.connect(self.close)
        self.graphicsScroll.sliderMoved.connect(self.show_img)

    # callback

    def beginOtsu(self):
        self.otsu_window.show()

    def beginRG(self):
        self.rg_window.show()

    def beginOC(self):
        self.oc_window.show()

    def open_img(self):
        self.statusbar.showMessage('打开文件')

        filepath, filetype = self.filedialog.getOpenFileName(
            self, '选择要处理的图片 *.nii.gz',
            r'./', "图片类型(*.nii.gz)"
        )
        if filepath:
            self.img = read_img(filepath)
            self.graphicsScroll.setMaximum(self.img.shape[2] - 1)
            self.show_img()
            self.statusbar.showMessage('文件打开成功')
        else:
            self.statusbar.showMessage('文件打开失败')

    def show_img(self):
        depth = self.graphicsScroll.value()
        image = self.img[:, :, depth]
        image = (image / np.max(image) * 255).astype('uint8')
        image = QImage(image, image.shape[1], image.shape[0], image.shape[1], QImage.Format_Grayscale8)
        img_pix = QPixmap(image).scaled(self.graphicsLabel.width(), self.graphicsLabel.height())
        self.graphicsLabel.setPixmap(img_pix)

    def save_img(self):
        if self.img is None:
            self.statusbar.showMessage("当前没有已打开的文件!")
            return

        filepath, filetype = self.filedialog.getSaveFileName(
            self, '保存文件', r'./', "图片类型(*.nii.gz)"
        )
        if filepath:
            write_img(self.img, filepath)
            self.statusbar.showMessage("文件保存成功")
        else:
            self.statusbar.showMessage("文件保存失败")
