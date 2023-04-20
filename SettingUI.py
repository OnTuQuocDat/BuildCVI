# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'SettingUI.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_SettingWindow(object):
    def setupUi(self, SettingWindow):
        SettingWindow.setObjectName("SettingWindow")
        SettingWindow.resize(647, 486)
        self.centralwidget = QtWidgets.QWidget(SettingWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.layoutSU60_L = QtWidgets.QLineEdit(self.centralwidget)
        self.layoutSU60_L.setGeometry(QtCore.QRect(180, 60, 351, 22))
        self.layoutSU60_L.setObjectName("layoutSU60_L")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 60, 131, 16))
        self.label.setObjectName("label")
        self.layoutSU60_R = QtWidgets.QLineEdit(self.centralwidget)
        self.layoutSU60_R.setGeometry(QtCore.QRect(180, 110, 351, 22))
        self.layoutSU60_R.setText("")
        self.layoutSU60_R.setObjectName("layoutSU60_R")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 110, 131, 16))
        self.label_2.setObjectName("label_2")
        self.layoutSU85_L = QtWidgets.QLineEdit(self.centralwidget)
        self.layoutSU85_L.setGeometry(QtCore.QRect(180, 160, 351, 22))
        self.layoutSU85_L.setText("")
        self.layoutSU85_L.setObjectName("layoutSU85_L")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(20, 160, 131, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(20, 210, 131, 16))
        self.label_4.setObjectName("label_4")
        self.layoutSU85_R = QtWidgets.QLineEdit(self.centralwidget)
        self.layoutSU85_R.setGeometry(QtCore.QRect(180, 210, 351, 22))
        self.layoutSU85_R.setText("")
        self.layoutSU85_R.setObjectName("layoutSU85_R")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(20, 260, 131, 16))
        self.label_5.setObjectName("label_5")
        self.layoutSU100_L = QtWidgets.QLineEdit(self.centralwidget)
        self.layoutSU100_L.setGeometry(QtCore.QRect(180, 260, 351, 22))
        self.layoutSU100_L.setText("")
        self.layoutSU100_L.setObjectName("layoutSU100_L")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(20, 310, 141, 16))
        self.label_6.setObjectName("label_6")
        self.layoutSU100_R = QtWidgets.QLineEdit(self.centralwidget)
        self.layoutSU100_R.setGeometry(QtCore.QRect(180, 310, 351, 22))
        self.layoutSU100_R.setText("")
        self.layoutSU100_R.setObjectName("layoutSU100_R")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(20, 360, 131, 16))
        self.label_7.setObjectName("label_7")
        self.serialgamma_file = QtWidgets.QLineEdit(self.centralwidget)
        self.serialgamma_file.setGeometry(QtCore.QRect(180, 360, 351, 22))
        self.serialgamma_file.setText("")
        self.serialgamma_file.setObjectName("serialgamma_file")
        self.save_button = QtWidgets.QPushButton(self.centralwidget)
        self.save_button.setGeometry(QtCore.QRect(290, 400, 81, 31))
        self.save_button.setObjectName("save_button")
        self.browse_1 = QtWidgets.QPushButton(self.centralwidget)
        self.browse_1.setGeometry(QtCore.QRect(550, 60, 41, 24))
        self.browse_1.setObjectName("browse_1")
        self.browse_2 = QtWidgets.QPushButton(self.centralwidget)
        self.browse_2.setGeometry(QtCore.QRect(550, 110, 41, 24))
        self.browse_2.setObjectName("browse_2")
        self.browse_3 = QtWidgets.QPushButton(self.centralwidget)
        self.browse_3.setGeometry(QtCore.QRect(550, 160, 41, 24))
        self.browse_3.setObjectName("browse_3")
        self.browse_4 = QtWidgets.QPushButton(self.centralwidget)
        self.browse_4.setGeometry(QtCore.QRect(550, 210, 41, 24))
        self.browse_4.setObjectName("browse_4")
        self.browse_5 = QtWidgets.QPushButton(self.centralwidget)
        self.browse_5.setGeometry(QtCore.QRect(550, 260, 41, 24))
        self.browse_5.setObjectName("browse_5")
        self.browse_6 = QtWidgets.QPushButton(self.centralwidget)
        self.browse_6.setGeometry(QtCore.QRect(550, 310, 41, 24))
        self.browse_6.setObjectName("browse_6")
        self.browse_7 = QtWidgets.QPushButton(self.centralwidget)
        self.browse_7.setGeometry(QtCore.QRect(550, 360, 41, 24))
        self.browse_7.setObjectName("browse_7")
        SettingWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(SettingWindow)
        self.statusbar.setObjectName("statusbar")
        SettingWindow.setStatusBar(self.statusbar)

        self.retranslateUi(SettingWindow)
        QtCore.QMetaObject.connectSlotsByName(SettingWindow)

    def retranslateUi(self, SettingWindow):
        _translate = QtCore.QCoreApplication.translate
        SettingWindow.setWindowTitle(_translate("SettingWindow", "Sonion Laser - Settings"))
        self.label.setText(_translate("SettingWindow", "Layout for SU60 Left"))
        self.label_2.setText(_translate("SettingWindow", "Layout for SU60 Right"))
        self.label_3.setText(_translate("SettingWindow", "Layout for SU85 Left"))
        self.label_4.setText(_translate("SettingWindow", "Layout for SU85 Right"))
        self.label_5.setText(_translate("SettingWindow", "Layout for SU100 Left"))
        self.label_6.setText(_translate("SettingWindow", "Layout for SU100 Right"))
        self.label_7.setText(_translate("SettingWindow", "Serial file for Gamma"))
        self.save_button.setText(_translate("SettingWindow", "SAVE"))
        self.browse_1.setText(_translate("SettingWindow", "..."))
        self.browse_2.setText(_translate("SettingWindow", "..."))
        self.browse_3.setText(_translate("SettingWindow", "..."))
        self.browse_4.setText(_translate("SettingWindow", "..."))
        self.browse_5.setText(_translate("SettingWindow", "..."))
        self.browse_6.setText(_translate("SettingWindow", "..."))
        self.browse_7.setText(_translate("SettingWindow", "..."))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    SettingWindow = QtWidgets.QMainWindow()
    ui = Ui_SettingWindow()
    ui.setupUi(SettingWindow)
    SettingWindow.show()
    sys.exit(app.exec_())