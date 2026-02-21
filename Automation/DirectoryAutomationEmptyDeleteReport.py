import sys
import os 
def DirectoryScanner(DirName="Marvellous"):
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
            print("Filename : ",fName)
            print("FileSize : ",os.path.getsize(fName))
            if(os.path.getsize(fName)==0):   
                EmptyFileCount+=1
                os.remove(fName)
    
    Border = "*"*50
    print(Border)
    print("....Automation Report....")
    print("Total Files Scanned : ",FileCount)
    print("Total Empty Files Fount : ",EmptyFileCount)    
    print(Border)

            

def main():
    Border = "*"*50
    print(Border)
    print("______________Marvellous Automation_____________")
    print(Border)

    if(len(sys.argv)!=2):
        print("Invalid no of arguments")
        print("Please specify name of directory")
        return
    
    DirectoryScanner(sys.argv[1])
    print(Border)
    print("_____________Marvellous Automation_____________")
    print(Border)

if __name__ == "__main__":
    main()
