# Details in notebook for full box plot description
# Create box plot for 'drive-wheels' and 'price'

import seaborn as sns

sns.boxplot(x = 'drive-wheels', y = 'price', data = auto_df)
pyplot.savefig('/home/hayley/Documents/Python/Python Graphs/Sample Box Plot.png')
