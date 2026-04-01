import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier,plot_tree
from sklearn.metrics import (accuracy_score,confusion_matrix,classification_report,ConfusionMatrixDisplay)
border = "-"*40
#---------------------------------------------------------------------------------------------------------#
#                                       1 : Load the Dataset
#---------------------------------------------------------------------------------------------------------#

print(border)
print("Step 1 : Load the Dataset")
print(border)
Dataset_path = "iris.csv"
df = pd.read_csv(Dataset_path)
print("Dataset Gets Loaded Succesfully")
print("Initial Entries from dataset : ")
print(df.head())

#---------------------------------------------------------------------------------------------------------#
#                                       2 : Data Analysis(EDA)
#---------------------------------------------------------------------------------------------------------#

print(border)
print("Step 2 : Data Analysis(EDA)")
print(border)
print("Shape of Dataset : ",df.shape)
print("Column names : ",list(df.columns))
print("Missing Values (Per column ) : ")
print(df.isnull().sum())
print("Class Distribution(Species count)")
print(df["species"].value_counts())
print("Statistical report od dataset")
print(df.describe())


#---------------------------------------------------------------------------------------------------------#
#                              3 : Decide Independant And Dependant Variables
#---------------------------------------------------------------------------------------------------------#

print(border)
print("Step 3 : Decide Independant And Dependant Variables")
print(border)

Feature_cols = [
    "sepal length(cm)",
    "sepal width(cm)",
    "petal length(cm)",
    "petal width(cm)"
]
X = df[Feature_cols]
Y = df["species"]

print("X shape : ",X.shape)
print("Y shape : ",Y.shape)

#---------------------------------------------------------------------------------------------------------#
#                                       4 : Visualization of dataset
#                                               (Scatter Plot)
#---------------------------------------------------------------------------------------------------------#

print(border)
print("Step 4 : Visualization of dataset")
print(border)

plt.figure(figsize=(7,5))
for sp in df["species"].unique():
    temp = df[df["species"]==sp]
    plt.scatter(temp["petal length(cm)"],temp["petal width(cm)"],label = sp)

plt.title("Iris : Petal Length vs Petal Width")
plt.xlabel("petal length(cm)")
plt.ylabel("petal width(cm)")
plt.legend()
plt.grid(True)
plt.show()













