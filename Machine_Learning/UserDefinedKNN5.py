#        A B C D
# x   : [1,2,3,5]
# y   : [2,3,1,6]
# Res : [R,R,B,B]

# predict(3,3)

import numpy as np
import math

def EuclideanDistance(P1,P2):
    Ans = math.sqrt(((P1['X']-P2['X'])**2)+ ((P1['Y']-P2['Y'])**2))
    #   /-----------------------
    # \/ ((x1-y1)^2 + (y2-y1)^2)

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

    print(Border)
    new_point={'X':3,'Y':3}
    for i in data:
        d['distance']=EuclideanDistance(d,new_point)

    print(Border)
    print("Calculated distances are:")
    print(Border)
    for d in data:
        print(d)
    
    sorted_data = sorted(data,key=lambda item:item['distance'])

    print(Border)
    print("Sorted data is :")
    print(Border)

    for d in sorted_data:
        print(d)
    
    k=3
    nearest = sorted_data[:k]
    print(Border)
    print("Nearest three points are : ")
    print(Border)
     
    for d in nearest:
        print(d)

    #Voting
    votes = {}
    for neighbor in nearest:
        label=neighbor['label']
        votes[label]=votes.get(label,0)+1

    print(Border)
    print("Voting result is : ")
    print(Border)

    for d in votes:
        print("Name :",d,"No of votes :",votes[d])
    
    print(Border)
def main():
    MarvellousKNeighborClassifier()
    
if __name__ == "__main__":
    main()