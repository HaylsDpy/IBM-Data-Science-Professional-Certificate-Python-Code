# groupby() can be applied on categorical variables and groups the data into subsets according to the different catergories of that variable
# Can group a single variable or multiple cariables
# Find the average price of vehicles and observe how they differe between different body styles and drive systems variables

# Pick out the columns you are interested in
df_test = auto_df[['drive-wheels', 'body-style', 'price']]

# Group the reduced data according to 'drive-wheels' and 'body-style'. Use mean() to take the mean of each group to see hoe the average price differs across the board
# 'as_index = False' indicates to groupby() that you don't want to set the column ID as the index
df_group = df_test.groupby(['drive-wheels', 'body-style'], as_index = False).mean()

# Have a look at the new table
print(df_group)


# TO MAKE THIS TABLE EASIER TO READ - CONVERT IT TO A PIVOT TABLE - NEXT DOCUMENT



# Another method is to use unique() when grouping to have a look at the catergories within a column
auto_df['drive-wheels'].unique
# Select the columns that you want to compare and assign to a new variable
df_group_one = auto_df[['drive-wheels', 'body-style', 'price']]
# Calculate the average price for each of the different categories
df_group_one = df_group_one.groupby(['drive-wheels'], as_index = False).mean()
df_group_one


# You can also group with multiple variables. Group by both 'drive-wheels' and 'body-style'. This groups the dataframe by the unique combinations. Store the result in a new
# variable.
df_gptest = auto_df[['drive-wheels', 'body-style', 'price']]
grouped_test_two = df_gptest.groupby(['drive-wheels', 'body-style'], as_index = False).mean()
grouped_test_two
