"""CSC110 Fall 2020 Assignment 3, Part 4: Modeling an Epidemic

Instructions (READ THIS FIRST!)
===============================
Implement each of the functions in this file. As usual, do not change any function headers
or preconditions. You do NOT need to add doctests.

Copyright and Usage Information
===============================

This file is provided solely for the personal and private use of students
taking CSC110 at the University of Toronto St. George campus. All forms of
distribution of this code, whether as given or with any changes, are
expressly prohibited. For more information on copyright for CSC110 materials,
please consult our Course Syllabus.

This file is Copyright (c) 2020 David Liu and Mario Badr.
"""
import csv
import datetime
from typing import Dict, List

import plotly.graph_objects as go
from plotly.subplots import make_subplots
import plotly.express
import pandas

def read_csv_data(filepath: str, x_axis_index, y_axis_index):
    with open(filepath) as file:
        reader = csv.reader(file)
        x_axis = []
        y_axis = []
        for line in reader:
            x_axis.append(line[x_axis_index])
            y_axis.append(line[y_axis_index])
        return (x_axis, y_axis)


def plot(data) -> None:
    """Plot the graph
    """

    fig = plotly.express.line(data[0], x="year", y="lifeExp", color='country')
    fig.show()



if __name__ == '__main__':
    # When you are ready to check your work with python_ta, uncomment the following lines.
    #     # (Delete the "#" and space before each line.)
    #     # IMPORTANT: keep this code indented inside the "if __name__ == '__main__'" block
    #     # Leave this code uncommented when you submit your files.
    # import python_ta
    #
    # python_ta.check_all(config={
    #     'allowed-io': ['read_csv_data'],
    #     'extra-imports': ['python_ta.contracts', 'csv', 'datetime',
    #                       'plotly.graph_objects', 'plotly.subplots'],
    #     'max-line-length': 100,
    #     'max-args': 6,
    #     'max-locals': 25,
    #     'disable': ['R1705'],
    # })

    import python_ta.contracts

    python_ta.contracts.DEBUG_CONTRACTS = False
    python_ta.contracts.check_all_contracts()
