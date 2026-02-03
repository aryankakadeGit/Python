# python Commandline4.py 11 10
import sys

def main():
    print("Command line arguments  Addition is :\n")
    a=int(sys.argv[1])
    b=int(sys.argv[2])
    print(a+b)

    

if __name__=="__main__":
    main()
