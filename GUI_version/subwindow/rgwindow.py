from ui.uiRG import Ui_RegionGrowing
from PySide2 import QtWidgets


class RGWindow(QtWidgets.QMainWindow, Ui_RegionGrowing):
    def __init__(self):
        super(RGWindow, self).__init__()
        self.setupUi(self)

        self.affirmButton.clicked.connect(self.affirm)

    def affirm(self):
        self.close()
