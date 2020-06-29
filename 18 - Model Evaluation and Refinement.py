# Refer to notebook for further notes

# An important step in testing your model is to split your data into training and testing data. We will place the target data price in a separate dataframe y:
y_data = df['price']
# drop price data in x data
x_data = df.drop('price',axis = 1)

# Model evaluation - in sample evaluation:
# The train_test_split() function splits data into random train and test subsets
from sklearn.model_selection import train_test_split

# From example code snippet
x_train, x_test, y_train, y_test = train_test_split(x_data, y_data, test_size = 0.3, random_state = 0)

print("Number of test samples :", x_test.shape[0])
print("Number of training samples:",x_train.shape[0])


# Cross Validation:
# The cross_val_score() function performs multiple out-of-sample evaluations
from sklearn.model_selection import cross_val_score

# 1st input parameter: 'lr' refers to the type of model we are using to do the cross validation (in this case, a linear regression model/object)
# Other parameters: 'x_data' (the predictive variable data), 'y_data' (the target variable data)
# Manage the number of partitions/ folds via the 'cv' parameter
scores = cross_val_score(lr, x_data[['horsepower']], y_data, cv = 3)

scores

# Use the Numpy mean() function to average the result together to estimate  the out-of-sample R^2
np.mean(scores)
# OR
print("The mean of the folds are", Rcross.mean(), "and the standard deviation is" , Rcross.std())

# We can use negative squared error as a score by setting the parameter 'scoring' metric to 'neg_mean_squared_error'.
-1 * cross_val_score(lr,x_data[['horsepower']], y_data,cv=4,scoring='neg_mean_squared_error')



# cross_val_predict() function:
# Has a similar interface to cross_val_score() - function returns the prediction that was obtaines for each element when it was in the test set
from sklearn.model_selection import cross_val_predict

# Input is exactly the same as the cross_val_score() function, but the output is a prediction
yhat = cross_val_predict(lr2e, x_data, y_data, cv = 3)


# Create plots: Let's perform some model evaluation using our training and testing data separately. First we import the seaborn and matplotlibb library for plotting.
import matplotlib.pyplot as plt
%matplotlib inline
import seaborn as sns

# Let's examine the distribution of the predicted values of the training data.
Title = 'Distribution Plot of Predicted Value Using Training Data vs Training Data Distribution'
DistributionPlot(y_train, yhat_train, "Actual Values (Train)", "Predicted Values (Train)", Title)
