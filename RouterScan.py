from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import router_scan_main

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = router_scan_main.Ui_RouterScanMain()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
