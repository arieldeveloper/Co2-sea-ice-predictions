import csv
import datetime
from typing import Dict, List

import plotly.graph_objects as go
from plotly.subplots import make_subplots
import plotly.express
import pandas
from plotly.subplots import make_subplots

import plotly.graph_objects as go
from typing import List, Tuple
import csv
from dataset_extract import make_x_y_lists

class Linegraph:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def plot(data, title) -> None:
    """Plot a line graph given the data
    """
    x, y = make_x_y_lists(data)
    fig = go.Figure()

    fig.add_trace(go.Scatter(x=x, y=y,
                             mode='lines',
                             name='lines'))

    fig.show()


def multiple_graphs_plot(data1, data2, data3, title) -> None:
    """Plot a line graph given the data
    """
    x1, y1 = make_x_y_lists(data1)
    x2, y2 = make_x_y_lists(data2)
    x3, y3 = make_x_y_lists(data3)

    fig = make_subplots(rows=3, cols=1)

    fig.add_trace(go.Scatter(x=x1, y=y1,
                             mode='lines',
                             name='lines'), row = 1, col=1)

    fig.add_trace(go.Scatter(x=x2, y=y2,
                             mode='lines',
                             name='lines'), row=2, col=1)

    fig.add_trace(go.Scatter(x=x3, y=y3,
                             mode='lines',
                             name='lines'), row=3, col=1)

    fig.update_layout(height=900, width=1000, title_text=title)
    fig.show()
