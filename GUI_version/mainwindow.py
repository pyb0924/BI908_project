from ui.uiSegTool import Ui_SegTool
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


class MainWindow(QtWidgets.QMainWindow, Ui_SegTool):
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

        # subWindow/thread signal-slot
        self.otsu_window.signal.connect(self.returnOtsu)
        self.workThread.signal.connect(self.returnWork)
        self.oc_window.signal.connect(self.returnOC)
        self.rg_window.signal.connect(self.returnRG)

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
        self.graphicsScroll.valueChanged.connect(self.show_img)
        self.graphicsScroll.sliderMoved.connect(self.show_img)

    # tools
    def setAllButtons(self, flag):
        button_list = ['new', 'otsu', 'rg', 'oc', 'valid', 'save']
        for button_name in button_list:
            button = getattr(self, button_name + 'Button')
            button.setEnabled(flag)

    def returnWork(self, img, cal_type, thresh):
        self.img = img
        method_dict = {1: 'Otsu', 2: 'Region Growing', 3: 'Opening', 4: 'Closing'}
        if cal_type == 1:
            message = '{}完成：t1={},t2={}'.format(method_dict[cal_type], *thresh)
        else:
            message = '{}完成'.format(method_dict[cal_type])
        self.statusbar.showMessage(message)
        self.setAllButtons(True)
        self.show_img()

    # callback
    def beginOtsu(self):
        if self.img is None:
            self.errorBox.critical(self, 'Error', "当前没有已打开的文件!")
            return
        self.otsu_window.show()

    def returnOtsu(self, num):
        self.statusbar.showMessage('正在进行：Otsu算法……')
        self.workThread.set_prams(otsu2Threshold, self.img, num)
        self.workThread.start()
        self.setAllButtons(False)

    def beginRG(self):
        if self.img is None:
            self.errorBox.critical(self, 'Error', "当前没有已打开的文件!")
            return
        self.rg_window.show()

    def returnRG(self, radius, threshold, seed, abs_flag, iter_max):
        self.statusbar.showMessage('正在进行：Region Growing……')
        self.workThread.set_prams(region_growing, self.img, radius, threshold, seed, abs_flag, iter_max)
        self.workThread.start()
        self.setAllButtons(False)

    def beginOC(self):
        if self.img is None:
            self.errorBox.critical(self, 'Error', "当前没有已打开的文件!")
            return
        self.oc_window.show()

    def returnOC(self, flag, radius):
        oc_type = opening if flag else closing
        message = '正在进行：{}运算，radius={}'.format(oc_type.__name__, radius)
        self.statusbar.showMessage(message)
        self.workThread.set_prams(oc_type, self.img, radius)
        self.workThread.start()
        self.setAllButtons(False)

    def beginValid(self):
        if self.img is None:
            self.errorBox.critical(self, 'Error', "当前没有已打开的文件!")
            return
        self.valid_window.validThread.img = self.img
        self.valid_window.show()

    def open_img(self):
        self.statusbar.showMessage('正在打开文件……')

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
    signal = Signal(np.ndarray, int, tuple)  # 1:Otsu 2:RG 3:Opening 4:Closing

    def __init__(self):
        super(WorkThread, self).__init__()
        self.method = None
        self.params = None

    def set_prams(self, method, *args):
        self.method = method
        self.params = args

    def run(self) -> None:
        result = self.method(*self.params)
        method_dict = {otsu2Threshold: 1, region_growing: 2, opening: 3, closing: 4}
        if self.method is otsu2Threshold:
            result = (result[0], 1, (result[1], result[2]))
        else:
            result = (result, method_dict[self.method], ())
        self.signal.emit(*result)
