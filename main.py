# Author: On Tu Quoc Dat - Control System Engineer
# Company : Sonion Viet Nam Co.,Ltd
# Version : 1.0
# Update  : 19/04/2023
# Built = Python 3.10.7 

#Special command python -m PyQt5.uic.pyuic -x inteface.ui -o interface.py


from PyQt5.QtWidgets import QApplication,QMainWindow
import sys
from Page1 import Ui_MainWindow
from laserconfig import *
from popup_window import *
from tcp import *

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
        
        self.product = 11 #Product for Gamma
        self.serial_gamma = []
    def scan_function(self):
        pass
    def start_function(self):
        match self.product:
            case 11:   #Gamma
                gm1 = self.serial_gamma[0]
                gm2 = self.serial_gamma[1]
                gm3 = self.serial_gamma[2]
                gm4 = self.serial_gamma[3]
                gm5 = self.serial_gamma[4]
                gm6 = self.serial_gamma[5]
                
                for i in range(0,81):
                    gm6 += 1
                    if gm6 == 69 or gm6 == 73 or gm6 == 79 or gm6 == 81 or gm6 == 85:
                        gm6 += 1
                    if gm6 == 88 or gm6 == 89:
                        gm6 = 90
                    if gm6 >= 91:
                        gm6 = 48
                    if gm6 >= 58 and gm6 < 66 and gm5 != 57:
                        gm6 = 66
                        gm5 += 1
                    
                    #gm5
                    if gm5 == 69 or gm5 == 73 or gm5 == 79 or gm5 == 81 or gm5 == 85:
                        gm5 += 1
                    if gm5 == 88 or gm5 == 89:
                        gm5 = 90
                    if gm5 >= 91:
                        gm5 = 48
                    if gm6 >= 58 and gm6 < 66 and gm5 == 57 and gm4 != 57:
                        gm6 = 66
                        gm5 = 66
                        gm4 += 1
                    
                    #gm4
                    
            




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

