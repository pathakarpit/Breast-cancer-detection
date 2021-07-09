import pandas as pd
import numpy as np

#importing the dataset
dataset = pd.read_csv('breast_cancer.csv')
X = dataset.iloc[:,1:-1].values
y = dataset.iloc[:,-1].values

#splitting the test case and training set
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.05)

# training the logistic regression model on the training set
from sklearn.linear_model import LogisticRegression
classifier = LogisticRegression(random_state=(0))
classifier.fit(X_train, y_train)

#predicting the test set
y_pred = classifier.predict(X_test)

#making the confusion matrix
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test, y_pred)
print(cm)

#computing the accuracy with k-fold cross validation
from sklearn.model_selection import cross_val_score
accuracies = cross_val_score(estimator = classifier, X = X_train, y = y_train, cv = 10)
print("Accuracy : {:.2f} %".format(accuracies.mean()*100))
print("Standard deviation : {:.2f} %".format(accuracies.std()*100))