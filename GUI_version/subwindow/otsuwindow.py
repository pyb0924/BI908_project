from ui.uiOtsu import Ui_Otsu
from PySide2 import QtWidgets
from PySide2.QtCore import Signal


class OtsuWindow(QtWidgets.QMainWindow, Ui_Otsu):
    signal = Signal(int)

    def __init__(self):
        super(OtsuWindow, self).__init__()
        self.setupUi(self)
        self.errorBox = QtWidgets.QMessageBox()
        self.affirmButton.clicked.connect(self.otsu_affirm)

    def otsu_affirm(self):
        bg_max = self.OtsuBGEdit.text()
        try:
            bg_max = int(bg_max)
        except ValueError:
            self.errorBox.critical(self, 'Error', '输入错误！请输入一个数字')
        else:
            if bg_max < 0:
                self.errorBox.critical(self, 'Error', '输入错误！请输入一个非负整数')
            else:
                self.close()
                self.signal.emit(bg_max)
