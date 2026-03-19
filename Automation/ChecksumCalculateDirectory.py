import hashlib
import os
def CalculateChecksum(FileName):
    fobj=open(FileName,"rb")
    hobj=hashlib.md5()
    Buffer = fobj.read(1000)
    while(len(Buffer)>0):
        hobj.update(Buffer)
        Buffer = fobj.read(1000)
    fobj.close()
    return hobj.hexdigest()

def DirectoryWatcher(DirectorryName="Marvellous"):
    Ret=False
    Ret=os.path.exists(DirectorryName)
    if(Ret==False):
        print("There is no such directory")
    Ret=os.path.isdir(DirectorryName)
    if(Ret==False):
        print("It is not a directory")
        return
    for FolderName,SubFolderName,FileName in os.walk(DirectorryName):
        for fname in FileName:
            fname=os.path.join(FolderName,fname)
            Checksum=CalculateChecksum(fname)
            print(f"File Name : {fname } Checksum : {Checksum}")

def main():
    DirectoryWatcher()

if(__name__=="__main__"):
    main()
