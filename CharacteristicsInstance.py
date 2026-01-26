import gc

class Demo:
    # Class Variable | Outside Class Function 
    No1=10
    No2=11

    
    def __init__(self):

        # Instance Variable  | Need a obj to access
        self.a=101
        self.b=201
        print("Inside Constructor")

    def __del__(self):
        print("Inside Destructor")

print(Demo.No1) 
print(Demo.No2)

obj=Demo() 
print(obj.a) 
print(obj.b) 
