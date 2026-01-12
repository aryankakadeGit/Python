def FilterX(Task, Element):
    Result = []
    for no in Element:
        if Task(no):
            Result.append(no)
    return Result  

def mapX(Task, Element):
    Result = []
    for no in Element:
        Result.append(Task(no))
    return Result

def reduceX(Task, Element):
    Sum = 0
    for no in Element:
        Sum = Task(Sum, no)
    return Sum 