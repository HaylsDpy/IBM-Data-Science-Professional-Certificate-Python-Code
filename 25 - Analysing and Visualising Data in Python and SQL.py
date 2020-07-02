# Using McDonald's menu nutritional facts data (Kaggle)
# Verify loaded data using SQL - shows that there are 260 rows of data
stmt = ibm_db.exec_immediate(conn, 'SELECT COUNT(*) FROM Mcdonalds_Nutrition')
ibm_db.fetch_both(stmt)

# Using pandas
import pandas
import ibm_db_dbi
pconn = ibm_db_dbi.Connection(conn)
df = pandas.read_sql('SELECT * FROM Mcdonalds_Nutrition', pconn)

df

# View first few rows
df.head()

# Learn about your data
df.describe(include = 'all')

# Which food item has max sodium content?
import matplotlib.pyplot as pyplot
%matplotlib inline
import seaborn as sns

# Catergorical scatter plots
plot = sns.swarmplot(x = 'Category', y = 'Sodium', data = df)
plt.setp(plot.get_xticklabels(), rotation = 70)
plt.title('Sodium Content')
plt.show()

# Note one particularly high value in chicken and fish
# Explore this further
df['Sodium'].describe()

# Now explore the row in the df associated with the maximum sodium value - result = 82
df['Sodium'].idxmax()

# Now we can find the item name associated with the 82nd item in the df - result is 'Chicken Nuggets (40 piece)'
df.at[82, 'Item']


# Further exploration using visualisations
import matplotlib.pyplot as plt
%matplotlib inline
import seaborn as sns

plot = sns.jointplot(x = 'Protein', y = 'Total Fat', data = df)
plt.show()

# Scatter plot shows a positive correlation between fat and protein content - pearsons r and p values support this
# Histogram at the top is for protein, histogram on the right is for fat

# Visualise data using box plots
plot = sns.set_style('whitegrid')
ax = sns.boxplot(x = df['Sugars'])
plot.show()
