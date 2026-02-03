import os
def main():
    Filename= input("Enter name of File : ")
    if os.path.exists(Filename):
        fobj = open(Filename,"r")
        print(fobj.name)
        print(fobj.mode)
        print(fobj.closed)
        fobj.close()
        print(fobj.closed)

        
    else:
        print("There is no such file")

if __name__=="__main__":
    main()