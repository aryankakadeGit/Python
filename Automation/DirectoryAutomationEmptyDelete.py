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
    for FolderName,SubFolder,Filename in os.walk(DirName):
        for fName in Filename:
            fName=os.path.join(FolderName,fName)
            print("Filename : ",fName)
            print("FileSize : ",os.path.getsize(fName))
            if(os.path.getsize(fName)==0):   
                os.remove(fName)
            

            

def main():
    Border = "*"*50
    print(Border)
    print("____________Marvellous Automation____________")
    if(len(sys.argv)!=2):
        print("Invalid no of arguments")
        print("Please specify name of directory")
        return
    
    DirectoryScanner(sys.argv[1])
if __name__ == "__main__":
    main()
