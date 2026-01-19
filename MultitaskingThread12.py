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
    
    t1=threading.Thread(target=Sumeven,args=(100000000,))
    t2=threading.Thread(target=SumOdd,args=(100000000,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()
    end_time=time.time()
    print("Time Required : ",end_time-start_time)
 
if __name__=="__main__":
    main()
    