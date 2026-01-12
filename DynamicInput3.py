def summation(Arr):
    sum =0
    for i in range(len(Arr)):
        sum=sum+Arr[i]
    return sum


def main():
    size=0
    value=0
    print("Enter the Number of elements :")
    size=int(input())
    data=list()
    print("Enter the elements : ")
    for i in range(size):
        value=int(input())
        
        data.append(value)
    iRet=summation(data)

    print(data)
    print("Summation is :",iRet)

if(__name__=="__main__"):
    main()
    