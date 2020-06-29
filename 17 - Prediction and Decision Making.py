# Example: do the predicted values make sense?
# Process:
# First, we train the model
lm.fit(auto_df['highway-mpg'], auto_df['price'])

lm

# Next we can predict the price of a car with 30 highway mpg
# Result: $13,771.30 - seems to make sense as value is not negative/ extremely high/ extremely low
lm.predict(np.array(30.0).reshape(-1, 1))

# Look at coefficient (-821.73337832)
lm.coef_

# Price = 38423.31 - 821.73 * highway-mpg
# Based on these numbers if the highway-mpg increases by 1 unit, the car price decreases by $821. This value also seems reasonable



# Example of process whilst looking at a specified range of the data - generate a sequence of values in a specified range
import matplotlib.pyplot as plt
import numpy as np

%matplotlib inline

x = auto_df['highway-mpg']
y = auto_df['price']

# Use NumPy arrange() function to generate a sequence from 1 -100
# Sequence starts at 1 and increments by 1 unit until it reaches 100
# (1, 101, 1): first 1 = starting point, 101 = end point plus 1, last 1 = step size between elements in the sequence
new_input = np.arrange(1, 101, 1), reshape(-1, 1)

# Fit the model
lm.fit(x, y)

lm

# You can use the output of this to predict new values. Output = NumPy array
yhat = lm.predict(new_input)
yhat[0:5]

# Plot the data
plt.plot(new_input, yhat)
plt.show()

# Use regression plot to visualise the data.
# The data trends down as the dependent variable increases. The plot also shows some non-linear behaviour



# Next, examine the residual plot
# Shows a curvature suggesting non-linear behaviour



# Distribution plot:
# Good for multiple linear regression.
# Shows the predictive values for prices in the range of 30,000 - 50,000 are inaccurate: a non-linear model may be more suitable, or, you may need more data in this range
