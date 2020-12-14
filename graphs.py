"""CSC110 Fall Final project: Graphing datasets and predictions and a Choropleth Map.

DESCRIPTION:
===============================

This module contains 2 main functions: The first one plots 3 different graphs based on our
datasets and predictions, and the second one creates a choropleth map. There is also a helper
function for our first main function that creates dataframes. (see below)

Copyright and Usage Information
===============================

This file is provided solely for the personal and private use of instructors and TAs
from CSC110 at the University of Toronto St. George campus. All forms of
distribution of this code, whether as given or with any changes, are
expressly prohibited.

This file is Copyright (c) Ariel Chouminov, Oliver Laranjeira, Ramya Chawla and Umayrah Chonee.
"""
# import statements
from typing import Dict, List
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import pandas as pd
from dataset_extract import make_x_y_lists, extract_list_map


def three_graphs_plot(co2_data: Dict[int, float], temp_data: Dict[int, float],
                      sea_ice_data: Dict[int, float], title: str) -> None:
    """Plot three line graphs given the three extracted datasets with additional predicted data.

    Preconditions:
        - The input dictionaries should contain 36 values from the extracted dataset and
         15 predicted values.
        - data must be in dict format as outputted by make_predictions_xxx functions from
        predictions module.
        - The inputted dictionaries should be in the order: co2-data, temperature-data,
         sea-ice-data.
    """

    x1, y1 = make_x_y_lists(co2_data)

    dict_info1 = adding_type_value(x1, y1, 'year', 'co2_emission')

    df1 = pd.DataFrame(dict_info1)

    y2 = make_x_y_lists(temp_data)[1]

    dict_info2 = adding_type_value(y1, y2, 'co2_emission', 'temperature')

    df2 = pd.DataFrame(dict_info2)

    y3 = make_x_y_lists(sea_ice_data)[1]

    dict_info3 = adding_type_value(y2, y3, 'temperature', 'sea-ice index')

    df3 = pd.DataFrame(dict_info3)

    # making subplots
    fig = make_subplots(rows=3, cols=1,
                        subplot_titles=("CO2 concentration over time",
                                        "Average land-Surface Temperature over CO2 Emission",
                                        "Sea-Ice Index over average land-surface temperature"))
    # Adding graph 1
    fig.add_trace(go.Scatter(x=df1['year'],
                             y=df1['co2_emission'],
                             mode='lines+markers',
                             name='year - CO2',
                             marker=dict(size=8, color=(df1.year < 2016).astype('int'),
                                         colorscale=[[0, 'red'], [1, 'green']])),
                  row=1, col=1)

    # Adding graph 2
    fig.add_trace(go.Scatter(x=df2['co2_emission'],
                             y=df2['temperature'],
                             mode='lines+markers',
                             name='CO2 - temperature',
                             marker=dict(size=8, color=(df2.type_value == 'dataset').astype('int'),
                                         colorscale=[[0, 'red'], [1, 'green']])),
                  row=2, col=1)

    # Adding graph 3
    fig.add_trace(go.Scatter(x=df3['temperature'],
                             y=df3['sea-ice index'],
                             mode='lines+markers',
                             name='temperature - sea-ice index',
                             marker=dict(size=8, color=(df2.type_value == 'dataset').astype('int'),
                                         colorscale=[[0, 'red'], [1, 'green']])),
                  row=3, col=1)

    # Adding annotations to indicate start of predicted values
    fig.add_annotation(row=1, col=1, x=2016, y=19891.809, text='Start of predictions')
    fig.add_annotation(row=2, col=1, x=19891.809, y=9.6796, text='Start of predictions')
    fig.add_annotation(row=3, col=1, x=9.6796, y=14.6694, text='Start of predictions')

    # Update xaxis properties
    fig.update_xaxes(title_text="Year", row=1, col=1)
    fig.update_xaxes(title_text="CO2 emission (million tons per year)", row=2, col=1)
    fig.update_xaxes(title_text="Temperature (degrees celsius)", row=3, col=1)

    # Update yaxis properties
    fig.update_yaxes(title_text="CO2 emission (million tons per year)", row=1, col=1)
    fig.update_yaxes(title_text="Temperature (degrees celsius)", row=2, col=1)
    fig.update_yaxes(title_text="Sea-ice index (million square kilometers)", row=3, col=1)

    fig.update_layout(height=900, width=1500, title_text=title)
    fig.show()


def make_map(year: int) -> None:
    """
    Creates a Choropleth map based on the co2-data.csv and presents the co2 emissions
    around the world for a given year.

    Preconditions:
        - 2018 >= year >= 1979
    """
    list_map = extract_list_map('datasets/co2-data.csv', year)
    # Accumulators
    list_code = []
    list_country_name = []
    list_co2_emission = []

    for inner_list in list_map:
        list_code.append(inner_list[0])
        list_country_name.append(inner_list[1])
        list_co2_emission.append(inner_list[2])

    data = {'Code': list_code,
            'Country': list_country_name,
            'CO2 Emission': list_co2_emission}

    df = pd.DataFrame(data)

    fig = go.Figure(data=go.Choropleth(
        locations=df['Code'],
        z=df['CO2 Emission'],
        text=df['Country'],
        colorscale='Reds',
        autocolorscale=False
    ))

    fig.update_layout(
        title_text='CO2 Emission Map ' + str(year),
        geo=dict(
            showframe=False,
            showcoastlines=False,
            projection_type='equirectangular'
        ))

    fig.show()


def adding_type_value(x_values: List, y_values: List, x_column: str, y_column: str) ->\
        Dict[str, List]:
    """
    Adding 'dataset' or 'prediction' as type value for the inputted x_values and y_values.

    The return type is a dictionary which maps name of x_column to the list of inputed x_values,
    the name of y_column to the list of inputed y_values, and the type_value to either 'dataset' or
    'prediction'.

    Preconditions:
        - len(x_values) == 52
        - len(y_values) == 52
    """
    type_value = []
    for _ in range(0, 37):
        type_value.append('dataset')

    for _ in range(0, 15):
        type_value.append('prediction')

    data = {x_column: x_values,
            y_column: y_values,
            'type_value': type_value}

    return data


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)

    import python_ta

    python_ta.check_all(config={
        'extra-imports': ['typing.List', 'typing.Dict', 'pandas', 'plotly.subplots',
                          'dataset_extract', 'plotly.graph_objects'],
        'allowed-io': [],
        'max-line-length': 100,
        'disable': ['R1705', 'C0200']
    })
