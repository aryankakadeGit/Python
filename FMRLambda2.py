from functools import reduce

CheckEven=lambda no: no%2==0

increment=lambda no : no+1

add=lambda a,b: a+b

def main():
    data = [11,10,15,20,22,27,30]
    print("Actual data is :",data)
    
    Fdata = list(filter(CheckEven,data))
    print("Data after filter is :",Fdata)
    
    Mdata=list(map(increment,Fdata))
    print("Data after map is :",Mdata)
    
    Rdata=reduce(add,Mdata)
    print("Data after reduce is : ",Rdata)
if(__name__=="__main__"):
    main()