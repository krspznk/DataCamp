# Import pandas
# ... YOUR CODE FOR TASK 1 ...
import pandas as pd

# Load dataset
cc_apps = pd.read_csv("datasets/cc_approvals.data", header=None)

# Inspect data
# ... YOUR CODE FOR TASK 1 ...

print(cc_apps.head())

# Print summary statistics
cc_apps_description = cc_apps.describe()
print(cc_apps_description)

print('\n')

# Print DataFrame information
cc_apps_info = cc_apps.info()
print(cc_apps_info)

print('\n')

# Inspect missing values in the dataset
# ... YOUR CODE FOR TASK 2 ...
print(cc_apps.isna().sum().tail(17))


# Import train_test_split
# ... YOUR CODE FOR TASK 3 ...
from sklearn.model_selection import train_test_split
# Drop the features 11 and 13
cc_apps = cc_apps.drop([11, 13], axis=1)

# Split into train and test sets
cc_apps_train, cc_apps_test = train_test_split(cc_apps, test_size=0.33, random_state=42)
# Import numpy
# ... YOUR CODE FOR TASK 4 ...
import numpy as np
# Replace the '?'s with NaN in the train and test sets
cc_apps_train = cc_apps_train.replace("?", np.nan)
cc_apps_test = cc_apps_test.replace("?", np.nan)
# Impute the missing values with mean imputation
cc_apps_train[[2,7,10,14]].fillna(cc_apps_train[[2,7,10,14]].mean, inplace=True)
cc_apps_test[[2,7,10,14]].fillna(cc_apps_test[[2,7,10,14]].mean, inplace=True)

# Count the number of NaNs in the datasets and print the counts to verify
# ... YOUR CODE FOR TASK 5 ...
print(cc_apps_train.isnull().sum())
print(cc_apps_test.isnull().sum())
# Iterate over each column of cc_apps_train
for col in cc_apps_train.columns:
    # Check if the column is of object type
    if cc_apps_train[col].dtype == 'object':
        # Impute with the most frequent value
        cc_apps_train = cc_apps_train.fillna(cc_apps_train[col].value_counts().idxmax())
        cc_apps_test = cc_apps_test.fillna(cc_apps_train[col].value_counts().idxmax())

# Count the number of NaNs in the dataset and print the counts to verify
# ... YOUR CODE FOR TASK 6 ...
print(cc_apps_train.isna().sum())
print(cc_apps_test.isna().sum())
# Convert the categorical features in the train and test sets independently
cc_apps_train = pd.get_dummies(cc_apps_train)
cc_apps_test = pd.get_dummies(cc_apps_test)

# Reindex the columns of the test set aligning with the train set
cc_apps_test = cc_apps_test.reindex(columns=cc_apps_train.columns, fill_value=0)
print(cc_apps_test)
print(cc_apps_train)
# Import MinMaxScaler
# ... YOUR CODE FOR TASK 8 ...
from sklearn.preprocessing import MinMaxScaler
# Segregate features and labels into separate variables
X_train, y_train = cc_apps_train.iloc[:, :-1].values, cc_apps_train.iloc[:, [-1]].values
X_test, y_test = cc_apps_test.iloc[:, :-1].values, cc_apps_test.iloc[:, [-1]].values

# Instantiate MinMaxScaler and use it to rescale X_train and X_test
scaler = MinMaxScaler()
rescaledX_train = scaler.fit_transform(X_train)
rescaledX_test = scaler.transform(X_test)
# Import LogisticRegression
# ... YOUR CODE FOR TASK 9 ...
from sklearn.linear_model import LogisticRegression
# Instantiate a LogisticRegression classifier with default parameter values
logreg = LogisticRegression()

# Fit logreg to the train set
# ... YOUR CODE FOR TASK 9 ...
logreg.fit(X_train, y_train)
# Import confusion_matrix
# ... YOUR CODE FOR TASK 10 ...
from sklearn.metrics import confusion_matrix
# Use logreg to predict instances from the test set and store it
y_pred = logreg.predict(X_test)

# Get the accuracy score of logreg model and print it
print("Accuracy of logistic regression classifier: ", logreg.score(X_test, y_test))

# Print the confusion matrix of the logreg model
# ... YOUR CODE FOR TASK 10 ...
print(confusion_matrix(y_test, y_pred))
# Import GridSearchCV
# ... YOUR CODE FOR TASK 11 ...
from sklearn.model_selection import GridSearchCV
# Define the grid of values for tol and max_iter
tol = [0.01, 0.001, 0.0001]
max_iter = [100, 150, 200]

# Create a dictionary where tol and max_iter are keys and the lists of their values are corresponding values
param_grid = {"tol": tol, "max_iter": max_iter}
# Instantiate GridSearchCV with the required parameters
grid_model = GridSearchCV(estimator=logreg, param_grid=param_grid, cv=5)

# Fit grid_model to the data
grid_model_result = grid_model.fit(rescaledX_train, y_train)

# Summarize results
best_score, best_params = grid_model_result.best_score_, grid_model_result.best_params_
print("Best: %f using %s" % (best_score, best_params))

# Extract the best model and evaluate it on the test set
best_model =grid_model_result.best_estimator_
print("Accuracy of logistic regression classifier: ", best_model.score(rescaledX_test,y_test))