"""
Description of module
"""
# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
from dataset_extract import *
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

def create_linear_regression(x_values:list, y_values:list):
    """ Takes in a list of x and y values and returns a slope and intercept
    for the linear regression line
    """
    # Creating the x and y arrays as numpy arrays

    x = np.array(x_values)
    y = np.array(y_values)

    # Reshape the
    x = x.reshape(len(x), 1)

    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.20, train_size=0.8, random_state=0)

    regressor = LinearRegression()

    regressor.fit(x_train, y_train)

    # Predicting the test set results
    y_pred = regressor.predict(x_test)

    # Calculate slope and intersept
    slope = regressor.coef_[0]
    intercept_value = regressor.intercept_

    # Visualizing the training set results
    plt.scatter(x_train, y_train, color='red')
    plt.plot(x_train, regressor.predict(x_train), color='blue')
    plt.title('C02 growth (training set)')
    plt.xlabel('years')
    plt.ylabel('co2 values')
    plt.show()

    # Visualizing the Test set results
    plt.scatter(x_test, y_test, color='red')
    plt.plot(x_train, regressor.predict(x_train), color='blue')
    plt.title('Co2 Growth (Test set)')
    plt.xlabel('years')
    plt.ylabel('c02 values')
    plt.show()
    return slope, intercept_value


def line_output(m, b, x):
    """Output a y value given an x and the m and b value of the line
    """
    y = (m * x) + b
    return y

def make_predictions(data, time_frame):
    """given the dataset and the time frame, return the predicted values
    """
    x_values = [key for key in data]
    y_values = [data[key] for key in data]

    slope, intercept = create_linear_regression(x_values, y_values)

    predicted_values = []

    for year in range(2016, 2015+time_frame+1):
        predicted_values.append(line_output(slope, intercept, year))

    return predicted_values
