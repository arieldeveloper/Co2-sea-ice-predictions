"""
Main file running all the other classes
"""

from dataset_extract import *
import graphs
from predictions import *

time_frame = 15

# Extract the data
sea_ice_data = extract_sea_ice('datasets/sea-ice-data.csv')
co2_data = extract_co2emission_top_five('datasets/co2-data.csv')
temp_data = extract_temperatures('datasets/temperature-data.csv')

# co2 prediction in dictionary format
co2_predictions = make_predictions(co2_data, time_frame)
add_predictions_to_data(co2_data, co2_predictions)

# temperature prediction

# graphs.three_graphs_plot(co2_data, temp_data, sea_ice_data, title="All graphs")
