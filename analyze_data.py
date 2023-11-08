import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px




def visualize_dashboard(df):
    signal = df[df['crossover'] == 'bull'].copy()
    fig = px.line(df, x='time', y=['close', 'fast_sma', 'slow_sma'])

    for i, row in signal.iterrows():
        fig.add_vline(x=row.time)

    app = dash.Dash(__name__)

    app.layout = html.Div([
        dcc.Graph(figure=fig)
    ])

    app.run_server(debug=True)
