import threading
import time
def Sumeven(no):
    sum=0
    for i in range(2,no+1,2):
        sum=sum+i
    print("EVEN SUM : ",sum)

def SumOdd(no):
    sum=0
    for i in range(1,no+1,2):
        sum=sum+i
    print("ODD SUM : ",sum)

def main():
    start_time=time.time()
    Sumeven(100000000)
    SumOdd(100000000)
    end_time=time.time()
    print("Time Required : ",end_time-start_time)
 
if __name__=="__main__":
    main()
    