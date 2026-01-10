def CheckEven(no):
    if(no%2==0):
        return True    
    else:
        return False    
def main():      
    value=0
    ret=False
    print("Enter the Number ")
    value=int(input())
    ret=CheckEven(value)
    if(ret==True):
        print("Number is Even")
    else:
        print("Number is Odd")
if(__name__=="__main__"):
    main()
