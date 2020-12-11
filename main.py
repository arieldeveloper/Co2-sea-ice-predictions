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

import plotly.graph_objects as go
from typing import List, Tuple
import csv

from dataset_extract import *
import graphs

# Extract the data

sea_ice_data = extract_sea_ice('datasets/sea-ice-data.csv')
co2_data = extract_co2emission_top_five('datasets/co2-data.csv')
temp_data = extract_temperatures('datasets/temperature-data.csv')

#

# Sea ice over time graph
# graphs.plot(sea_ice_data, title="Sea ice concentration over time")

graphs.multiple_graphs_plot(co2_data, sea_ice_data, temp_data, title="Sea ice concentration over time")
