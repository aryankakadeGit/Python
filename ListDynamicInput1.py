def main():
    size=0
    value=0
    print("Enter the Number of elements :")
    size=int(input())
    data=list()
    print("Enter the elements : ")
    for i in range(size):
        value=int(input())
        
        data.append(value)# data[i] =/= no working
                          # index out of bound 
                          # coz no responsibility
    print(data)

if(__name__=="__main__"):
    main()
    