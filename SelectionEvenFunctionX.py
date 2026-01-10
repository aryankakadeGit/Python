# Procedural
def CheckEven(no):
    if(no%2==0):
        print("Even")
    else:
        print("Odd")
    
def main():      
    value=0
    print("Enter the Number ")
    value=int(input())
    CheckEven(value)

if(__name__=="__main__"):
    main()
