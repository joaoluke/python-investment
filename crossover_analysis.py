import MetaTrader5 as mt5
import pandas as pd
import plotly.express as px
import dash
import dash_core_components as dcc
import dash_html_components as html


def generate_graphs(dataframe):
    app = dash.Dash(__name__)

    app.layout = html.Div([
        dcc.Graph(figure=fig),
        dcc.Graph(figure=fig1)
    ])

    app.run_server(debug=True)
    