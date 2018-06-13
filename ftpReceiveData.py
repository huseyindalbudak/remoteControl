import ftplib
import time
filename = 'okuma.txt'

while True:
    ftp = ftplib.FTP('|||.||.|||.||')  #domian name // Host
    ftp.login('................','..................') #'userName','password'
    ftp.cwd('.......................')  #remote site (file adresi)
    #myfile = open('path_to_file/working.txt','rb') #uploaded file for example txt
    #ftp.storlines('STOR '+filename,myfile)
    
    ftp.retrbinary("RETR " + filename, open('okuyucu.txt','wb').write) #we must write
    ftp.quit()
    time.sleep(20)      #it can change 
