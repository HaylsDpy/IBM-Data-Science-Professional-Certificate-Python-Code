# Generate a histogram of some data using the artist layer
from matplotlib.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import figure
fig = figure()
canvas = FigureCanvas(fig)

# Create 10000 random numbers using NumPy
import numpy as np
x = np.random.randn(10000)
# Create axes artist
ax = fig.add_subplot(111)
# Generate a histogram of the 10000 numbers
ax.hist(x, 100)

# Add a title to the figure and save it
ax.set_title('Normal distribution with $\mu = o, \sigma = 1$')
fig.savefig('Matplotlib_histogram.png')


# Generate the same histogram of 10000 random values using pyplot interface
import matplotlib.pyplot as plt
import numpy as np

x = np.random.randn(10000)
plt.hist(x, 100)
plt.title(r 'Normal distribution with $\mu = o, sigma = 1$')
plt.savefig('Matplotlib_histogram.png')
plt.show()

# Plot function with matplotlib
import matplotlib.pyplot as plt

plt.plot(5, 5, 'o')
plt.show()

# Matplotlib - Pandas
india_china_df.plot(kind = 'line')

india_china_df['India'].plot(kind = 'hist')


# Read data into pandas dataframe
import numpy as np
import pandas as pd
from __future__ import print_function
# Install xlrd
!pip install xlrd
print('xlrd installed!')

df_can = pd.read_excel(
   'https://ibm.box.com/shared/static/1w190pt9zpy5bd1ptyg2aw15awamz9pu.xlsx',
   sheetname = 'Canada by Citizenship'
   skiprows = range(20)
   skip_footer = 2)
