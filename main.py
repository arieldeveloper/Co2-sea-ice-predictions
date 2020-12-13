"""
Main file running all the other classes
"""

from dataset_extract import *
import graphs
from predictions import *

timeframe = 15

# Extract the data
sea_ice_data = extract_sea_ice('datasets/sea-ice-data.csv')
co2_data = extract_co2emission_top_five('datasets/co2-data.csv')
temp_data = extract_temperatures('datasets/temperature-data.csv')

# graphs.multiple_graphs_plot(co2_data, sea_ice_data, temp_data, title="Sea ice concentration over time")
x_values = [key for key in co2_data]
y_values = [co2_data[key] for key in co2_data]

slope, intercept = create_linear_regression(x_values, y_values)
prediction2025 = line_output(slope, intercept, 2025)

