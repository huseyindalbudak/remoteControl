import ftplib
import time
filename = 'working.txt'

while True:
    ftp = ftplib.FTP('|||.||.|||.||')  #domian name // Host
    ftp.login('...........','..........') #'userName','password'
    ftp.cwd('............................')  #remote site (file adresi)
    myfile = open('path_to+file/working.txt','rb') #uploaded file
    ftp.storlines('STOR '+filename,myfile)
    ftp.quit()
    time.sleep(60)   # you can change for sleep time
