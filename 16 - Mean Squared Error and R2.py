# Refer to notebok for explanations
# MSE: Generally the values of the MSE are between 0 and 1
# Simple Linear Regression:
x = auto_df[['highway-mpg']]
y = auto_df['price']

yhat = lm.predict(x)
print('The output of the first 4 predicted value is:', yhat[0:4])

from sklearn.metrics import mean_squared_error

# Compare the predicted results with the actual results
mse = mean_squared_error(auto_df['price'], yhat)
print('The mean square error of price and predicted value is:', mse)

# Find R2 value:
# Calculate as follows using the score() method
x = auto_df[['highway-mpg']]
y = auto_df['price']

lm.fit(x, y)

print('The R-square is:', lm.score(x, y)

# From the value that we get from this example (0.496591188), we can say that approx. 49.695% of the variation of price is eplained by the simple linear model
# R2 is generally between 0 and 1. If your R2 is negative, it can be due to overfitting



# Multiple Linear Regression R2:
z = auto_df[['horsepower', 'curb-weight', 'engine-size', 'highway-mpg']]

# Fit the model
lm.fit(z, auto_df['price'])

# Find the R2
# Output: we can say that ~80.896% of the variation of price is explained by this multiple linear regression 'mulit-fit'
print('The R-square is:', lm.score(z, auto_df['price']))

# Calculate the MSE
# Produce a prediction
y_predict_multifit = lm.predict(z)

# Compare the predicted results with the actual results
print('The mean square error of price and predicted value using multifit is:', mean_squared_error(auto_df['price'], y_predict_multifit))


# Polynomial Fit R2:
# Calculate the R2
from sklearn.metrics import r2_score

f = np.polyfit(x, y, 3)
p = np.polyld(f)

x = auto_df[['highway-mpg']]
y = auto_df['price']

# Apply the function to get the value of R2
r_squared = r2_score(y, p(x))
print('The R-square value is:', r_squared)

# Calculate the MSE
mean_squared_error(auto_df['price'], p(x))
