# As before, 100% refer to notes in notebook for this

from sklearn.linear_model import LinearRegression

# Extract the four predictor variables and store them in the variable 'z'
z = auto_df[['horsepower', 'curb-weight', 'engine-size', 'highway-mpg']]

# Train the model, as in simple linear regression model, using the target/ dependent variable
lm.fit(z, auto_df['price'])

# Alternative method to the above:
lm2 = LinearRegression()
lm2.fit(auto_df[['horsepower', 'curb-weight', 'engine-size', 'highway-mpg']], auto_df['price'])



# Obtain a prediction
Yhat = lm.predict(z)

# Find the intercept (b0)
lm.intercept_

# Find the coefficients (b1, b2, b3, b4)
lm.coef_

# Output is an array
# Estimated linear model is as follows, based on the numbers output and the equation: 'yhat' = b0 + b1 x1 + b2 x2 + b3 x3 + b4 x4
# Price = 15678.74 + (52.66) * 'horsepower' + (4.70) * 'curb-weight' + (81.96) * 'engine-size' + (33.58) * 'highway-mpg'



# How do you visualise a model for MLR? (Can't visualise using regression or a residual plot)
# One way is to look at the distribution plot
# Make a prediction first:
yhat = lm.predict(z)

# Make plot
%matplotlib inline
import seaborn as sns

width = 12
height = 10
plt.pyplot.figure(figsize = (width, height))

ax1 = sns.distplot(auto_df['price'], hist = False, color = 'r', label = 'Actual Value')
sns.distplot(Yhat, hist = False, color = 'b', label = 'Fitted Values', ax = ax1)

plt.pyplot.title('Actual vs Predicted Values for Car Price')
plt.pyplot.xlabel('Price - in US Dollars')
plt.pyplot.ylabel('Proportion of Cars')
plt.pyplot.savefig('/home/hayley/Documents/Python/Python Graphs/MLR Distribution Plot.png')

plt.pyplot.show()
plt.pyplot.close()

# You can see that the fitted values are reasonably close to the actual values as the two lines overlap a bit. However, there is definitely room for improvement
