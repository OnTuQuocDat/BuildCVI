from popup_window import *
import os
from tcp import *

class Laser_Param():
    def __init__(self):
        self.launch_exe = 1
        self.laser_type = 0
        self.layoutdir = 'C:\\Rofin\\VisualLaserMarker\\MarkingFiles'
        self.DBpath = 'C:\\Sonion\\laser.txt'
        # self.cfgfile = "C:\\lasercfg"
        self.cfgfile = "lasercfg"
        self.serialforGammapath = 'C:\\Sonion\\serial_gamma.txt'
        self.layoutforGammaLpath = "unique_Gamma_L.vlm"
        self.layoutforGammaRpath = "unique_Gamma_R.vlm"
        self.layoutforGammaL2path = "unique_Gamma_L.vlm"
        self.layoutforGammaR2path = "unique_Gamma_R.vlm"
        self.layoutforGammaL3path = "unique_Gamma_L.vlm"
        self.layoutforGammaR3path = "unique_Gamma_R.vlm"

        # self.VMC_HK_location = "C:\\Rofin\\VisualLaserMarker\\Bin\\VMC_HK.exe"
        self.VMC_HK_location = 'C:\\Users\\DAQ\\AppData\\Local\\Programs\\GammaSU\\main.exe'
    
    def check_configuration_file(self):
        fp = open(self.cfgfile, "wb")
        if fp is None:
            pop_up_configuration_file()
        # fp.write()  ## Recheck lại
        fp.close()
    
    def launch_VMC_HK(self):
        if self.launch_exe:
            launch = os.startfile(self.VMC_HK_location)
            if launch == 0:
                pop_up_VMC_exe()
            
            #
