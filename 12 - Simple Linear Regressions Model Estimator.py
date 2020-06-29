# *** NOTE: The ENTIRE point of the various regression models and the following calculations is to allow you to make better and more accurate predicitions when analysing
# the data. I.e. in business models, you want to ensure that you are making the best possible predictions/ results as possible in order to promote business and not lose money.

# 100% refer to notebook for the entire regression moduel

#Import linear_model from scikit_learn
from sklearn.linear_model import LinearRegression

# Create a linear regression object using the constructor
lm = LinearRegression()

lm

# Define the predictor variable and target variable. x = predictor, y = target
x = auto_df[['highway-mpg']]
y = auto_df[['price']]

# Use lm.fit(x, y) to fit the model (i.e. find the parameters b0 - the intercept and b1 - the slope)
lm.fit(x, y)

# Obtain a prediction using predict() - outputs an array
# The output array has the same number of samples as the input 'x'
Yhat = lm.predict(x)

# We can view the intercept value
lm.intercept_

# We can also view the slope
lm.coef_

# The relationship between price and highway is, therefore, based on the numbers output by the above code, given by the following equation
# 'yhat' = b0 - b1, x
