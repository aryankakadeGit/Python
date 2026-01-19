import time
import multiprocessing
def SumCube(no):
    sum=0

    for i in range(1,no+1):
        sum=sum+(i**3)
    return sum

def main():
    Data =[1000000,2000000,3000000,4000000,5000000,6000000,7000000,8000000,9000000,10000000]
    Result=[]
    start_time=time.time()
    pobj = multiprocessing.Pool()
    Result=pobj.map(SumCube,Data)
    pobj.close()
    pobj.join()
    print(Result)
    end_time=time.time()
    print("Total Execution Time : ",end_time-start_time)


if __name__ =="__main__":
    main()  