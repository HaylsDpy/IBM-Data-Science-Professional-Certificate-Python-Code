# Using the describe() function in Pandas:
# Only displays numbers for numeric values in a DataFrame. Any Nan entires are automatically omitted.
auto_df.describe()

# Using the value_counts() function:
# Summarises categorical data. E.g. 'drive-system' consists of 3 categories: 'forward-wheel-drive', 'rear-wheel-drive' and 'four-wheel-drive'
drive_wheels_count = auto_df['drive-wheels'].value_counts()
# Rename the columns of the new DF to make the table easier to read
drive_wheels_count.rename({'drive_wheels': 'value_counts'}, inplace = True)

drive_wheels_count.index.name = 'drive_wheels'
