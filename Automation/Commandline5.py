# python Commandline4.py 11 10
import sys

def main():
    print("Command line arguments  Addition is :\n")
    if(len(sys.argv)<3 or len(sys.argv)>3):
        print("Invalid no of arguments\n")
    else:
        a=int(sys.argv[1])
        b=int(sys.argv[2])
        print(a+b)

    

if __name__=="__main__":
    main()
