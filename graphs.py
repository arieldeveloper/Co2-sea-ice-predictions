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
from dataset_extract import make_x_y_lists

class Linegraph:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def plot(data) -> None:
    """Plot a line graph given the data
    """
    x, y = make_x_y_lists(data)
    fig = go.Figure()

    fig.add_trace(go.Scatter(x=x, y=y,
                             mode='lines',
                             name='lines'))

    fig.show()

