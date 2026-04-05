import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt

from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error,r2_score
from sklearn.model_selection import train_test_split

def MarvellousAdvertise(datapath):
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
    # Step 2 : Remove Unwanted Columns
    #------------------------------------------------------------
    print(Border)
    print("2 :Remove Unwanted Columns")
    print(Border)

    print("Shape if dataset before removal : ")
    if 'Unnamed: 0' in df.columns:
        df.drop(['Unnamed: 0'],inplace=True)

    print("Shape of dataset After removal :")
    print(Border)
    print("Clean Dataset is : ")
    print(df.head())
    print(Border)

    #------------------------------------------------------------
    # Step 3 :Check Missing Values
    #------------------------------------------------------------
    print(Border)
    print("3 :Check Missing Values")
    print(Border)
    print("Missing values Count : ",df.isnull().sum())

    #------------------------------------------------------------
    # Step 4 : Display Statistical summary
    #------------------------------------------------------------
    print(Border)
    print("4 : Display Statistical summary")
    print(Border)

    print(df.describe())

    #------------------------------------------------------------
    # Step 5 : Correlation between columns
    #------------------------------------------------------------
    print(Border)
    print("5 : Correlation between columns")
    print(Border)

    print("Correlation matrix : ")
    print(df.corr())

    #------------------------------------------------------------
    # Step 6 : Split Dataset into independant and dependant variables
    #------------------------------------------------------------
    print(Border)
    print("6 : Split Dataset into independant and dependant variables")
    print(Border)
    X=df[['TV','radio','newspaper']]
    Y=df['sales']

    print("Shape of independant variables : ",X.shape)
    print("Shape of Dependant variables : ",Y.shape)

    #------------------------------------------------------------
    # Step 7 : Split Dataset for Training and Testing
    #------------------------------------------------------------
    print(Border)
    print("7 : Split Dataset for Training and Testing")
    print(Border)

    X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size=0.2,random_state=42);

    print("X_train shape : ",X_train.shape)
    print("X_test shape : ",X_test.shape)
    print("Y_train shape : ",Y_train.shape)
    print("Y_test shape : ",Y_test.shape)

    #------------------------------------------------------------
    # Step 8 : Create and train the model
    #------------------------------------------------------------
    print(Border)
    print("8 : Create and train the model")
    print(Border)
    model = LinearRegression();
    model.fit(X_train,Y_train)

    #------------------------------------------------------------
    # Step 9 : Test the model 
    #------------------------------------------------------------
    print(Border)
    print("9 : Test the model ")
    print(Border)

    Y_pred = model.predict(X_test)

    #------------------------------------------------------------
    # Step 10 : Evaluate the model
    #------------------------------------------------------------
    print(Border)
    print("10 : Evaluate the model")
    print(Border)
    
    MSE = mean_squared_error(Y_test,Y_pred)
    RMSE = np.sqrt(MSE)
    R2 = r2_score(Y_test,Y_pred)


    print("Mean Squared Error : ",MSE)
    print("Root Mean Squared Error : ",RMSE)
    print("R Square : ",R2)

    #------------------------------------------------------------
    # Step 11 : Calculate model coeffiecient
    #------------------------------------------------------------
    print(Border)
    print("11 : Calculate model coeffiecient")
    print(Border)
    
    for column,value in zip(X.columns,model.coef_):
        print(f"{column} : {value}")

    print("Intercept : ",model.intercept_)

    #------------------------------------------------------------
    # Step 12 : Compare actual and predicted values
    #------------------------------------------------------------
    print(Border)
    print("12 : Compare actual and predicted values")
    print(Border)
    Result = pd.DataFrame({
                            'Actual sale':Y_test.values,
                            'Predicted sale':Y_pred
                           })
    print(Result.head)
    


def main():
    MarvellousAdvertise("Advertising.csv")
 

if __name__=="__main__":
    main()