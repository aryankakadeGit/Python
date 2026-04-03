#        A B C D
# x   : [1,2,3,5]
# y   : [2,3,1,6]
# Res : [R,R,B,B]

# predict(3,3)

import numpy as np
import math

def EuclideanDistance(P1,P2):
    Ans = math.sqrt(((P1['X']-P2['X'])**2)+ (P1['Y']-P2['Y'])**2)
    #   /-----------------------
    # \/ ((x1-x2)^2 + (y2-y1)^2)

def MarvellousKNeighborClassifier():
    Border = "-"*40
    data = [
            {'point':'A','X':1,'Y':2,'label':'Red'},
            {'point':'B','X':2,'Y':3,'label':'Red'},
            {'point':'C','X':3,'Y':1,'label':'Blue'},
            {'point':'D','X':5,'Y':6,'label':'Blue'}
           ]
    print(Border)
    print("Marvellous USer Defined KNN")
    print(Border)

    print(Border)
    print("Training Dataset")
    print(Border)

    for i in data:
        print(i)

    print(Border)
    new_point={'X':3,'Y':3}
    print(data[0])
    print(new_point)
    Result = EuclideanDistance(data[0],new_point)
    print(Result)



     
    
def main():
    MarvellousKNeighborClassifier()
    
if __name__ == "__main__":
    main()