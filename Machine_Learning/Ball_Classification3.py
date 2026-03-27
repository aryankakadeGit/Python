# Rough = 1
# Smooth = 0
# Cricket = 2
# Tennis = 1

from sklearn import tree

def main():
    print("BAll Classification Case Study \n")

    # Data Gathering Done

    # Independant variables
    Features = [[35,1],[47,1],[90,0],[48,1],[90,0],[35,1],[92,0],[35,1],[35,1],[35,1],[96,0],[43,1],[110,0],[35,1],[95,0]] 
    
    # Dependant variables
    labels = [1,1,2,1,2,1,2,1,1,1,2,1,2,1,2]

    modelobj = tree.DecisionTreeClassifier()

    trainedmodel = modelobj.fit(Features,labels)
    
    
    Result = trainedmodel.predict([[37,1],[94,0]]) #[1 2]

    print("Model predicts the object as : ",Result)




if __name__ == "__main__":
    main()
