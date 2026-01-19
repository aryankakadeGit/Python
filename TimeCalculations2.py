import time

def Factorial(no):
    fact = 1
    for i in range(1,no+1):
        fact=fact*i
    
    return fact

def main():
    value=int(input("Enter Number :"))
    start_time=time.time()
    Ret=Factorial(value)
    end_time=time.time()
    print("Factorial is ",Ret)
    print("TOTAL EXECUTION TIME IS : ",end_time-start_time)


if __name__=="__main__":
    main()
    