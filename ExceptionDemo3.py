def main():

    Ans=0    
    try:
        print("Inside try \n")

        print("Enter first number : \n")
        No1=int(input())

        print("Enter second number : \n")
        No2=int(input())

        Ans=No1/No2


    except ZeroDivisionError as zobj:
        print("Inside except : \n",zobj)

    
    except ValueError as vobj:
        print("Inside except : \n",vobj)
    
    except Exception as eobj: #generic except block
        print("Inside except : \n",eobj)



    finally :
        print("Inside Finally\n")

    print("Division is : ",Ans)



if __name__ =="__main__":
    main() 