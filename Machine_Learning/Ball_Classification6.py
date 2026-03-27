# Rough = 1
# Smooth = 0
# Cricket = 2
# Tennis = 1

from sklearn import tree

def main():
    print("Ball Classification Case Study \n")

    # Original Encoded Dataset

    # Independant variables
    X = [[35,1],[47,1],[90,0],[48,1],[90,0],[35,1],[92,0],[35,1],[35,1],[35,1],[96,0],[43,1],[110,0],[35,1],[95,0]] 
    
    # Dependant variables
    Y = [1,1,2,1,2,1,2,1,1,1,2,1,2,1,2]

    # Independant Variables for Training
    Xtrain = [[35,1],[47,1],[90,0],[48,1],[90,0],[35,1],[92,0],[35,1],[35,1],[35,1],[96,0],[43,1],[110,0]] 
    
    # Independant Variables for Testing
    Xtest = [[35,1],[95,0]] 
    
    # Dependant Variables for Training
    Ytrain = [1,1,2,1,2,1,2,1,1,1,2,1,2]
    
    # Dependant Variables for Testing
    Ytest = [1,2]

    modelobj = tree.DecisionTreeClassifier()

    trainedmodel = modelobj.fit(Xtrain,Ytrain)
    
    Result = trainedmodel.predict([[35,1]])
    print(type(Result))
    if(Result == 1):
        print({"object looks like tennis"}) 
    elif(Result == 2):
        print({"object looks like cricket"}) 

    print("Model predicts the object as : ",Result)


if __name__ == "__main__":
    main()
