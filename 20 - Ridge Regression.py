# In order to select alpha, we use cross validation
# To make a prediction using ridge regression, import ride from sklearn.linear_models
from sklearn.linear_model import Ridge

# Creat a ridge object using the constructor
Ridge_Model = Ridge(alpha = 0.1)

# Train the model
Ridge_Model.fit(x, y)

# Use predict() to make a prediction
Yhat = Ridge_Model.predict(x)
