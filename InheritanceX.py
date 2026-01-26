class Parent:
    def __init__(self):
        print("Inside parent constructor \n")
        self.No1=10
        self.No2=20

    def Fun(self):
        print("Inside Fun method of parent \n",self.No1,self.No2)

class Child(Parent):
    def __init__(self):
        super().__init__()
        print("Inside Child Constructor\n")
        self.A=11
        self.B=21

    def Sun(self):
        print("Inside sun method of child\n",self.A,self.B,self.No1,self.No2)

cobj=Child()

print(cobj.No1)     #10
print(cobj.No2)     #20
#______________________\
#                      /
print(cobj.A)       #11
print(cobj.B)       #21

cobj.Fun()
cobj.Sun()

