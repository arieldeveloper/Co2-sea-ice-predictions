"""CSC110 Fall Final project: Main Module

DESCRIPTION:
===============================

This module contains all the top_level statements and function calls from the other
modules that are needed to run our project.
You should be able to run this file and access our finished project.

Copyright and Usage Information
===============================

This file is provided solely for the personal and private use of instructors and TAs
from CSC110 at the University of Toronto St. George campus. All forms of
distribution of this code, whether as given or with any changes, are
expressly prohibited.

This file is Copyright (c) Ariel Chouminov, Oliver Laranjeira, Ramya Chawla and Umayrah Chonee.
"""
# import statements
import dataset_extract
import graphs
import predictions

TIME_FRAME = 15

# Extract the data
sea_ice_data = dataset_extract.extract_sea_ice('sea-ice-data.csv')
co2_data = dataset_extract.extract_co2emission_top_five('co2-data.csv')
temp_data = dataset_extract.extract_temperatures('temperature-data.csv')

# co2 prediction in dictionary format
x_values_co2 = [key for key in co2_data]
y_values_co2 = [co2_data[key] for key in co2_data]

co2_predictions = predictions.make_predictions_co2(x_values_co2, y_values_co2, TIME_FRAME)
updated_co2_data = predictions.add_predictions_to_data(co2_data, co2_predictions)

# temperature prediction
x_values_temp = [co2_data[key] for key in co2_data]
y_values_temp = [temp_data[key] for key in temp_data]

temp_predictions = predictions.make_predictions_temp(x_values_temp, y_values_temp, co2_predictions)
updated_temp_data = predictions.add_predictions_to_data(temp_data, temp_predictions)

# Sea ice prediction
x_values_sea_ice = [temp_data[key] for key in temp_data]
y_values_sea_ice = [sea_ice_data[key] for key in sea_ice_data]

sea_ice_predictions = predictions.make_predictions_sea_ice(x_values_sea_ice,
                                                           y_values_sea_ice, temp_predictions)
updated_sea_ice = predictions.add_predictions_to_data(sea_ice_data, sea_ice_predictions)

graphs.three_graphs_plot(updated_co2_data, updated_temp_data, updated_sea_ice, 'Graphs')
graphs.make_map(2018)

