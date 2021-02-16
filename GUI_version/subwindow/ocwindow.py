from ui.uiOC import Ui_OC
from PySide2 import QtWidgets
from PySide2.QtCore import Signal


class OCWindow(QtWidgets.QMainWindow, Ui_OC):
    signal = Signal(bool, int)

    def __init__(self):
        super(OCWindow, self).__init__()
        self.setupUi(self)
        self.openingButton.setChecked(True)
        self.radiusBox.setValue(1)
        self.affirmButton.clicked.connect(self.affirm)

    def affirm(self):
        radius = self.radiusBox.value()
        if radius > 0:
            self.signal.emit(self.openingButton.isChecked(), radius)
            self.close()
