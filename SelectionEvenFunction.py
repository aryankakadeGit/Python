
def CheckEven(no):
    if(no%2==0):
        print("Even")
    else:
        print("Odd")
    
def main():      
    CheckEven(22)       #positional
    CheckEven(no=21)    #keyword

if(__name__=="__main__"):
    main()
