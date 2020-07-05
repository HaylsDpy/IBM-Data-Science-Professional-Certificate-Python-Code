# A scatter plot is a type of plot that displays values pertaining to, typically, two variables against each other. Usually is it a dependent variable to be plotted against
# an independent variable in order to determine if any correlation between the two variables exists.

# Say we're interested in plotting a scatter plot of the total annual immigration to Canada from 1980 to 2013.
# To be able to do this, we need to create a new dataframe that shows each year and the corresponding total number of immigrants from all the countries world wide.

import matplotlib as mpl
import matplotlib.pyplot as plt

df_total.plot(
   kind = 'scatter',
   x = 'year',
   y = 'total'
)

plt.title('Total Immigrant Population to Canada from 1980-2013')
plt.xlabel('Year')
plt.ylabel('Number of Immigrants')
plt.show()
