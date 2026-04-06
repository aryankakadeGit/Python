import matplotlib.pyplot as plt
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score,confusion_matrix,classification_report

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

    
    

def main():
    Border = "-"*40
    print(Border)
    print("Wine classifer")
    print(Border)  
    marvellousClassifier("WinePredictor.csv")



if __name__=="__main__":
    main()