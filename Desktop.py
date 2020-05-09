import sys
from PyQt5 import QtCore, QtGui, QtWidgets

from Desktop.DialogTarget import Ui_TargetDialog
from Desktop.MainWindowRouterScan import Ui_RouterScanMainWindow
import qtawesome

APP=None

class RouterScanMainWindow(QtWidgets.QMainWindow):
    app = None

    def __init__(self, app):
        super(RouterScanMainWindow, self).__init__()
        self.app = app

    def show_DialogTarget(self):
        dialog_target = QtWidgets.QDialog()
        ui = Ui_TargetDialog()
        ui.setupUi(dialog_target)
        dialog_target.show()
        dialog_target.exec_()


class TargetDialog(QtWidgets.QDialog):
    data=None
    def __init__(self,data):
        super(TargetDialog,self).__init__(APP.window)
        self.data=data


class RouterScan:

    def __init__(self):
        global APP
        APP = self
        self.app = QtWidgets.QApplication(sys.argv)
        self.ui = Ui_RouterScanMainWindow()
        self.window = RouterScanMainWindow(self)
        self.window.setWindowIcon(QtGui.QIcon(qtawesome.icon('fa5s.network-wired')))
        self.ui.setupUi(self.window)
        self.setupAction()
        self.window.show()
        sys.exit(self.app.exec_())

    def setupAction(self):
        self.ui.actionExploitCVE_2018_14847.triggered.connect(self.window.show_DialogTarget)
        self.ui.actionVPNCVE_2018_14847.triggered.connect(self.window.show_DialogTarget)


if __name__ == '__main__':
    RouterScan()
