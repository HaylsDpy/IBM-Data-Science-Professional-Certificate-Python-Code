# A box plot is a way of statistically representing the distribution of given data via the dimensions: minmum, first quartile, median, third quartile and maximum.
# Say we're interested in creating a box plot to visualise immigration from Japan to Canada.

import matplotlib as mpl
import matplotlib.pyplot as plt

df_japan - df_canada.loc[['Japan'], years].transpose()
df_japan.plot(kind = 'box')

plt.title('Box plot of Japanese Immigrants from 1980-2013')
plt.ylabel('Number of Immigrants')
plt.show()
