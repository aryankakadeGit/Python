import os

def DirectoryScanner(DirectoryName):    
    
    print("Contents of directory are : ")
    for FolderName,SubFolderName,FileName in os.walk(DirectoryName):
        print("Folder name : ",FolderName)
        for subf in SubFolderName:
            print("SubFolder name : ",subf)
        for fname in FileName:
            print("File name : ",fname)

def main():
    DirectoryName=input("Enter name of Directory ")
    DirectoryScanner(DirectoryName)



if __name__=="__main__":
    main()