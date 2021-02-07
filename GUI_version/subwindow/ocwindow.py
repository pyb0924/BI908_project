from ui.uiOC import Ui_Opening_Closing
from PySide2 import QtWidgets


class OCWindow(QtWidgets.QMainWindow, Ui_Opening_Closing):
    def __init__(self):
        super(OCWindow, self).__init__()
        self.setupUi(self)

        self.affirmButton.clicked.connect(self.affirm)

    def affirm(self):
        self.close()
