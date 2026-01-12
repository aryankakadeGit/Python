no = 11 #Global ----- Data defination statement
def fun(): 
    no = 21 #Local
    print("Value of no from fun() is : ",no)#21
print("Value of no is : ",no)#11
fun()