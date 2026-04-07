import pandas as pd
import numpy as np

# has functions to store on HDD
import joblib 

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score,confusion_matrix

#__________________________________________________________
# Function Name : DisplayInfo
# Description   : displays formatted title           
# Parameters    : title(str)
# Return        : NONE
# Date          : 14/03/2026
# Author        : Aryan Hanumant Kakade 
#__________________________________________________________
def DisplayInfo(title):
    print("\n"+"="*70)
    print(title)
    print("="*70)

#__________________________________________________________
# Function Name : ShowData
# Description   : It shows basic info about dataset(df)                
# Parameters    : df
#                 df -> Pandas Dataframe object
#                 Message
#                 Message -> Heading text to display
# Return        : NONE
# Date          : 14/03/2026
# Author        : Aryan Hanumant Kakade 
#__________________________________________________________
def ShowData(df,Message):
    DisplayInfo(Message)
    print("\nFirst five rows of dataset : ")
    print(df.head())

    print("\nShape of dataset : ")
    print(df.shape)

    print("\nColumn names of dataset : ")
    print(df.columns.tolist())
    
    print("\nMissing Values of each column : ")
    print(df.isnull().sum())


#__________________________________________________________
# Function Name : CleanTitanicData
# Description   : It does preprocessing
#                    removes unnecessary columns
#                    Handles missing values
#                    Convert text data to numeric format
#                    Does encoding to categorical columns               
# Parameters    : df -> Pandas Dataframe object
# Return        : df -> Cleaned Pandas Dataframe object
# Date          : 14/03/2026
# Author        : Aryan Hanumant Kakade 
#__________________________________________________________
def CleanTitanicData(df,Message):
    DisplayInfo("Step 2 : Original data")
    print(df.head())
    
    # Remove unnecessary columns
    drop_columns=["Passengerid","zero"]

    existing_columns =[col for col in drop_columns if col in df.columns]
    
    print("Columns to be dropped : ")
    print(existing_columns)

    # Drop the unwanted columns
    df = df.drop(columns=existing_columns)

    DisplayInfo("Step 2 : Data after column removal")
    print(df.head())

    # Handle edge column
    if "Age" in df.columns:
        print("Age column before filling missing values")
        print(df["Age"].head(10))
        
        # coerce -> invalud convert to NaN
        df["Age"]=pd.to_numeric(df["Age"],errors = "coerce")
        
        age_median = df["Age"].median()

        # Replace missing values with median
        df["Age"].fillna(age_median)

        print("Age column after preprocessing")
        print(df["Age"].head(10))

    # Handle fare column
    if "Fare" in df.columns:
        print("\nFare column before preprocessing")
        print(df["Fare"].head(10))
        df["Fare"]=pd.to_numeric(df["Fare"],errors = "coerce")
        fare_median = df["Fare"].median()

        # Replace missing values with median
        df["Fare"].fillna(fare_median)
        print("median of Fare column "+fare_median)

        print("Fare column after preprocessing")
        print(df["Fare"].head(10))

    # Handle Embarked Column
    if "Embarked" in df.columns:
        print("\Embarked column before preprocessing")
        print(df["Embarked"].head(10))
        # convert to string
        df["Embarked"]=df["Embarked"].astype(str).str.strip()

        # Replace missing values with median
        df["Embarked"]=df["Embarked"].replace(['nan','None',''],np.nan)

        # Get Most Frequent Value -  mode
        Embarked_mode = df["Embarked"].mode()[0]
        print("mode of embarked column "+Embarked_mode)

        df["Embarked"] = df["Embarked"].fillna(Embarked_mode)

        print("Embarked column after preprocessing")
        print(df["Embarked"].head(10))

    # Handle sex column
    if "Sex" in df.columns:
        print("\Sex column before preprocessing")
        print(df["Sex"].head(10))
        df["Sex"]=pd.to_numeric(df["Sex"],errors = "coerce")
        
        print("Sex column after preprocessing")
        print(df["Sex"].head(10))

    DisplayInfo("Data after preprocessing : ")
    print(df.head())

    print("\nMising Values after preprocessing"+df.isnull().sum())


    return df

#__________________________________________________________
# Function Name : MarvellousTitanicLogistic
# Description   : Main Pipeline Controller 
#                   Loads dataset 
#                   Shows data
#                   Preprocesses dataset & train the model                 
# Parameters    : Datapath of dataset file
# Return        : NONE
# Date          : 14/03/2026
# Author        : Aryan Hanumant Kakade 
#__________________________________________________________
def MarvellousTitanicLogistic(Datapath):
    DisplayInfo("Step 1 : Loading the Dataset")
    df = pd.read_csv(Datapath)
    
    ShowData(df,"Initial Dataset")
    df = CleanTitanicData(df)




#__________________________________________________________
# Function Name : main
# Description : starting point of application
# Parameters : NONE
# Return : NONE
# Date : 14/03/2026
# Author : Aryan Hanumant Kakade 
#__________________________________________________________
def main():
    MarvellousTitanicLogistic("MarvellousTitanicDataset.csv")

if __name__=="__main__":
    main()