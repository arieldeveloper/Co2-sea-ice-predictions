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
x_values_co2 = [key for key in co2_data]
y_values_co2 = [co2_data[key] for key in co2_data]

co2_predictions = make_predictions_co2(x_values_co2, y_values_co2, time_frame)

updated_co2_data = add_predictions_to_data(co2_data, co2_predictions)

# temperature prediction
x_values_temp = [co2_data[key] for key in co2_data]
y_values_temp = [temp_data[key] for key in temp_data]

temp_predictions = make_predictions_temp(x_values_temp, y_values_temp, co2_predictions)
updated_temp_data = add_predictions_to_data(temp_data, temp_predictions)

# Sea ice prediction
x_values_sea_ice = [temp_data[key] for key in temp_data]
y_values_sea_ice = [sea_ice_data[key] for key in sea_ice_data]

sea_ice_predictions = make_predictions_temp(x_values_sea_ice, y_values_sea_ice, temp_predictions)
updated_sea_ice = add_predictions_to_data(sea_ice_data, sea_ice_predictions)

# graphs.three_graphs_plot(co2_data, temp_data, sea_ice_data, title="All graphs")
