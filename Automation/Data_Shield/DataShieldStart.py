# Commandline Input Code
import sys
import psutil
import os
import schedule
import time

def BackupFiles(Source,Destination):
    copied_Files=[]
    print("Creating a backup folder for backup processes")
    os.makedirs(Destination,exit_ok=True)
    for root,Dirs,Files in os.walk(Source):
        for file in Files:
            src_path=os.path.join(root,file)
            relative = os.path.relpath(src_path)
            dest_path = os.path.join(relative)
            os.makedirs(os.path.dirname(dest_path))

# copy files if its new
            shutil.copy2(src_path,dest_path)
            copied_Files.append(relative)
    return copied_Files

def MarvellousDataShieldStart(Source="Data"):
    BackupName="MarvellousBackup"
    print("Backu p psocc started successfully at ",time.ctime())
    BackupFiles(source,BackupName)

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
        schedule.every(int(sys.argv[1])).minutes.do(MarvellousDataShieldStart,sys.argv[2])

        print("Data shield system started successfully")
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