# AKA regression plots. Refer to notes for model and plot examples + explanation
# There are many ways to do this, but a simple way is to use 'regplot' in seaborn
import matplotlib as plt
import seaborn as sns

sns.regplot(x = 'highway-mpg', y = 'price', data = auto_df)
plt.pyplot.ylim(0, )
plt.pyplot.savefig('/home/hayley/Documents/Python/Python Graphs/Regression Plot.png')

 Alternative method:
# Regression plot
%matplotlib inline
import seaborn as sns

width = 12
height = 10
figsize = (width, height)
plt.pyplot.figure(figsize = (width, height))
sns.regplot( x = 'higway-mpg', y = 'price', data = auto_df)
plt.pyplot.ylim(0, )

# Output shows that price is negitively correlated to highway-mpg. Keep in mind when looking at a regression plot - pay attention to how scattered the data points are around
# the regression line. This gives you a good indication of the variance of the data and whether a linear model is the best fit or not.


# Compare this plot to the regression plot of 'peark-rpm'
%matplotlib inline
import seaborn as sns

width = 12
height = 10
plt.pyplot.figure(figsize = (width, height))
sns.regplot(x = 'peak-rpm', y = 'price', data=auto_df)
plt.pyplot.ylim(0, )
plt.pyplot.savefig('/home/hayley/Documents/Python/Python Graphs/Regression Plot 2.png')

# you can see that the points for this plot make it much harder to determine if the points are decreasing or increasing




# Residual Plots:
# Represents the error between the actual value and the predicted value using residplot
import seaborn as sns

sns.residplot(auto_df['highway-mpg'], auto_df['price'])
# Output appears to have curvature (the residuals are not randomly spread around the x-axis), meaning that a non-linear model might be more appopriate for the data

# Alternative method for same residual plot:
%matplotlib inline
import seaborn as sns

width = 12
height = 10
plt.pyplot.figure(figsize = (width, height))
sns.regplot(auto_df['highway-mpg'], auto_df['price'])
plt.pyplot.savefig('/home/hayley/Documents/Python/Python Graphs/Residual Values Plot.png')
plt.pyplot.show()





# Distribution plot:
# 'ax' refers to the axis
import seaborn as sns

ax1 = sns.distplot(auto_df['price'], hist = False, color = 'r', label = 'Actual Value')
sns.distplot(Yhat, hist = False, color = 'b', label = 'Fitted Values', ax = ax1)
