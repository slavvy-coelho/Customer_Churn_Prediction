
# Load libraries
import pandas as pd
from sklearn.ensemble import RandomForestClassifier, AdaBoostClassifier
from sklearn.model_selection import train_test_split # Import train_test_split function
from sklearn import metrics #Import scikit-learn metrics module for accuracy calculation
import numpy as np
import sys

final = pd.read_csv("final.csv")

feature_cols_red = ["bd","registration_init_time","num_100"]
X_red = final[feature_cols_red] # Features
y_red = final.is_churn # Target variable

# Split dataset into training set and test set
X_train_red, X_test_red, y_train_red, y_test_red = train_test_split(X_red, y_red, test_size=0.3, random_state=1) # 70% training and 30% test

# Create RandomForestClassifier object
clf_red = RandomForestClassifier()

# Train RandomForestClassifier Classifer
clf_red = clf_red.fit(X_train_red,y_train_red)

#Predict the response for test dataset
y_pred_red = clf_red.predict(X_test_red)

# Model Accuracy, how often is the classifier correct?
print("Accuracy:",metrics.accuracy_score(y_test_red, y_pred_red))

from sklearn.externals import joblib 
  
# Save the model as a pickle in a file 
joblib.dump(clf_red, 'model_red.pkl') 

print("Input location: ")
i = input()
ynew_red = clf_red.predict(X_test_red.iloc[[i]])
if ((ynew_red[0]) == 1):
    print("The user will churn as predicted value=%s" % (ynew_red[0]))
else:
    print("The user will not churn as predicted value=%s" % (ynew_red[0]))