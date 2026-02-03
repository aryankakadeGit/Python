import os
def main():
    Filename= input("Enter name of File : ")
    if os.path.exists(Filename):
        Ret = os.path.isabs(Filename)

        if Ret == True:
            print("It is absolute path")
        else :
            print("It is relative path")
            NewPath = os.path.abspath(Filename)
            print("Updated path : ",NewPath)
    else:
        print("There is no such file")

if __name__=="__main__":
    main()