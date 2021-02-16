from ui.uiRG import Ui_RegionGrowing
from PySide2 import QtWidgets
from PySide2.QtCore import Signal


class RGWindow(QtWidgets.QMainWindow, Ui_RegionGrowing):
    signal = Signal(int, int, tuple, bool, int)  # radius, threshold, seed, abs_flag, tail_max

    def __init__(self):
        super(RGWindow, self).__init__()
        self.setupUi(self)
        self.errorBox = QtWidgets.QMessageBox()
        self.affirmButton.clicked.connect(self.rg_affirm)

    def rg_affirm(self):
        try:
            radius = self.RGradiusBox.value()
            assert radius > 0
            thresh = self.RGtBox.value()
            assert thresh > 0
            seed = tuple(int(x) for x in self.RGseedEdit.text().split(','))
            assert len(seed) == 3
            iter_max = int(self.RGitermaxEdit.text())
            abs_flag = True if self.RGtypeBox.currentText() == '是' else False
        except (ValueError, AssertionError):
            self.errorBox.critical(self, 'Error', "参数输入错误!")
        else:
            self.signal.emit(radius, thresh, seed, abs_flag, iter_max)
            self.close()
