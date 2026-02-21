import sys
import os 
import schedule
import time
def DirectoryScanner(DirName="Marvellous"):    
    Border = "*"*50
    Timestamp=time.ctime()
    LogFileName="Marvellous %s.log" %(Timestamp)
    LogFileName=LogFileName.replace(" ","_")
    LogFileName=LogFileName.replace(":","_")
    fobj=open(LogFileName,"w") 
    fobj.write(Border+"\n")
    fobj.write("This is a log file created by marvellous automation\n")
    fobj.write("This is a Directory cleaner script\n")    
    fobj.write(Border+"\n")
    Ret=False
    Ret = os.path.exists(DirName)
    
    if(Ret==False):
        print("There is no such directory")
        return
    
    Ret=os.path.isdir(DirName)
    
    if(Ret==False):
        print("It is not a directory")
        return
    FileCount = 0
    EmptyFileCount = 0

    for FolderName,SubFolder,Filename in os.walk(DirName):
        for fName in Filename:
            FileCount+=1
            fName=os.path.join(FolderName,fName)

            if(os.path.getsize(fName)==0):   
                EmptyFileCount+=1
                os.remove(fName)
    
    fobj.write(Border+"\n")
    fobj.write("Total Files Scanned : "+str(FileCount)+"\n")
    fobj.write("Total Empty Files Fount : "+str(EmptyFileCount)+"\n")    
    fobj.write("This log file is created at "+Timestamp+"\n")
    fobj.write(Border+"\n")
    fobj.close()
            

def main():

    Border = "*"*50
    print(Border)
    print("______________Marvellous Automation_____________")
    print(Border)

    if(len(sys.argv)!=2):
        print("Invalid no of arguments")
        print("Please specify name of directory")
        return
    
    #DirectoryScanner(sys.argv[1])
    schedule.every(1).minute.do(DirectoryScanner)
    while(True):
        schedule.run_pending()
        time.sleep(1)

    print(Border)
    print("_____________Marvellous Automation_____________")
    print(Border)

if __name__ == "__main__":
    main()
