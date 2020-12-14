"""CSC110 Fall Final project: Predictions based on datasets

DESCRIPTION:
===============================

This module contains three main functions: The first one predicts future co2 emission values,
the second one predicts future average land surface temperature values based on predicted co2
emission values and the third one predicts future sea-ice index based on the predicted average
land surface temperature.

There are also three helper functions: The first one returns the slope and intercept of a linear
regression based on its inputted x and y values, the second one returns a value based on the
inputted x, m and b values. The third helper function returns a dictionary that combines the two
inputted dictionaries.

Copyright and Usage Information
===============================

This file is provided solely for the personal and private use of instructors and TAs
from CSC110 at the University of Toronto St. George campus. All forms of
distribution of this code, whether as given or with any changes, are
expressly prohibited.

This file is Copyright (c) Ariel Chouminov, Oliver Laranjeira, Ramya Chawla and Umayrah Chonee.
"""
# Import statements
from typing import Tuple, Dict
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import numpy as np


def make_predictions_co2(x_values: list, y_values: list, time_frame: int) -> Dict[int, float]:
    """
    Given a list of x values and y values from a dataset and a given time frame,
    return a dictionary mapping a key value-pair with the year as the key and the prediction
    as the corresponding value.

    Preconditions:
        - x_values should be the x values from the extracted co2-data.csv dataset
        - y_values should be the y values of the extracted co2-data.csv dataset
        - time_frame > 0
    """
    slope, intercept = create_linear_regression(x_values, y_values)

    # Accumulator
    predicted_values = {}

    for year in range(2016, 2015 + time_frame + 1):
        predicted_values[year] = line_output(slope, intercept, year)

    return predicted_values


def make_predictions_temp(x_values: list, y_values: list, predicted_co2_values: dict)\
        -> Dict[int, float]:
    """
    Given a list of x values and y values from a dataset and a given dictionary,
    return a dictionary mapping a key value-pair with the year as the key and the prediction
    as the corresponding value.

    Preconditions:
        - x_values should be the y-values of the extracted co2-data.csv dataset
        - y_values should be the x-values of the extracted temperature-data.csv dataset
        - predicted_co2_values should be a dictionary containing co2 predictions
    """

    slope, intercept = create_linear_regression(x_values, y_values)

    predicted_values = {}

    for year in predicted_co2_values:
        predicted_values[year] = line_output(slope, intercept, predicted_co2_values[year])

    return predicted_values


def make_predictions_sea_ice(x_values: list, y_values: list, predicted_temp_values: dict)\
        -> Dict[int, float]:
    """
    Given a list of x values and y values from a dataset and a given dictionary,
    return a dictionary mapping a key value-pair with the year as the key and the prediction
    as the corresponding value.

    Preconditions:
        - x_values should be the y-values of the extracted temperature-data.csv dataset
        - y_values should be the x-values of the extracted sea-ice-data.csv dataset
        - predicted_temp_values should be a dictionary containing temperature predictions
    """

    slope, intercept = create_linear_regression(x_values, y_values)

    predicted_values = {}

    for year in predicted_temp_values:
        predicted_values[year] = line_output(slope, intercept, predicted_temp_values[year])

    return predicted_values


def create_linear_regression(x_values: list, y_values: list) -> Tuple[int, int]:
    """
    Takes in a list of x and y values and returns a tuple containing two values:
    the slope and intercept respectively for the linear regression line.

    Preconditions:
        - len(x_values) > 5
        - len(y_values) > 5
    """

    # Creating the x and y arrays as numpy arrays
    x = np.array(x_values)
    y = np.array(y_values)

    x = x.reshape(len(x), 1)

    x_train, _, y_train, _ = train_test_split(x, y, test_size=0.20, train_size=0.8, random_state=0)

    regressor = LinearRegression()

    regressor.fit(x_train, y_train)

    # Calculate slope and intercept
    slope = regressor.coef_[0]
    intercept_value = regressor.intercept_

    # Visualizing the training set results
    # plt.scatter(x_train, y_train, color='red')
    # plt.plot(x_train, regressor.predict(x_train), color='blue')
    # plt.title('C02 growth (training set)')
    # plt.xlabel('years')
    # plt.ylabel('co2 values')
    # plt.show()

    # Visualizing the Test set results
    # plt.scatter(x_test, y_test, color='red')
    # plt.plot(x_train, regressor.predict(x_train), color='blue')
    # plt.title('Co2 Growth (Test set)')
    # plt.xlabel('years')
    # plt.ylabel('c02 values')
    # plt.show()
    return (slope, intercept_value)


def line_output(m: float, b: float, x: float) -> float:
    """
    Return value given an x and the m, which is the slope of the line and b,
    which is the intercept of the line.
    """
    y = (m * x) + b
    return y


def add_predictions_to_data(data: dict, predicted_values: dict) -> Dict[int, float]:
    """
    Return a dictionary consisting of all key value pairs inside data and predicted_values

    Preconditions:
        - data should be a dictionary with the key as an int and the corresponding value
        as a float value.
        - predicted_values should be a dictionary with the key as an int and the corresponding value
        as a float value.

    >>> final_dict = add_predictions_to_data({2000: 10.0, 2001: 10.5, 2002: 11.0}, {2003: 11.5, 2004: 12.0})
    >>> final_dict == {2000: 10.0, 2001: 10.5, 2002: 11.0, 2003: 11.5, 2004: 12.0}
    True
    """
    new_data = data.copy()
    for key in predicted_values:
        new_data[key] = predicted_values[key]

    return new_data


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)

    import python_ta

    python_ta.check_all(config={
        'extra-imports': ['typing.Tuple', 'typing.Dict', 'numpy',
                          'sklearn.linear_model', 'sklearn.model_selection'],
        'allowed-io': [],
        'max-line-length': 100,
        'disable': ['R1705', 'C0200']
    })
