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

def FindDuplicate(DirectorryName="Marvellous"):
    Ret=False
    Ret=os.path.exists(DirectorryName)
    if(Ret==False):
        print("There is no such directory")
    Ret=os.path.isdir(DirectorryName)
    if(Ret==False):
        print("It is not a directory")
        return
    
    Duplicate={}

    for FolderName,SubFolderName,FileName in os.walk(DirectorryName):
        for fname in FileName:
            fname=os.path.join(FolderName,fname)
            Checksum=CalculateChecksum(fname)
            if Checksum in Duplicate:
                Duplicate[Checksum].append(fname)
            else:
                Duplicate[Checksum]=[fname]
    return Duplicate

def DisplayResult(MyDict):
    Result=list(filter(lambda x:(len(x))>1,MyDict.values()))
    Count = 0
    for value in Result:
        for subvalue in value:
            Count+=1
            print(subvalue)
        print("Value of Count is : ",Count)
        Count = 0
def DeleteDuplicate(Path="Marvellous"):
    Cnt=0
    MyDict=FindDuplicate(path)
    Result=list(filter(lambda x:(len(x))>1,MyDict.values()))
    Count = 0
    for value in Result:
        for subvalue in value:
            Count+=1
            if(Count>1):
                print("Deleted value",subvalue)
                os.remove(subvalue)
                Cnt+=1

        Count=0
    print("Total files Deleted ",Cnt)        


def main():
    DeleteDuplicate()
    DisplayResult(Ret)

if(__name__=="__main__"):
    main()
