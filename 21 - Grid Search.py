# Import libraries
from sklearn.linear_model import Ridge
from sklearn.model_selection import GridSearchCV

# Create dictionary of parameter values
parameters1 = [{'alpha': [0.001, 0.1, 1, 10, 100, 1000, 10000, 100000, 1000000]}]

# Create ridge regression object/ model
RR = Ridge()

# Create a grid search cv object - inputs are the ridge regression object, the parameter values and the number of folds. We will use the R2 - this is the default scoring method
Grid1 = GridSearchCV(RR, parameters1, cv = 4)

# Fit the object
Grid1.fit(x_data[['horsepower', 'curb-weight', 'engine-size', 'highway-mpg']], y_data)

# We can find the best values for the free parameters using the attribute 'best_estimator_'
Grid1.best_estimator_

# We can also get information like the mean score on the validation data using the attribute 'cv_results_'
score = Grid1.cv_results_
scores['mean_test_score']

# Output is an array



# Ridge regression also has the option to normalise the data
from sklearn.linear_model import Ridge
from sklearn.model_selection import GridSearchCV

parameters2 = [{'alpha': [0.001, 0.1, 1, 10, 100], 'normalise': [True, False]}]

RR = Ridge()

Grid1 = GridSearchCV(RR, parameters2, cv = 4)

Grid1.fit(x_data[['horsepower', 'curb-weight', 'engine-size', 'highway-mpg']], y_data)

Grid1.best_estimator_

scores = Grid1.cv_results_

# You can print out the score of the different free parameter values
from param, mean_val, mean_test unzip(scores['params'], scores['mean_test_result'], scores['mean_train_score']):
   print(param, 'R-squared on test data:', mean_val, 'R-squared on train data:', mean_test)
