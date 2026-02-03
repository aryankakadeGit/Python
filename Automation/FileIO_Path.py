import os
def main():
    Filename= input("Enter name of File : ")
    Ret = os.path.isabs(Filename)
    if Ret == True:
        print("It is absolute path")
    else :
        print("It is relative path")


if __name__=="__main__":
    main()