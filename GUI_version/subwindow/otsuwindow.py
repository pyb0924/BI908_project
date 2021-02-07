from ui.uiOtsu import Ui_Otsu
from PySide2 import QtWidgets


class OtsuWindow(QtWidgets.QMainWindow, Ui_Otsu):
    def __init__(self):
        super(OtsuWindow, self).__init__()
        self.setupUi(self)

        self.pushButton.clicked.connect(self.affirm)

    def affirm(self):
        self.close()

