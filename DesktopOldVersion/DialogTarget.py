# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DialogTarget.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_TargetDialog(object):
    def setupUi(self, TargetDialog):
        TargetDialog.setObjectName("TargetDialog")
        TargetDialog.resize(475, 300)
        self.widget = QtWidgets.QWidget(TargetDialog)
        self.widget.setGeometry(QtCore.QRect(80, 60, 302, 148))
        self.widget.setObjectName("widget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.lineEditSingle = QtWidgets.QLineEdit(self.widget)
        self.lineEditSingle.setObjectName("lineEditSingle")
        self.horizontalLayout.addWidget(self.lineEditSingle)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.pushButtonSingle = QtWidgets.QPushButton(self.widget)
        self.pushButtonSingle.setObjectName("pushButtonSingle")
        self.horizontalLayout_2.addWidget(self.pushButtonSingle)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.verticalLayout_3.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_3.addWidget(self.label_2)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem2)
        self.lineEditMultiple = QtWidgets.QLineEdit(self.widget)
        self.lineEditMultiple.setObjectName("lineEditMultiple")
        self.horizontalLayout_3.addWidget(self.lineEditMultiple)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem3)
        self.pushButtonMultiple = QtWidgets.QPushButton(self.widget)
        self.pushButtonMultiple.setObjectName("pushButtonMultiple")
        self.horizontalLayout_4.addWidget(self.pushButtonMultiple)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.verticalLayout_3.addLayout(self.verticalLayout_2)

        self.retranslateUi(TargetDialog)
        QtCore.QMetaObject.connectSlotsByName(TargetDialog)

    def retranslateUi(self, TargetDialog):
        _translate = QtCore.QCoreApplication.translate
        TargetDialog.setWindowTitle(_translate("TargetDialog", "Target"))
        self.label.setText(_translate("TargetDialog", " Single Target "))
        self.pushButtonSingle.setText(_translate("TargetDialog", "OK"))
        self.label_2.setText(_translate("TargetDialog", " MultipleTargets "))
        self.pushButtonMultiple.setText(_translate("TargetDialog", "OK"))



