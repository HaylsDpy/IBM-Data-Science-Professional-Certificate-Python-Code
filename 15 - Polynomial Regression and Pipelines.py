# Refer to notebook for explanation

# Calculate polynomial of 3rd order - DEBUG
import numpy as np

f = np.polyfit(x, y, 3)

p = np.polyld(f)

# Print out the model (equation)
print(p)



# Mutlidimensional Polynomial Linear Regression:
# NumPy's polyfit() function cannot perform this type of regression.
# Use the 'preprocessing' library in scikit_learn to create a polynomial feature object
from sklearn.preprocessing import PolynomialFeatures

z = auto_df[['horsepower', 'curb-weight', 'engine-size', 'highway-mpg']]
# The constructor takes the degree of the polynomial as a parameter
# Then you transform the features into a polynomial feature with the fit_transform() method
# Create a polynomial object of degree 2
pr = PolynomialFeatures(degree = 2)

pr
# The original data is of 201 samples and 4 features
z_pr = pr.fit_transform(Z)
# After transformation, there are 201 samples and 15 features
z.shape
# Output of this is (201, 15)
z_pr.shape



# Pre-processing:
# As the dimension of the data gets larger, we may want to normalise multiple features in scikit_learn.
# Instead, we can use the preprocessing module to simplify many tasks.
# Normalise each feature simultaneously
from sklearn.preprocessing import StandardScaler

# Train the object
SCALE = StandardScaler()

# Fit the scale object
SCALE.fit(x_data[['horsepower', 'highway-mpg']])

# Transform the data into a new DataFrame on array x_scale
x_Scale = SCALE.transform(x_data[['horsepower', 'highway-mpg']])



# We observed earlier that a linear model did not provide best fit whilst using highway-mpg as the predictor variable. Let's see if a polynomial model can be fitted intead:
def PlotPolly(model, independent_variable, dependent_variable, Name):
   x_new = np.linspace(15, 55, 100)
   y_new = model(x_new)

   plt.pyplot.plot(independent_variable, dependent_variable, '.', x_new, y_new)
   plt.pyplot.title('Polynomial Fit with matplotlib for Price ~ Length')
   ax = plt.pyplot.gca()
   ax.set_facecolor((0.898, 0.898, 0.898))
   fig = plt.pyplot.gcf()
   plt.pyplot.xlabel(Name)
   plt.pyplot.ylabel('Price of Cars')
   plt.pyplot.savefig('/home/hayley/Documents/Python/Python Graphs/Polynomial Regression Model.png')

   plt.pyplot.show()
   plt.pyplot.close()

# Get the variables
x = auto_df['highway-mpg']
y = auto_df['price']

# Fit the polynomial using polyfit() function, then use poly1d() function to display the polynomial function
f = np.polyfit(x, y, 3)
p = np.poly1d(f)

print(p)

# Plot the function
PlotPolly(p, x, y, 'highway-mpg')

# You can aleady see that this polynomial model performs better than the linear model. This s because the generated polynomial function 'hits' more of the data points


# Create an 11 order (cubic) polynomial model with the variables x and y from above:
# Redefine the PlotPolly function if you want to save the graphs seperately
f1 = np.polyfit(x, y, 11)
p1 = np.poly1d(f1)

print(p)

PlotPolly(p1, x, y, 'Highway MPG')



# Pipelines:
# Simplify the above process by using pipelines
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline

# Create a list of tuples (in Python, this is a collection which is ordered and unchangeable)
# The first element in the tuple contains the name of the estimator model: 'scale', 'polynomial', 'mode'
# The second element contains the model constructor: 'StandardScaler', 'PolynomialFeatures', 'LinearRegression'
Input = [('scale', StandardScaler()), ('polynomial', PolynomialFeatures(degree = 2), 'mode', LinearRegression())]

# Next, input the list into the pipeline constructor. This creates a pipeline object
pipe = Pipeline(Input)

pipe

# Train the pipeline by applying the train method to the pipeline object
pipe.fit(auto_df[['horsepower', 'curb-weight', 'engine-size', 'highway-mpg']], y)
# Alternative code inputting a variable with the above parameters saved into it:
pipe.fit(z, y)

# We can also produce a prediction
yhat = pipe.predict(x[['horsepower', 'curb-weight', 'engine-size', 'highway-mpg']])
# Similarly as above, you can normalise the data, perform a transformation and produce a prediction simultaneously
ypipe = pipe.predict(z)
ypipe[0:4]
