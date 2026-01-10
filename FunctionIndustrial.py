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
    print(ret)

if(__name__=="__main__"):
    main()
