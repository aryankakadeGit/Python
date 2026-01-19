import os

def Factorial(no):
    fact = 1
    for i in range(1,no+1):
        fact=fact*i
    
    return fact

def main():
    value=int(input("Enter Number :"))
    Ret=Factorial(value)
    print("Factorial is ",Ret)


if __name__=="__main__":
    main()
    