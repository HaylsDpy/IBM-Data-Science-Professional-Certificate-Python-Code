# A histogram is a way of representing the frquency distribution of a variable. The histogram partitions the spread of the numeric data into 'bins', assigns each data point in
# the dataset to a bin and then counts the number of data points that have been assignes to each bin.

# Visualise the distribution of immigrants to Cnada in the year 2013
import matplotlib a mpl
import matplotlib.pyplot as plt

df_canada['2013'].plot(kind = 'hist')

plt.title('Histogram of Immigration from 195 Countries in 2013')
plt.ylabel('Number of Countries')
plt.xlabel('Number of Immigrants')
plt.show()

# Notice that the bins are not aligned with the tick marks on the x axis. This can make the histogram hard to read. One way to fix this is to use the NumPy histogram function:
import matplotlib a mpl
import matplotlib.pyplot as plt
import numpy as np

count, bin_edges = np.histogram(df_canada['2013'])

df_canada['2013'].plot(kind = 'hist', xticks = bin_edges)

plt.title('Histogram of Immigration from 195 Countries in 2013')
plt.ylabel('Number of Countries')
plt.xlabel('Number of Immigrants')
plt.show()
