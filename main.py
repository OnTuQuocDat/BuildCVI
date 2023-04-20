# Author: On Tu Quoc Dat - Control System Engineer
# Company : Sonion Viet Nam Co.,Ltd
# Version : 1.0
# Update  : 19/04/2023
# Built = Python 3.10.7 

#Special command python -m PyQt5.uic.pyuic -x inteface.ui -o interface.py


from PyQt5.QtWidgets import QApplication,QMainWindow
import sys
from Page1 import Ui_MainWindow
from UniqueUI import Ui_SelectUniqueCode
from Printer import Ui_Printer
from SettingUI import Ui_SettingWindow
from laserconfig import *
from popup_window import *
from tcp import *
from print_serial import *
from Gamma import *

class Printer(QMainWindow):
    def __init__(self):
        super().__init__()
        self.win3 = QMainWindow()
        self.page_printer = Ui_Printer()
        self.page_printer.setupUi(self.win3)
        self.win3.setFixedHeight(681)
        self.win3.setFixedWidth(818)
        self.win3.show()

class SettingUI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.win4 = QMainWindow()
        self.page_setting = Ui_SettingWindow()
        self.page_setting.setupUi(self.win4)
        self.win4.setFixedHeight(486)
        self.win4.setFixedWidth(647)
        self.win4.show()

class UniqueUI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.win2 = QMainWindow()
        self.page_unique = Ui_SelectUniqueCode()
        self.page_unique.setupUi(self.win2)
        self.win2.show()

        self.page_unique.SU60left_button.clicked.connect(SU60_left)
        self.page_unique.SU60right_button.clicked.connect(SU60_right)
        self.page_unique.SU85left_button.clicked.connect(SU85_L)
        self.page_unique.SU85right_button.clicked.connect(SU85_R)
        self.page_unique.SU100left_button.clicked.connect(SU100_L)
        self.page_unique.SU100right_button.clicked.connect(SU100_R)

class Page1(QMainWindow):
    def __init__(self):
        super().__init__()
        self.win1 = QMainWindow()
        self.page1 = Ui_MainWindow()
        self.page1.setupUi(self.win1)
        self.win1.setFixedHeight(141)
        self.win1.setFixedWidth(990)
        self.win1.show()

        self.page1.Scan_button.clicked.connect(self.scan_function)
        self.page1.Start_button.clicked.connect(self.start_function)
        self.page1.Stop_button.clicked.connect(self.stop_function)
        self.page1.Manual_button.clicked.connect(self.manual_function)
        self.page1.Settings_button.clicked.connect(self.settings_function)
        self.page1.Unique_code_button.clicked.connect(self.unique_code_button_function)
        self.page1.Quit_button.clicked.connect(self.quit_function)
        
        self.product_gamma = 11 #Product for Gamma
        self.serial_gamma = []
    def scan_function(self):
        pass
    def start_function(self):
        #Generate serial gamma
        last_serial = output_serial(self.product_gamma)
        #Write final serial gamma into file txt
        write_sn_gamma(last_serial,laserconfig.serialforGammapath)

                    
            




    def stop_function(self):
        pass
    def manual_function(self):
        pass
    def settings_function(self):
        pass
    def unique_code_button_function(self):
        pass
    def quit_function(self):
        self.win1.close()

if __name__ == '__main__':
    try:
        app = QApplication(sys.argv)
        w = Page1()
        laserconfig = Laser_Param()
        # print("Laser config test: ",laserconfig.launch_exe)

        laserconfig.check_configuration_file()
        #Launch VMC_HK.exe
        laserconfig.launch_VMC_HK()
        #Check TCP connection
        # if TCP_init() < 0:
            # pop_up_content("Connection to server failed")
        # else:
            #Run User Interface
        TCP_init()
        #RUN USER INTERFACE



        sys.exit(app.exec())
    except KeyboardInterrupt:
        print("Error")

