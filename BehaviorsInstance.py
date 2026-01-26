class Demo:
    No=10
    def __init__(self,a,b):
        self.value1=a
        self.value2=b

    def Fun(self):
        print("INSIDE INSTANCE METHOD FUN ",self.value1,self.value2)
    
    @classmethod  # Have to convey compulsary 
    def Sun(cls):
        print("Inside CLASS METHOD SUN ",cls.No)

Demo.Sun() 
print("Class Variable No : ",Demo.No)
obj = Demo(11,21)
obj.Fun()
print("INSTANCE VARIABLE : ",obj.value1,obj.value2)


