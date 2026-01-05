# One function can call Another Function

def fun():
    print("INSIDE FUN")
    
def gun():
    print("INSIDE GUN")
    fun()

def main():
     gun()

if(__name__=="__main__"):
    main()

    