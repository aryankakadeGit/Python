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


def main():
    MarvellousAdvertise("Advertising.csv")
 

if __name__=="__main__":
    main()