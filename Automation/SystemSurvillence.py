# Commandline Input Code
import sys
import psutil
import os
import schedule
import time

def createlog(FolderName):
    Border = "-"*50

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
    timestamp=time.strftime("%Y-%m-%d_%H-%M-%S")
    FileName=os.path.join(FolderName,"Marvellous_%s.log" %timestamp)
    print("Log file gets created with name : ",FileName)
    fobj = open(FileName,"w")
    fobj.write(Border+"\n")
    fobj.write("------Marvellous Platform Survillence System------"+"\n")
    fobj.write("----------------- Log Created At : ---------------"+time.ctime())
    fobj.write(Border+"\n\n")
    fobj.write("------------------System report ---------------------")


    #print("CPU USAGE : ",psutil.cpu_percent)
    fobj.write("CPU Usage : %s %%\n"%psutil.cpu_percent)
    fobj.write(Border+"\n\n")


    mem = psutil.virtual_memory

    #print("RAM USAGE : ",mem.percent)
    fobj.write("RAM Usage : %s %%\n"%mem.percent)
    fobj.write(Border+"\n\n")


    fobj.write("\n DISK USAGE REPORT\n")
    fobj.write(Border+"\n\n")

    for part in psutil.disk_partitions:
      try:
        usage = psutil.disk_usage(part.mountpoint)
        #print(f"{part.mountpoint} used {usage.percent}%%")
        fobj.write("%s ---> %s %% used"%(part.mountpoint,usage.percent))
      except:
        pass
    fobj.write(Border+"\n\n")

    net=psutil.net_io_counters()
    fobj.write("\nNetwork usage report\n")
    fobj.write("\nSent : %.2f MB \n"%(net.bytes_sent/(1024*1024)))
    fobj.write("\nReceived : %.2f MB \n"%(net.bytes_recv/(1024*1024)))
    fobj.write(Border+"\n\n")


    # Process log
    


    fobj.write(Border+"\n")
    fobj.write("End of log file")
    fobj.write(Border+"\n")                  
    

def ProcessScan():
    print("Process scan Report")
    for proc in psutil.process_iter(attrs=["pid","name","status"]):
        info=proc.info
        print(info["pid"],info["name"],info["status"])
        

def main():
    ProcessScan()
    return
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

        # Apply the scheduler
        schedule.every(int(sys.argv[1])).minutes.do(createlog,sys.argv[2])

        print("Platform Survillenge system started successfully")
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