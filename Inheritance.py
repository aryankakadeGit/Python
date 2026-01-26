class Parent:
    def __init__(self):
        print("Inside parent constructor \n")
        self.No1=10
        self.No2=20

    def Fun(self):
        print("Inside Fun method of parent \n")

class Child(Parent):
    def __init__(self):
        super().__init__()
        print("Inside Child Constructor\n")
        self.A=11
        self.B=21

    def Sun(self):
        print("Inside sun method of child\n")

cobj=Child()

