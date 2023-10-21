import plotly.express as px
import dash
import dash_core_components as dcc
import dash_html_components as html


def generate_graphs(df):
    app = dash.Dash(__name__)

    fig = px.line(df, x='time', y=['close', 'fast_sma', 'slow_sma'])

    for i, row in df.iterrows():
        fig.add_vline(x=row.time)

    app.layout = html.Div([
        dcc.Graph(figure=fig),
    ])

    app.run_server(debug=True)
    