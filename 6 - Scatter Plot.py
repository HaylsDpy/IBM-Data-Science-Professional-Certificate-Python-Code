# Used to represent categorical values. Each observation is represented as a point
# In the car data set, 'price' and 'engine-size' are categorical. Could engine size, possibly, predict the price of a car?

import matplotlib as plt

y = auto_df['price']
x = auto_df['engine-size']
pyplot.scatter(x, y)

pyplot.title('Scatterplot of Engine Size vs Price')
pyplot.xlabel('Engine Size')
pyplot.ylabel('Price')

# This graph give initial indication that there is a positive linear relationship between engine size and car price
