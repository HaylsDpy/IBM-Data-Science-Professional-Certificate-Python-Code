# Generate area plots for the countries with the highest number of immigration to Canada.
# We can try to find these countries by sorting the dataframe in descending order of cummulative total immigration from 19800 to 2013.
df_canada.sort_values(['Total'], ascending = False, axis = 0, inplace = True)

# Now create a new dataframe with these top 5 countries and excluding the 'total' column
# We want 'Years' to be plotted on the x axis and 'Annual immigration' on the y axis. (Note that Matplotlib plots the indices of a df on the x axis)
df_top5 = df_canada.head()

# Transpose the dataframe
df_top5 = df_top5[years].transpose()

# Generate the plot
import matplotlib as mpl
import matplotlib.pyplot as plt

df_top5.plot(kind = 'area')

plt.title('Immigration trend of top 5 countries')
plt.ylabel('Number of immigrants')
plt.xlabel('Years')

plt.show()
