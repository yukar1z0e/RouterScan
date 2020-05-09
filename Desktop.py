import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from Desktop.MainWindowRouterScan import Ui_RouterScanMainWindow, RouterScanMainWindow
import qtawesome


class RouterScan:

    def __init__(self):
        global APP
        APP = self
        self.app = QtWidgets.QApplication(sys.argv)
        self.ui = Ui_RouterScanMainWindow()
        self.window = RouterScanMainWindow(self)
        self.window.setWindowIcon(QtGui.QIcon('router.png'))
        self.ui.setupUi(self.window)
        self.setupAction()
        self.window.show()
        sys.exit(self.app.exec_())

    def setupAction(self):
        self.ui.actionExploitCVE_2018_14847.triggered.connect(self.window.show_DialogTarget)
        self.ui.actionVPNCVE_2018_14847.triggered.connect(self.window.show_DialogTarget)


if __name__ == '__main__':
    RouterScan()
