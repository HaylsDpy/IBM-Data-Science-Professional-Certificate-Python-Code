# Use corr() to calculate the correlation between variables of type 'int64' or 'float64'
# Can use this function to back up any plots with the numerical data
# The 'diagonal' elements always = 1
auto_df.corr()
# To find the correlation between the following columns:
auto_df[['bore', 'stroke', 'compression-ratio', 'horsepower']].corr()

# Use scatterplot in seaborn to visualise the relationship between variables. This plot includes an added linear line (line of regression)

# Example of positive linear relationship: correlation between two features (engine-size and price)
# This graph shows a positive linear relationship
# ylim() get or set the y-limits of the current axes.
import matplotlib as plt
import seaborn as sns

sns.regplot(x = 'engine-size', y = 'price', data = auto_df)
pyplot.ylim(0, )
pyplot.savefig('/home/hayley/Documents/Python/Python Graphs/Positive Correlation Scatter.png')


# Example of negative linear relationship: correlation between two features (highway-mpg and price)
# This graph shows a strong negative correlation, however, as the line of regression is still steep, it can still be used as an indicator of price
import matplotlib as plt
import seaborn as sns

sns.regplot(x = 'highway-mpg', y = 'price', data = auto_df)
pyplot.ylim(0, )
pyplot.savefig('/home/hayley/Documents/Python/Python Graphs/Strong Negative Correlation Scatter.png')


# Example of weak correlation between two features (peak-rpm and price)
# Result means that you cannot use peak-rpm to predict car price
import matplotlib as plt
import seaborn as sns

sns.regplot(x = 'peak-rpm', y = 'price', data = auto_df)
pyplot.ylim(0, )
pyplot.savefig('/home/hayley/Documents/Python/Python Graphs/Weak Correlation Scatter.png')


# Pearsons r calculation using horsepower and price
# Result shows a strong positive correlation between the two variables
from scipy import stats

pearson_coef, p_value = stats.pearsonr(auto_df['horsepower'], auto_df['price'])

pearson_coef, p_value

# Another pearson example:
from scipy import stats

pearson_coef, p_value = stats.pearsonr(auto_df['wheel-base'], auto_df['price'])
print('The Pearson Correlation Coefficient is', pearson_coef, 'with a P-value of P =', p_value)
