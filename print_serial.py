from laserconfig import *

def output_serial(product,serial_gamma):
    if product == 11: #Gamma
        gm1 = serial_gamma[0]
        gm2 = serial_gamma[1]
        gm3 = serial_gamma[2]
        gm4 = serial_gamma[3]
        gm5 = serial_gamma[4]
        gm6 = serial_gamma[5]
        
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
            if gm4 == 69 or gm4 == 73 or gm4 == 79 or gm4 == 81 or gm4 == 85:
                gm4 += 1
            if gm4 == 88 or gm4 == 89:
                gm4 = 90
            if gm4 >= 91:
                gm4 = 48
            if gm6 >= 58 and gm6 < 66 and gm5 == 57 and gm4 == 57 and gm3 != 57:
                gm6 = 66
                gm5 = 66
                gm4 = 66
                gm3 += 1
            
            #gm3
            if gm3 == 69 or gm3 == 73 or gm3 == 79 or gm3 == 81 or gm3 == 85:
                gm3 += 1
            if gm3 == 88 or gm3 == 89:
                gm3 = 90
            if gm3 >= 91:
                gm3 = 48
            if gm6 >= 58 and gm6 < 66 and gm5 == 57 and gm4 == 57 and gm3 == 57 and gm2 != 57:
                gm6 = 66
                gm5 = 66
                gm4 = 66
                gm3 = 66
                gm2 += 1
            
            #gm2
            if gm2 == 69 or gm2 == 73 or gm2 == 79 or gm2 == 81 or gm2 == 85:
                gm2 += 1
            if gm2 == 88 or gm2 == 90:
                gm2 = 90
            if gm2 >= 91:
                gm2 = 48
            if gm6 >= 58 and gm6 < 66 and gm5 == 57 and gm4 == 57 and gm3 == 57 and gm2 == 57 and gm1 != 57:
                gm6 = 66
                gm5 = 66
                gm4 = 66
                gm3 = 66
                gm2 = 66
                gm1 += 1

            #gm1
            if gm1 == 69 or gm1 == 73 or gm1 == 79 or gm1 == 81 or gm1 == 85:
                gm1 += 1
            if gm1 == 88 or gm1 == 89:
                gm1 = 90
            if gm1 >= 91:
                gm1 = 48
            if gm6 >= 58 and gm6 < 66 and gm5 == 57 and gm4 == 57 and gm3 == 57 and gm2 == 57 and gm1 == 57:
                gm6 = 66
                gm5 = 66
                gm4 = 66
                gm3 = 66
                gm2 = 66
                gm1 = 66

    return serial_gamma


def write_sn_gamma(serial_gamma):
    #Write final serial gamma into txt file for next running
    print(Laser_Param.serialforGammapath)