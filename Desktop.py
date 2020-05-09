import sys
from PyQt5 import QtCore, QtGui, QtWidgets

from Desktop.DialogTarget import Ui_TargetDialog
from Desktop.MainWindowRouterScan import Ui_RouterScanMainWindow
from MikroTik.cve_2018_14847.get_targets import format_file,format_single_ip
from MikroTik.cve_2018_14847.exploit import exploit
from MikroTik.cve_2018_14847.create_vpn import vpn

# APP = None


class RouterScanMainWindow(QtWidgets.QMainWindow):
    app = None

    def __init__(self, app):
        super(RouterScanMainWindow, self).__init__()
        self.app = app

    def show_DialogTargetCVE_2018_14847EXP(self):
        data = []
        dialog_target = TargetDialog(data,title='CVE_2018_14847@EXP')
        # ui = Ui_TargetDialog()
        # ui.setupUi(dialog_target)
        dialog_target.setupAction()
        dialog_target.show()
        dialog_target.exec_()

    def show_DialogTargetCVE_2018_14847VPN(self):
        data = []
        dialog_target = TargetDialog(data, title='CVE_2018_14847@VPN')
        # ui = Ui_TargetDialog()
        # ui.setupUi(dialog_target)
        dialog_target.setupAction()
        dialog_target.show()
        dialog_target.exec_()


class TargetDialog(QtWidgets.QDialog):
    data = None

    def __init__(self, data,title):
        super(TargetDialog, self).__init__(APP.window)
        self.data = data
        self.title=title
        self.ui = Ui_TargetDialog()
        self.ui.setupUi(self)

    def setupAction(self):
        self.ui.pushButtonSingle.clicked.connect(self.addSingle)
        self.ui.pushButtonMultiple.clicked.connect(self.addMultiple)

    def addSingle(self):
        ip = self.ui.lineEditSingle.text()
        CVE,FUN=self.title.split('@')
        print(CVE,FUN)
        print(type(CVE),type(FUN))
        print(self)
        if ip:
            self.data = ''
            if ip in self.data:
                print('[*] INFO: {} is already exits'.format(ip))
                return
            self.data = ip
            target=format_single_ip(ip)
            print(target)
            for item in target:
                APP.ui.textBrowserTarget.append(str(item[0])+':'+str(item[1]))
            if FUN=='EXP':
                output=exploit(target)
                print('OUTPUT',output)
            elif FUN=='VPN':
                output=vpn(target)
                print('OUTPUT',output)

        print(self.data)
        print(type(self.data))

    def addMultiple(self):
        filename = self.ui.lineEditMultiple.text()
        CVE, FUN = self.title.split('@')
        print(CVE, FUN)
        print(type(CVE), type(FUN))
        if filename:
            self.data = ''
            if filename == self.data:
                print('[*] INFO: {} is already exits'.format(filename))
                return
            self.data = filename
            target=format_file(self.data)
            for item in target:
                APP.ui.textBrowserTarget.append(str(item[0]) + ':' + str(item[1]))
            if FUN=='EXP':
                output=exploit(target)
                print('OUTPUT',output)
            elif FUN=='VPN':
                output=vpn(target)
                print('OUTPUT',output)

        print(self.data)
        print(type(self.data))


class RouterScan:

    def __init__(self):
        global APP
        APP = self
        self.app = QtWidgets.QApplication(sys.argv)
        self.ui = Ui_RouterScanMainWindow()
        self.window = RouterScanMainWindow(self)
        self.ui.setupUi(self.window)
        self.setupAction()
        self.window.show()
        sys.exit(self.app.exec_())

    def setupAction(self):
        self.ui.actionExploitCVE_2018_14847.triggered.connect(self.window.show_DialogTargetCVE_2018_14847EXP)
        self.ui.actionVPNCVE_2018_14847.triggered.connect(self.window.show_DialogTargetCVE_2018_14847VPN)


if __name__ == '__main__':
    RouterScan()
