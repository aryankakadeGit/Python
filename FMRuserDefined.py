from functools import reduce

CheckEven=lambda no: no%2==0
increment=lambda no : no+1
add=lambda a,b: a+b

#   FilterX(CheckEven,data)
def FilterX(Task,Element): #(CheckEven,data)
    Result=list() #Result = [] Not Used
    for no in Element:
        Ret=Task(no) #CheckEven(no)
        if(Ret==True):
            Result.append(no)
    
    return Result  

def main():
    data = [11,10,15,20,22,27,30]
    print("Actual data is :",data)
    
    Fdata = list(FilterX(CheckEven,data))
    print("Data after filter is :",Fdata)
    
    Mdata=list(map(increment,Fdata))
    print("Data after map is :",Mdata)
    
    Rdata=reduce(add,Mdata)
    print("Data after reduce is : ",Rdata)
if(__name__=="__main__"):
    main()