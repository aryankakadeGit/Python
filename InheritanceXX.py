class Parent:
    def __init__(self):
        print("Inside parent constructor \n")
        

    def Fun(self):
        print("Inside Fun method of parent \n")

class Child(Parent):
    def __init__(self):
        super().__init__()
        print("Inside Child Constructor\n")
        

    def Fun(self):
        super().Fun()
        print("Inside Fun method of child\n")

cobj=Child()

cobj.Fun()
