# Commandline Input Code
import sys
import psutil
import os
import schedule
import time

def fun(Dirname):
    fun(_)

def main():
    Border = "-"*50
    print(Border)
    print("------Marvellous Data shield  System------")
    print(Border)
    if(len(sys.argv)==2):
        if(sys.argv[1])=="--h" or sys.argv[1]=="--H":
            print("This script is used to :")
            print("1 : Takes auto bsckup at given time");
            print("2 : Backup only new aupdated files");
            print("3 : creare an archive of backup periodically");
        elif(sys.argv[1])=="--U" or sys.argv[1]=="--u":
            print("USe the automation script as")
            print("ScriptName.py Timeinterval Source DirectoryName")
            print("Timeinterval : Time in minutes for periodic schedulling")
            print("SourceDirectoryName : Name of directory to back up")
        else:
            print("Unable to proceed as there is no such option")
            print("use --u or --u for more details")
    
    # python demo.py 5 Marvellous
    elif(len(sys.argv)==3):
        print("Inside Projects logic")
        print("Time Interval : ",sys.argv[1]) 
        print("Directory Name : ",sys.argv[2])

        # Apply the scheduler
        schedule.every(int(sys.argv[1])).minutes.do(fun,sys.argv[2])

        print("Data shield system started successfully")
        print("Directory created with name : ",sys.argv[2])
        print("Time Interval : in minutes",sys.argv[1])
        print("Press CTRL + C to stop the execution")

        # Wait until abort
        schedule.run_pending()
        time.sleep(1)


    else :
        print("Invalid no of cmd line arguments")
        print("Unable to proceed as there is no such option")


    print(Border)
    print("----------Thank you for using our script----------")
    print(Border)
if __name__=="__main__":
    main() 