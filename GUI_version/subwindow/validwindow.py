from ui.uiValid import Ui_Validation
from PySide2 import QtWidgets
from PySide2.QtCore import QThread, Signal
from utils import *
from validation import *


class ValidWindow(QtWidgets.QMainWindow, Ui_Validation):
    def __init__(self):
        super(ValidWindow, self).__init__()
        self.setupUi(self)
        self.filedialog = QtWidgets.QFileDialog()
        self.openButton.clicked.connect(self.open_label)
        self.closeButton.clicked.connect(self.close)
        self.saveButton.clicked.connect(self.saveValid)
        self.errorBox = QtWidgets.QMessageBox()
        self.validThread = ValidThread()
        self.filepath = None

        self.validThread.signal.connect(self.show_valid)

    def open_label(self):
        self.filepath, filetype = self.filedialog.getOpenFileName(
            self, '选择分割正确标签 *.nii.gz',
            r'./', "图片类型(*.nii.gz)"
        )
        if self.filepath:
            self.validThread.label = read_img(self.filepath)
            self.statusbar.showMessage('文件读取完毕')
            self.openButton.setEnabled(False)
            self.saveButton.setEnabled(False)
            self.validThread.start()
            self.statusbar.showMessage('正在计算评价指标……')

    def show_valid(self, cm):
        self.saveButton.setEnabled(True)
        self.openButton.setEnabled(True)
        self.senEdit.setText(str(get_sensitivity(cm)))
        self.preEdit.setText(str(get_precision(cm)))
        self.accEdit.setText(str(get_accuracy(cm)))
        self.iouEdit.setText(str(get_iou(cm)))
        self.diceEdit.setText(str(get_dice(cm)))
        self.statusbar.showMessage('评价指标计算完毕')

    def saveValid(self):
        if self.filepath:
            valid_list = ['sen', 'pre', 'acc', 'iou', 'dice']
            result = {'sample_name': self.filepath}
            for valid in valid_list:
                edit_name = getattr(self, valid + 'Edit')
                number = float(edit_name.text())
                result[valid] = number
            write_result(result, 'result.log')
            self.statusbar.showMessage('评价指标已保存')
        else:
            self.errorBox.critical(self, 'Error', '当前没有已经打开的标签！')


class ValidThread(QThread):
    signal = Signal(np.ndarray)

    def __init__(self):
        super(ValidThread, self).__init__()
        self.img = None
        self.label = None

    def run(self) -> None:
        cm = cal_cm(self.img, self.label)
        self.signal.emit(cm)
