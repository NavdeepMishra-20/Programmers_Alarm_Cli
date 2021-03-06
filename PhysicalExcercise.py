
import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
from os.path import expanduser
import time as t
import pygame

from plyer import notification


import getpass
usernm = getpass.getuser()
from datetime import datetime



   
    
def userDirFinder():
    from os.path import expanduser
    usrpth = expanduser("~")
    mainp = os.path.join(usrpth, "Documents")
    return mainp
    
def checknSetdir():
    mainp=userDirFinder()
    target_path = os.path.join(mainp,"Programmers_Alram","Physical_Excercise_log")
    
    if os.path.exists(target_path):
        os.chdir(target_path)
    else:
        
        os.makedirs(target_path)
        os.chdir(target_path)
        
    
def getCurrentDateandTime():
    Dat = datetime.now()
    
    currentD = Dat.strftime("%d/%m/%Y") 
    currentT = Dat.strftime("%I:%M %p")
    return currentD , currentT
def notifier():
    
   
    notification.notify(
            title = "Time for a Short Physical Excercise break.",
            message ="Please do some mini physical excercises and after that open the program and type \"Done\" in the Program Windows",
            app_icon = ".\\Notification_Icons\\Excercise.ico",
            app_name = "Programmers alarm"
            
        
        )
    t.sleep(4) 
    
def logCreater():
        notifier()
        print("Countdown paused")
        current_dir = os.getcwd()
        pygame.mixer.init()
        pygame.mixer.music.load(".\\Notification_Sounds\\Physound.mp3")
        pygame.mixer.music.play(-1)
        write_msg = f"Physical Excercise Done by {usernm}"
        while 1:
            os.system('cls')
            try:
                print("Time for a Physical Excercise Break , After the Physical Excercise Break")
                usr_msg = input("Type \"Done\" to stop this alarm: ").strip()
                
                usr_msg = usr_msg.lower()
                if usr_msg != "done":
                    raise ValueError("Invalid Answer")
                elif "done" == usr_msg:
                    checknSetdir()
                    with open("Physical_Excercise_log.txt","a") as fi:
                        cdat , ctim = getCurrentDateandTime()
                        fi.write(f"Date: {cdat}          Time: {ctim}          Message: {write_msg}\n")
                        # print("Log Created")
                        pygame.mixer.music.stop()
                        pygame.mixer.quit()
                        os.chdir(current_dir)
                       
                        break
                        
                
            except Exception as e:
                print(e)
                input("Press Enter to Continue")
            
    
def logReader():
        
        checknSetdir()
        try:
            
            with open("Physical_Excercise_log.txt","r") as fi:
                lis = fi.readlines()
                for i in lis:
                    print(i)
            input("Press to contiue")
        except FileNotFoundError:
            print("No log is created yet")
            input("Press to contiue")
        except Exception as e:
            print(e)

    

if __name__ =="__main__":
    
    print("Please Run the MainModule.py only")
    input("Press Enter to continue...")