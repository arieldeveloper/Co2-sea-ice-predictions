"""
Description of module
"""
# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
from dataset_extract import *

# Importing the dataset
co2_data = extract_co2emission_top_five('datasets/co2-data.csv')

# Creating the x and y arrays as numpy arrays
X = np.array([key for key in co2_data])
y = np.array([co2_data[key] for key in co2_data])

# Reshape the
X = X.reshape(len(X), 1)

# Splitting the dataset into the Training set and Test set
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, train_size=0.8, random_state=0)

# Feature Scaling
"""from sklearn.preprocessing import StandardScaler
sc_X = StandardScaler()
X_train = sc_X.fit_transform(X_train)
X_test = sc_X.transform(X_test)
sc_y = StandardScaler()
y_train = sc_y.fit_transform(y_train)"""

# Linear regression model being applied to the sets of data we have
from sklearn.linear_model import LinearRegression

regressor = LinearRegression()

regressor.fit(X_train, y_train)

# Predicting the test set results
y_pred = regressor.predict(X_test)

# Visualizing the training set results
plt.scatter(X_train, y_train, color='red')
plt.plot(X_train, regressor.predict(X_train), color='blue')
plt.title('C02 growth (training set)')
plt.xlabel('years')
plt.ylabel('co2 values')
plt.show()

# Visualizing the Test set results
plt.scatter(X_test, y_test, color='red')
plt.plot(X_train, regressor.predict(X_train), color='blue')
plt.title('Co2 Growth (Test set)')
plt.xlabel('years')
plt.ylabel('c02 values')
plt.show()
