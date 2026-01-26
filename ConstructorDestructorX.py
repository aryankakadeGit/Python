import gc

class Demo:
    def __init__(self):
        print("Inside Constructor")

    def __del__(self):
        print("Inside Destructor")

# Allocate
obj1=Demo()
obj2=Demo()

# Use

# Deallocate
del obj1,obj2                           #free ( Request )
gc.collect()                            #system.gc 

print("End of Application")

