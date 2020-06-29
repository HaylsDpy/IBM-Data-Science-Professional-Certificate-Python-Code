import numpy as np
import pandas as pd

filename = '/home/hayley/Documents/Data Analysis/imports-85.csv'

auto_df = pd.read_csv(filename, header = None)

auto_df.head()

# Reads from the bottom of the table, instead of from the top as head() does
auto_df.tail()

# Method to find only numeric data
auto_df._get_numeric_data()

# To replace default header names
auto_df.columns = headers

headers = ['symboling', 'normalised-losses', 'make', 'fuel-type', 'aspiration', 'num-of-doors', 'body-style', 'drive-wheels', 'engine-location', 'wheel-base',
   'length', 'width', 'height', 'curb-weight', 'engine-type', 'num-of-cylinders', 'engine-size', 'fuel-system', 'bore', 'stroke', 'compression-ratio', 'horsepower',
   'peak-rpm', 'city-mpg', 'highway-mpg', 'price']

# Checking data types
auto_df.dtypes()

# Statistical summary
auto_df.describe()

# Statistical summary of full data set - including strings/objects
auto_df.describe(include = 'all')
# Or specify that you want to look at the values for objects
auto_df.describe(include = ['object'])

# To obtain a concise summary of yotur DataFrame
auto_df.info()

# Drop missing values along a single column - when using an axis argument, 1 refers to columns, 0 refers to rows - 0 is usually default(?)
auto_df.dropna(subset = ['price'], axis = 0)

# Get names of columns
print(auto_df.columns)
# or
print(list(auto_df.columns))

# Select the columns of a DataFrame by indicating the name of each column:
# auto_df[['column 1', 'column 2', 'column 3']]
auto_df[['symboling', 'num-of-doors', 'price']]

# Where 'Column' is the name of the column, you can apply the method .describe() to get the stats of those columns
# auto_df[['column 1', 'column 2', 'column 3']].describe()

auto_df[['symboling', 'num-of-doors', 'price']].describe()

# Access a columns by specifying the name of the column:
auto_df['symboling']
auto_df['body-style']

# Add 1 to each value in a column
auto_df['symboling'] = auto_df['symboling'] + 1

# Drop values in a DataFrame
auto_df.dropna(axis = 0) # Rows

auto_df.dropna(axis = 1) # Columns

# E.g. in this scenario, we're trying to look at car prices. If an entry is missing a value, you would have to drop that entry (or row) as the rest of the data
# in that row is useless to you without the price
# 'inplace = True' allows for the modification to take place on the DataFrame directly
auto_df.dropna(subset = ['price'], axis = 0, inplace = True)
# Reset index, because the above code dropped two rows:
auto_df.reset_index(drop = True, inplace = True)

# Convert '?' to 'NaN':
auto_df.replace('?', np.nan, inplace = True)

# Detect missing data using two methods - isnull() and notnull():
missing_data = auto_df.isnull()

# Count the missing values in each column:
for column in missing_data.columns.values.tolist():
   print(column)
   print(missing_data[column].value_counts())
   print(' ')

# Replacing missing values in DataFrames:
# One option is to replace missing values with the mean of that variable. I.e calculate the mean of the entire column and replace missing values with that
# First, calculate the mean for the column
mean = auto_df['normalised-losses'].mean()
# Then use the NumPy replace() function
auto_df['normalised-losses'].replace(np.nan, mean)

# Or, replace the missing value with the most frequent within the column (in this case, four is the most frequent):
auto_df['num-of-doors'].replace(np.nan, 'four', inplace = True)



# Convert all data types to their proper format:
auto_df[['bore', 'stroke']] = auto_df[['bore', 'stroke']].astype('float')
auto_df[['normalised-losses']] = auto_df[['normalised-losses']].astype('int')
auto_df[['price']] = auto_df[['price']].astype('float')
auto_df[['peak-rpm']] = auto_df[['peak-rpm']].astype('float')
# List the types after conversion to check that it is all correct:
auto_df.dtypes()


# Calculating the average of the column (convert the answer to a float):
avg_norm_loss = auto_df['normalised-losses'].astype('float').mean(axis = 0)
print('Average of normalised-losses:', avg_norm_loss)
# Replace 'NaN' with mean value in 'normalised-losses' column:
auto_df['normalised-losses'].replace(np.nan, avg_norm_loss, inplace = True)

# To see which values are present in a particular column, we can use the value_counts() function:
auto_df['num-of-doors'].value_counts()

# We can also use idxmax() to calculate which value is the most frequent within the column:
auto_df['num-of-doors'].value_counts().idxmax()

# Converting values in a column/ applying calculations to an entire column:
# E.g. transform 'mpg' to 'litres per km'
auto_df['city-mpg'] = 235/auto_df['city-mpg']

auto_df.rename(columns = {'city-mpg': 'city-L/100km'}, inplace = True)
# Alternative method:
auto_df['city-L/100km'] = 235/auto_df['city-mpg']


# Methods of normalising data - refer to notebook for equations:
# With Pandas - to normalise 'length' in car data set
auto_df['length'] = auto_df['length'] / auto_df['length'].max()
# Min-max method with Pandas
auto_df['length'] = (auto_df['length'] - auto_df['length'].min()) / (auto_df['length'].max() - auto_df['length'].min())
# Z-score method with Pandas
auto_df['length'] = (auto_df['length'] - auto_df['length'].mean()) / auto_df['length'].std())


# Binning:
# E.g. binning the car prices into three groups - high, medium and low
# First, you want to create 3 bins of equal 'bin width', so, you need 4 numbers as dividers that are an equal distance appart. Do this by using NumPy linspace()
# function to return the array 'bins' that contains 4 equally spaces numbers over the specified variable of 'price'
bins = np.linspace(min(auto_df['price']), max(auto_df['price']), 4)
# Create a list called 'group_names' that contains the desired bin names
group_names = ['Low', 'Medium', 'High']
# Use Pandas function cut() to segment and sort the data values into the bins
auto_df['price-binned'] = pd.cut(auto_df['price'], bins, labels = group_names, include_lowest = True)


# Use dummy variables to convert categorical variables to a useable format:
# I.e. covert fuel values from 'gas' and 'diesel' to '0' and '1'. This enables for easier further analysis
dummy_variable_1 = pd.get_dummies(auto_df['fuel-type'])
# To change column names:
dummy_variable_1.rename(columns = {'fuel-type-diesel': 'gas', 'fuel-type-diesel': 'diesel'}, inplace = True)
dummy_variable_1.head()
# To merge this new DataFrame with the original DataFrame (auto_df):
auto_df = pd.concat([auto_df, dummy_variable_1], axis = 1)
# Drop original column 'fuel-type' from 'auto_df':
auto_df.drop('fuel-type', axis = 1, inplace = True)


# Example: have a look at the values within a column using value_counts():
auto_df['drive-wheels'].value_counts()
# If you wish, you can convert the above series to a dataframe:
auto_df['drive-wheels'].value_counts().to_frame()
# Example, repeating the above steps, but saving the results to a dataframe with the name 'drive_wheels_counts' and rename the column 'drive_wheels' to 'value_counts
drive_wheels_counts = auto_df['drive_wheels'].value_counts.to_frame()
drive_wheels_counts.rename(columns = {'drive-wheels': 'value_counts'} inplace = True)
drive_wheels_counts
# Rename the index to 'drive-wheels':
drive_wheels_counts.index.name = 'drive_wheels'
drive_wheels_counts



# After all data cleaning is complete, save the new dataframe to a new csv file:
auto_df.to_csv('Clean_auto_df.csv')
