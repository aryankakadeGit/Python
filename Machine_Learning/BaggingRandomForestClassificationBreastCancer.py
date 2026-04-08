import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score,classification_report,confusion_matrix

#######################################################################
# Step 1 : Load the Dataset
#######################################################################
df = pd.read_csv("breast_cancer.csv")
print("Shape of dataset : ",df.shape)
print("First 5 entries of dataset : ",df.head())

#######################################################################
# Step 2 : Separate features and labels
#######################################################################
X=df.drop("target",axis=1)
Y=df["target"]

#######################################################################
# Step 3 : Split dataset for training and testing
#######################################################################
X_train,X_test,Y_train,Y_test=train_test_split(X,Y,test_size=0.2,random_state=42)

#######################################################################
# Step 4 : Create Random forest model
#######################################################################
RF_model = RandomForestClassifier(random_state=42,n_estimators=10)


#######################################################################
# Step 5 : Train model
#######################################################################
RF_model.fit(X_train,Y_train)

#######################################################################
# Step 6 : Test model
#######################################################################
Y_pred = RF_model.predict(X_test)

#######################################################################
# Step 7 : Evaluate bagging model
#######################################################################
print("RF accuracy : ")
print(accuracy_score(Y_test,Y_pred))
print("Confusion MAtrix : ")
print(confusion_matrix(Y_test,Y_pred))
