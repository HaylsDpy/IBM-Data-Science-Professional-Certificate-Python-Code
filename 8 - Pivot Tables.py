# USING TABLE FROM LAST DOCUMENT
# Pivot tables: one variable displayed along the columns and other variable displayed along the rows

df_pivot = df_group.pivot(index = 'drive-wheels', columns = 'body-style')

df_pivot

# Use fillna() to fill any NaN values with zero:
df_pivot = df_pivot.fillna(0)
df_pivot
