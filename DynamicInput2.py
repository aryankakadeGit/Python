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

    sum =0
    for i in range(size):
        sum=sum+data[i]

    print(data)
    print("Summation is :",sum)

if(__name__=="__main__"):
    main()
    