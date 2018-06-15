#it use for Ubuntu and raspberryPi operating system
#it is so simple code without any special that read for temp libraries 
# Python 3.5.2
# H. Dalbudak 16.05.2018

import io 
import time 
while True:
  ftemp0 = open("/sys/class/thermal/thermal_zone0/temp", "r")
  ftemp1 = open("/sys/class/thermal/thermal_zone1/temp", "r")
  ftemp2 = open("/sys/class/thermal/thermal_zone2/temp", "r")
  
  temp0 = ftemp0.readline()
  temp1 = ftemp1.readline()
  temp2 = ftemp2.readline()

  cputemp0 = "temp0: "+temp0
  cputemp1 = "temp1: "+temp1
  cputemp2 = "temp2: "+temp2
  
  #outputs 
  print (cputemp0)
  print (cputemp0)
  print (cputemp0)
