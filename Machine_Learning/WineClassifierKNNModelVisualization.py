import matplotlib.pyplot as plt
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score,confusion_matrix,classification_report
from sklearn.preprocessing import StandardScaler

def marvellousClassifier(Datapath):
    Border = "-"*40
    print(Border)
    print("1 :Load dataset from CSV file")
    print(Border)

    print(Border)
    df= pd.read_csv(Datapath)
    print("Some entries from dataset")
    print(df.head())
    print(Border)

    # step 2 : clean dataset by removing Empty cells
    print(Border)
    print("2 :clean dataset by removing Empty cells")
    print(Border)

    df.dropna(inplace= True)
    print("TOtal Records : ",df.shape[0])
    print("TOtal Columns : ",df.shape[1])
    print(Border)

    
    # step 3 : Separate Dependant and INdependant Variables"
    print(Border)
    print("3 : Separate Dependant and INdependant Variables")
    print(Border)

    X=df.drop(columns=['Class'])
    Y=df['Class']

    print("Shape of X :",X.shape)
    print("The shape of Y :",Y.shape)
    

    print(Border)
    print("Input columns are : ",X.columns.to_list())
    print(Border)

    # step 4 : Split dataset for training and testing
    print(Border)
    print("4 : Split dataset for training and testing")
    print(Border)

    X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size=0.2,random_state=42,stratify=Y)
    print(Border)
    print("Information from training and testing data :")
    print("y_train shape :",X_train.shape)
    print("y_train shape :",X_test.shape)
    print("Y_train shape :",Y_train.shape)
    print("Y_test shape :",Y_test.shape)
    print(Border)

    # step 5  : Feature Scaling
    print(Border)
    print("5  : Feature Scaling")
    print(Border)


    scaler = StandardScaler()
    
    # independant variable scaling
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.fit_transform(X_test)
    print("feature scaling done ")

    # step 6  : Explore multiple values of K
    # Hyperparameter tuning
    print(Border)
    print("6  : Explore multiple values of K") 
    print(Border)

    accuracy_scores = []
    K_values = range(1,21)

    for k in K_values:
        model = KNeighborsClassifier(n_neighbors=k)
        
        model.fit(X_train_scaled,Y_train)
        Y_pred = model.predict(X_test_scaled)
        accuracy = accuracy_score(Y_test,Y_pred)
        accuracy_scores.append(accuracy)

    print(Border)
    print("Accuracy report of all k values in 1 - 20 : ")
    for value in accuracy_scores:
        print(value)
    print(Border)

    # step 7  : plot graphs of K  vs Accuracy
    print(Border)
    print("7  : plot graphs of K  vs Accuracy") 
    print(Border)
    plt.figure(figsize=(8,5))
    plt.plot(K_values,accuracy_scores,marker='o')
    plt.title("K Values vs accuracy")
    plt.xlabel("Value of K")
    plt.ylabel("Accuracy")
    plt.grid(True)
    plt.xticks(list(K_values))
    plt.show()
    

def main():
    Border = "-"*40
    print(Border)
    print("Wine classifer")
    print(Border)  
    marvellousClassifier("WinePredictor.csv")



if __name__=="__main__":
    main()