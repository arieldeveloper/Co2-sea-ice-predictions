from typing import Dict, List
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from dataset_extract import make_x_y_lists, extract_list_map
import pandas as pd


def three_graphs_plot(co2_data: Dict[int, float], co2_data_predict: Dict[int, float],
                      temp_data: Dict[int, float], temp_data_predict: Dict[int, float],
                      sea_ice_data: Dict[int, float], sea_ice_predict: Dict[int, float], title: str) -> None:

    """Plot three line graphs given the three datasets.

    Preconditions:
        - data must be in dict format as outputted by extract_xxx functions
        - The datasets should be in the order: co2-data, temperature-data, sea-ice-data
    """

    x1, y1 = make_x_y_lists(co2_data)
    x1_predict, y1_predict = make_x_y_lists(co2_data_predict)

    for prediction in x1_predict:
        x1.append(prediction)
    for prediction in y1_predict:
        y1.append(prediction)

    dict_info1 = dataframe_creation(x1, y1)

    df1 = pd.DataFrame(dict_info1)

    # x2, y2 = make_x_y_lists(temp_data)

    # x2_predict, y2_predict = make_x_y_lists(temp_data_predict)

    # for prediction in x2_predict:
    #    x2.append(prediction)
    # for prediction in y2_predict:
    #    y2.append(prediction)

    # dict_info2 = dataframe_creation(x2, y2)

    # df2 = pd.DataFrame(dict_info2)

    # x3, y3 = make_x_y_lists(sea_ice_data)

    #x3_predict, y3_predict = make_x_y_lists(sea_ice_predict)

    #for prediction in x3_predict:
    #    x3.append(prediction)
    #for prediction in y3_predict:
    #    y3.append(prediction)

    # dict_info3 = dataframe_creation(x3, y3)

    # df3 = pd.DataFrame(dict_info3)

    fig = make_subplots(rows=3, cols=1, subplot_titles=("CO2 concentration over time",
                                                        "Land-Surface Temperature over CO2",
                                                        "Sea-Ice Index over average land-surface temperature"))

    fig.add_trace(go.Scatter(x=df1['year'], y=df1['co2_emission'],
                             mode='lines+markers', name='year - CO2',
                             marker=dict(size=8, color=(df1.year < 2016).astype('int'),
                             colorscale=[[0, 'red'], [1, 'green']])), row=1, col=1)

    fig.add_trace(go.Scatter(x=df1['year'], y=df1['co2_emission'],
                             mode='lines+markers', name='year - CO2',
                             marker=dict(size=8, color=(df1.year < 2016).astype('int'),
                             colorscale=[[0, 'red'], [1, 'green']])), row=2, col=1)

    fig.add_trace(go.Scatter(x=df1['year'], y=df1['co2_emission'],
                             mode='lines+markers', name='year - CO2',
                             marker=dict(size=8, color=(df1.year < 2016).astype('int'),
                                         colorscale=[[0, 'red'], [1, 'green']])), row=3, col=1)

    # Update xaxis properties
    fig.update_xaxes(title_text="Year", row=1, col=1)
    fig.update_xaxes(title_text="CO2 emission", row=2, col=1)
    fig.update_xaxes(title_text="Temperature", row=3, col=1)

    # Update yaxis properties
    fig.update_yaxes(title_text="CO2 emission", row=1, col=1)
    fig.update_yaxes(title_text="Temperature", row=2, col=1)
    fig.update_yaxes(title_text="Sea-ice index", row=3, col=1)

    fig.update_layout(height=900, width=1500, title_text=title)
    fig.show()


def dataframe_creation(x_values: List, y_values: List) -> Dict[str, List]:
    """
    Adding 'dataset' or 'prediction' as type value.
    """
    type_value = []
    for _ in range(0, 37):
        type_value.append('dataset')

    for _ in range(0, 15):
        type_value.append('prediction')

    data = {'year': x_values,
            'co2_emission': y_values,
            'type_value': type_value}

    return data


def make_map(year: int) -> None:

    list_map = extract_list_map('datasets/co2-data.csv', year)
    list_code = []
    list_country_name = []
    list_co2_emission = []

    for list in list_map:
        list_code.append(list[0])
        list_country_name.append(list[1])
        list_co2_emission.append(list[2])

    data = {'Code': list_code,
            'Country': list_country_name,
            'CO2 Emission': list_co2_emission}

    df = pd.DataFrame(data)

    fig = go.Figure(data=go.Choropleth(
        locations=df['Code'],
        z=df['CO2 Emission'],
        text=df['Country'],
        colorscale='Blues',
        autocolorscale=False
    ))

    fig.update_layout(
        title_text='CO2 Emission Map 2018',
        geo=dict(
            showframe=False,
            showcoastlines=False,
            projection_type='equirectangular'
        ),
        annotations=[dict(
            x=0.55,
            y=0.1,
            xref='paper',
            yref='paper',
            text='Source: <a href="https://www.cia.gov/library/publications/the-world-factbook/fields/2195.html">\
                CIA World Factbook</a>',
            showarrow=False
        )]
    )

    fig.show()
