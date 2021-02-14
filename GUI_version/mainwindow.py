from ui.uiSegTool import Ui_Segmentation_Tool
from PySide2 import QtWidgets
from PySide2.QtGui import QPixmap, QImage
from subwindow.otsuwindow import OtsuWindow
from subwindow.rgwindow import RGWindow
from subwindow.ocwindow import OCWindow
from subwindow.validwindow import ValidWindow
from utils import *
from otsu import otsu2Threshold
from region_growing import region_growing
from PySide2.QtCore import Signal, QThread


class MainWindow(QtWidgets.QMainWindow, Ui_Segmentation_Tool):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.oc_window = OCWindow()
        self.otsu_window = OtsuWindow()
        self.rg_window = RGWindow()
        self.valid_window = ValidWindow()
        self.filedialog = QtWidgets.QFileDialog()
        self.errorBox = QtWidgets.QMessageBox()
        self.workThread = WorkThread()
        self.img = None

        # subwindow/thread signal-slot
        self.otsu_window.signal.connect(self.returnOtsu)
        self.workThread.signal.connect(self.returnWork)

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
        self.ocButton.clicked.connect(self.beginOC)
        self.validButton.clicked.connect(self.beginValid)
        self.saveButton.clicked.connect(self.save_img)
        self.exitButton.clicked.connect(self.close)
        self.graphicsScroll.sliderMoved.connect(self.show_img)

    # tools
    def setAllButtons(self, flag):
        button_list = ['new', 'otsu', 'rg', 'valid', 'save']
        for button_name in button_list:
            button = getattr(self, button_name + 'Button')
            button.setEnabled(flag)

    # callback
    def returnWork(self, img, t1, t2):
        self.img = img
        if t1 >= 0:
            otsu_result = 'Otsu算法完成：t1={},t2={}'.format(t1, t2)
            self.statusbar.showMessage(otsu_result)
            self.setAllButtons(True)
        else:
            pass  # TODO after rg
        self.show_img()

    def beginOtsu(self):
        self.otsu_window.show()

    def returnOtsu(self, num):
        self.statusbar.showMessage('正在进行：Otsu算法……')
        self.workThread.set_prams('otsu2Threshold', self.img, num)
        self.workThread.start()
        self.setAllButtons(False)

    def beginRG(self):
        self.rg_window.show()

    def beginOC(self):
        self.oc_window.show()

    def beginValid(self):
        self.valid_window.validThread.img = self.img
        self.valid_window.show()

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
        if self.img is None:
            self.errorBox.critical(self, 'Error', "当前没有已打开的文件!")
            return
        depth = self.graphicsScroll.value()
        image = self.img[:, :, depth]
        image = (image / np.max(self.img) * 255).astype('uint8')
        image = QImage(image, image.shape[1], image.shape[0], image.shape[1], QImage.Format_Grayscale8)
        img_pix = QPixmap(image).scaled(self.graphicsLabel.width(), self.graphicsLabel.height())
        self.graphicsLabel.setPixmap(img_pix)

    def save_img(self):
        if self.img is None:
            self.errorBox.critical(self, 'Error', "当前没有已打开的文件!")
            return

        filepath, filetype = self.filedialog.getSaveFileName(
            self, '保存文件', r'./', "图片类型(*.nii.gz)"
        )
        if filepath:
            write_img(self.img, filepath)
            self.statusbar.showMessage("文件保存成功")
        else:
            self.statusbar.showMessage("文件保存失败")


class WorkThread(QThread):
    signal = Signal(np.ndarray, int, int)

    def __init__(self):
        super(WorkThread, self).__init__()
        self.method = None
        self.params = None

    def set_prams(self, method, *args):
        self.method = method
        self.params = args

    def run(self) -> None:
        result = eval(self.method)(*self.params)
        if len(result) == 1:
            result = (result, -1, -1)
        self.signal.emit(*result)
