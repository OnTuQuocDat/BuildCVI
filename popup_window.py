from PyQt5 import QtWidgets
from PyQt5 import QtCore

def pop_up_configuration_file():
    msg = QtWidgets.QMessageBox()
    msg.setIcon(QtWidgets.QMessageBox.Warning)
    msg.setText("Cannot save default configuration file")
    msg.exec_()

def pop_up_VMC_exe():
    msg = QtWidgets.QMessageBox()
    msg.setIcon(QtWidgets.QMessageBox.Warning)
    msg.setText("There was an error launching VMC_HK.exe application")
    msg.exec_()  

def pop_up_content(content):
    msg = QtWidgets.QMessageBox()
    msg.setIcon(QtWidgets.QMessageBox.Information)
    msg.setText(content)
    msg.exec_()  