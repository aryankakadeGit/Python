import os
def main():
    Filename= input("Enter name of File : ")
    Ret = os.path.exists(Filename)
    if(Ret == True):
        fobj = open(Filename,"r")
        print("File Successfully Opened")
    else:
        print("File does not exist")
    


if __name__=="__main__":
    main()