import csv
import datetime
from typing import Dict, List

import plotly.graph_objects as go
from plotly.subplots import make_subplots
import plotly.express
import pandas
from plotly.subplots import make_subplots

from typing import List, Tuple
import csv
from dataset_extract import make_x_y_lists

def three_graphs_plot(data1: Dict[int, float], data2: Dict[int, float], data3: Dict[int, float], title: str) -> None:
    """Plot three line graphs given the three datasets.

    Preconditions:
        - data must be in dict format as outputted by extract_xxx functions
        - The datasets should be in the order: co2-data, temperature-data, sea-ice-data
    """
    x1, y1 = make_x_y_lists(data1)
    x2, y2 = make_x_y_lists(data2)
    x3, y3 = make_x_y_lists(data3)

    fig = make_subplots(rows=3, cols=1, subplot_titles=("CO2 concentration over time", "Global Temperature over time",
                                                        "Sea-Ice Index over time"))

    fig.add_trace(go.Scatter(x=x1, y=y1,
                             mode='lines',
                             name='CO2 - Year'), row=1, col=1)

    fig.add_trace(go.Scatter(x=x2, y=y2,
                             mode='lines',
                             name='CO2 - Temperature'), row=2, col=1)

    fig.add_trace(go.Scatter(x=x3, y=y3,
                             mode='lines',
                             name='Temperature - Sea ice'), row=3, col=1)

    # Update xaxis properties
    fig.update_xaxes(title_text="Year", row=1, col=1)
    fig.update_xaxes(title_text="CO2 emission", row=2, col=1)
    fig.update_xaxes(title_text="Temperature", type="log", row=3, col=1)

    # Update yaxis properties
    fig.update_yaxes(title_text="CO2 emission", row=1, col=1)
    fig.update_yaxes(title_text="Temperature", row=2, col=1)
    fig.update_yaxes(title_text="Sea-ice index", row=3, col=1)

    fig.update_layout(height=900, width=1000, title_text=title)
    fig.show()
