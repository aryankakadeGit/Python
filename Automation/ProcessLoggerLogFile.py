# Commandline Input Code
import sys
import psutil
import os
def createlog(FolderName):
    Ret=False
    Ret = os.path.exists(FolderName)
    if(Ret == True):
        Ret=os.path.isdir(FolderName)
        if(Ret==False):
            print("Unable to create folder")
            return
    else:
        os.mkdir(FolderName)
        print("Directory for log files gets crested successfully")
        
def main():
    Border = "-"*50
    print(Border)
    print("------Marvellous Platform Survillence System------")
    print(Border)
    if(len(sys.argv)==2):
        if(sys.argv[1])=="--h" or sys.argv[1]=="--H":
            print("This script is used to :")
            print("1 : Create automatic logs")
            print("2 : Executes periodically")
            print("3 : Sends mail with log")
            print("4 : Store information about preprocessor")
            print("5 : Store information about CPU")
            print("6 : Store information about RAM usage")
            print("7 : Store information about Secondary storage")
        elif(sys.argv[1])=="--U" or sys.argv[1]=="--u":
            print("USe the automation script as")
            print("ScriptName.py Timeinterval DirectoryName")
            print("Timeinterval : Time in minutes for periodic schedulling")
            print("DirectoryName : Name of directory to create auto logs")
        else:
            print("Unable to proceed as there is no such option")
            print("use --u or --u for more details")

    # python demo.py 5 Marvellous
    elif(len(sys.argv)==3):
        print("Inside Projects logic")
        print("Time Interval : ",sys.argv[1]) 
        print("Directory Name : ",sys.argv[2])
        createlog(sys.argv[2]) 

    else :
        print("Invalid no of cmd line arguments")
        print("Unable to proceed as there is no such option")

    print(Border)
    print("----------Thank you for using our script----------")
    print(Border)
if __name__=="__main__":
    main()