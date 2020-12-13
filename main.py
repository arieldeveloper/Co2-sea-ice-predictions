"""

import plotly.graph_objects as go
from plotly.subplots import make_subplots
import plotly.express
=======
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

co2_predictions = make_predictions(co2_data, 15)
temp_predictions = ...
sea_ice_predictions = ...

graphs.three_graphs_plot(co2_data, co2_predictions, temp_data, temp_predictions, sea_ice_data, sea_ice_predictions, 'Graphs')
graphs.make_map(2018)
