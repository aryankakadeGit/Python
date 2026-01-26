class Demo:
    No=10
    def __init__(self,a,b):
        self.value1=a
        self.value2=b


print("Class Variable : ",Demo.No)

obj1=Demo(11,21)
obj2=Demo(51,101)

# print("Class Variable of obj  : ",obj1.No)  *ALLOWED*
print("Instance Variable obj1 : ",obj1.value1 , obj1.value2)# 11 21
print("Instance Variable obj2 : ",obj2.value1 , obj2.value2)# 51 101
obj1.value1=15

Demo.No=0

print("Instance Variable obj1 : ",obj1.value1 , obj1.value2)# 15 21 
print("Instance Variable obj2 : ",obj2.value1 , obj2.value2)# 51 101
print(obj1.No) # 0
print(obj2.No) # 0



