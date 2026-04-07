import pandas as pd
import numpy as np

# has functions to store on HDD
import joblib 

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score,confusion_matrix

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
    print(df.columns.to_List())
    
    print("\nMissing Values of each column : ")
    print(df.isNull().sum())




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