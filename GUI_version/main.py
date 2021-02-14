from mainwindow import MainWindow
import sys
from PySide2 import QtWidgets

if __name__ == '__main__':
    app = QtWidgets.QApplication()
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
