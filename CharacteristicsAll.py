class Demo:
    No=10
    def __init__(self,a,b):
        self.value1=a
        self.value2=b


print("Class Variable : ",Demo.No)

obj1=Demo(11,21)
obj2=Demo(51,101)

print("Instance Variable obj1 : ",obj1.value1 , obj1.value2)
print("Instance Variable obj2 : ",obj2.value1 , obj2.value2)





