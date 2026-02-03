import os
def main():
    Filename= input("Enter name of File : ")
    if os.path.exists(Filename):
        os.remove(Filename)
        print("File gets Deleted")
         
    else:
        print("There is no such file")

if __name__=="__main__":
    main()