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
print(df.head()) # Displays first 5 elements










