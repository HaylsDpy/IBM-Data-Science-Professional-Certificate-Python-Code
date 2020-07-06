# Seaborn is a Python visualisation library based on Matplotlib. It was built primarily to provide a high-lvevl interface for drawing attractive statstical graphics, such as
# regression plots, box plots etc.

# Let's say we have a dataframe, called df_total, of total immigration to Canada from 1980 to 2013 with the year in one column and the corresponding total immigration in another
# column.
# We want to create a scatter plot along with a regression line to highlight any trends in the data.

import seaborn as sns

ax = sns.regplot(x = 'year', y = 'total', data = df_total)

# Seaborn's regplot function also accepts additional parameters for any personal customisation e.g. you can change the colour using the 'color' parameter.

import seaborn as sns

ax = sns.regplot(x = 'year', y = 'total', data = df_total, color = 'green')

# You can also change the shape of the markers to '+' insted of the usual circular marker

import seaborn as sns

ax = sns.regplot(x = 'year', y = 'total', data = df_total, color = 'green', marker = '+')
