# Another way to represent pivot tables
# Plot target variable over multiple variables
import matplotlib as plt

pyplot.pcolor(df_pivot, cmap = 'RdBu')
pyplot.colorbar()
pyplot.title('Avg. Price of Vehicles Depending on Body Style & Drive System')
pyplot.xlabel('Body style')
pyplot.ylabel('Drive System')
pyplot.savefig('/home/hayley/Documents/Python/Python Graphs/Sampleheatmap.png')
pyplot.show()


# Another way to plot the same char with more labels and more detail
fig, ax = pyplot.subplots()
im = ax.pcolor(df_pivot, cmap = 'RdBu')
# Label names
row_labels = df_pivot.columns.levels[1]
col_labels = df_pivot.index
# Move ticks and labels to the centre
ax.set_xticks(np.arange(df_pivot.shape[1]) + 0.5, minor = False)
ax.set_yticks(np.arange(df_pivot.shape[0]) + 0.5, minor = False)
# Insert labels
ax.set_xticklabels(row_labels, minor = False)
ax.set_yticklabels(col_labels, minor = False)
# Rotate label if too long
pyplot.xticks(rotation = 90)
fig.colorbar(im)
pyplot.savefig('/home/hayley/Documents/Python/Python Graphs/Improved heatmap.png')
pyplot.show()
