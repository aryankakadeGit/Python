import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error,r2_score
from sklearn.model_selection import train_test_split

def MarvellousHeadBrain(datapath):

    Border = "-"*40

    #------------------------------------------------------------
    # Step 1 : Load the Dataset
    #------------------------------------------------------------

    print(Border)
    print("1 : Load the Dataset")
    print(Border)

    df = pd.read_csv(datapath)

    print("Few Records from dataset : ")
    print(df.head())


    #------------------------------------------------------------
    # Step 2 : Check Dataset Shape
    #------------------------------------------------------------

    print(Border)
    print("2 : Dataset Shape")
    print(Border)

    print("Rows :",df.shape[0])
    print("Columns :",df.shape[1])


    #------------------------------------------------------------
    # Step 3 : Check Missing Values
    #------------------------------------------------------------

    print(Border)
    print("3 : Check Missing Values")
    print(Border)

    print("Missing values count :")
    print(df.isnull().sum())


    #------------------------------------------------------------
    # Step 4 : Statistical Summary
    #------------------------------------------------------------

    print(Border)
    print("4 : Statistical Summary")
    print(Border)

    print(df.describe())


    #------------------------------------------------------------
    # Step 5 : Correlation Matrix
    #------------------------------------------------------------

    print(Border)
    print("5 : Correlation Matrix")
    print(Border)

    print(df.corr())


    #------------------------------------------------------------
    # Step 6 : Split Dataset into X and Y
    #------------------------------------------------------------

    print(Border)
    print("6 : Split Dataset into Independent and Dependent Variables")
    print(Border)

    X = df[['Gender','Age Range','Head Size(cm^3)']]
    Y = df['Brain Weight(grams)']

    print("Shape of X :",X.shape)
    print("Shape of Y :",Y.shape)


    #------------------------------------------------------------
    # Step 7 : Train Test Split
    #------------------------------------------------------------

    print(Border)
    print("7 : Split Dataset for Training and Testing")
    print(Border)

    X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size=0.2,random_state=42)

    print("X_train :",X_train.shape)
    print("X_test :",X_test.shape)
    print("Y_train :",Y_train.shape)
    print("Y_test :",Y_test.shape)


    #------------------------------------------------------------
    # Step 8 : Create and Train Model
    #------------------------------------------------------------

    print(Border)
    print("8 : Create and Train Model")
    print(Border)

    model = LinearRegression()

    model.fit(X_train,Y_train)


    #------------------------------------------------------------
    # Step 9 : Test Model
    #------------------------------------------------------------

    print(Border)
    print("9 : Test Model")
    print(Border)

    Y_pred = model.predict(X_test)


    #------------------------------------------------------------
    # Step 10 : Evaluate Model
    #------------------------------------------------------------

    print(Border)
    print("10 : Evaluate Model")
    print(Border)

    MSE = mean_squared_error(Y_test,Y_pred)

    RMSE = np.sqrt(MSE)

    R2 = r2_score(Y_test,Y_pred)

    print("Mean Squared Error :",MSE)
    print("Root Mean Squared Error :",RMSE)
    print("R2 Score :",R2)



def main():             
    MarvellousHeadBrain("MarvellousHeadBrain.csv")



if __name__ == "__main__":
    main()