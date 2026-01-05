# One function can call Another Function

def fun():
    print("INSIDE FUN")
    
def gun():
    print("INSIDE GUN")

def main():
     fun()
     gun()

if(__name__=="__main__"):
    main()

    