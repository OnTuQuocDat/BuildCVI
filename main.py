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
    
    def scan_function(self):
        pass
    def start_function(self):
        pass
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
        print("Laser config test: ",laserconfig.launch_exe)

        sys.exit(app.exec())
    except KeyboardInterrupt:
        print("Error")

