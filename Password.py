# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Password.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_PasswordWindow(object):
    def setupUi(self, PasswordWindow):
        PasswordWindow.setObjectName("PasswordWindow")
        PasswordWindow.resize(396, 99)
        self.centralwidget = QtWidgets.QWidget(PasswordWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 30, 71, 16))
        self.label.setObjectName("label")
        self.password_blank = QtWidgets.QLineEdit(self.centralwidget)
        self.password_blank.setGeometry(QtCore.QRect(100, 30, 151, 22))
        self.password_blank.setObjectName("password_blank")
        self.checkpass_button = QtWidgets.QPushButton(self.centralwidget)
        self.checkpass_button.setGeometry(QtCore.QRect(290, 30, 75, 24))
        self.checkpass_button.setObjectName("checkpass_button")
        PasswordWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(PasswordWindow)
        self.statusbar.setObjectName("statusbar")
        PasswordWindow.setStatusBar(self.statusbar)

        self.retranslateUi(PasswordWindow)
        QtCore.QMetaObject.connectSlotsByName(PasswordWindow)

    def retranslateUi(self, PasswordWindow):
        _translate = QtCore.QCoreApplication.translate
        PasswordWindow.setWindowTitle(_translate("PasswordWindow", "Sonion Laser - Password"))
        self.label.setText(_translate("PasswordWindow", "Password"))
        self.checkpass_button.setText(_translate("PasswordWindow", "OK"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    PasswordWindow = QtWidgets.QMainWindow()
    ui = Ui_PasswordWindow()
    ui.setupUi(PasswordWindow)
    PasswordWindow.show()
    sys.exit(app.exec_())
