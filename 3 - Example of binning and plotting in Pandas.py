# Example of binning and plotting data in Pandas:
auto_df['horsepower'] = auto_df['horsepower'].astype(int, copy = True)

%matplotlib inline
import matplotlib as plt
from matplotlib import pyplot
plt.pyplot.hist(auto_df['horsepower'])
# Set x/y labels and plot title
plt.pyplot.xlabel('Horsepower')
plt.pyplot.ylabel('Count')
plt.pyplot.title('Horsepower bins')
pyplot.savefig('/home/hayley/Documents/Python/Python Graphs/Sample Histogram.png')

# Create 3 bins of equal size
bins = np.linspace(min(auto_df['horsepower']), max(auto_df['horsepower']), 4)
# Set group names
group_names = ['Low', 'Medium', 'High']
# Apply the cut() function to determine what each value of 'auto_df['horsepower']' belongs to
auto_df['horsepower-binned'] = pd.cut(auto_df['horsepower'], bins, labels = group_names, include_lowest = True)
auto_df[['horsepower', 'horsepower-binned']].head(20)
# Look at the number of vehicles in each bin
auto_df['horsepower-binned'].value_counts()


# Plot the distribution of each bin
%matplotlib inline
import matplotlib as plt
from matplotlib import pyplot
pyplot.bar(group_names, auto_df['horsepower-binned'].value_counts())
# Set x/y axis names and plot title
plt.pyplot.xlabel('Horsepower')
plt.pyplot.ylabel('Count')
plt.pyplot.title('Horsepower Bins')
pyplot.savefig('/home/hayley/Documents/Python/Python Graphs/Sample Bar Chart.png')


# Bins visualisation:
# Normally, a histogram is used to visualise the distribution of the bins created above
%matplotlib inline
import matplotlib as plt
from matplotlib import pyplot

a = (0, 1, 2)

# Draw histogram of attribute 'horsepower' with bins = 3
plt.pyplot.hist(auto_df['horsepower'], bins = 3)
# Set x/y labels and plot title
plt.pyplot.xlabel('Horsepower')
plt.pyplot.ylabel('Count')
plt.pyplot.title('Horsepower Bins')
pyplot.savefig('/home/hayley/Documents/Python/Python Graphs/Sample Histogram with Bins.png')
