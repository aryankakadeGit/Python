def CheckEven(no):
    return(no%2==0)

def increment(no):
    return(no+1)

def main():
    data = [11,10,15,20,22,27,30]
    print("Actual data is :",data)
    Fdata = list(filter(CheckEven,data))
    # Parameter function = Boolean Only
    print("Data after filter is :",Fdata)
    Mdata=list(map(increment,Fdata))
    print("Data after map is :",Mdata)

if(__name__=="__main__"):
    main()