#it is so simple code without any special that read for temp libraries 
# Python 3.5.2
# H. Dalbudak 16.05.2018

import io 
import time 
  
while True:
    # the paths is used for Ubuntu and raspberryPi operating system
    ftemp0 = open("/sys/class/thermal/thermal_zone0/temp", "r")
    ftemp1 = open("/sys/class/thermal/thermal_zone1/temp", "r")
    ftemp2 = open("/sys/class/thermal/thermal_zone2/temp", "r")
  
    temp0 = ftemp0.readline()
    temp1 = ftemp1.readline()
    temp2 = ftemp2.readline()
    cputempAvInt = ((int(temp0)+int(temp1)+int(temp2))/3)/1000 

    cputempAv = "tempAv " + str(cputempAvInt) + " C"
    cputemp0 = "temp0: "+temp0
    cputemp1 = "temp1: "+temp1
    cputemp2 = "temp2: "+temp2

    print (cputemp0)
    print (cputemp1)
    print (cputemp2)
    print (cputempAv)
    #print (cputempAv)
    time.sleep(5)
