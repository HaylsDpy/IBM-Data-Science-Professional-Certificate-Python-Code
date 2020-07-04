# Unlike a histogram, a bar chart is commonly used to compare the values of a variable at a given point in time.
# E.g. visualising, in a discrete fashion, how immigration from Iceland to Canada looked from 1980-2013.

import matplotlib as mpl
import matplotlib.pyplot as plt

year = list(map(str, range(1980, 2014)))

df_iceland = df_canada.loc['Iceland', years]

df_iceland.plot(kind = 'bar')
plt.title('Iceland Immigrants to Canada from 1980 to 2013')
plt.xlabel('Year')
plt.ylabel('Number of Immigrants')
plt.show()
