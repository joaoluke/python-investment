import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px


df = px.data.stocks()
fig = px.line(df, x='date', y="GOOG")
fig1 = px.line(df, x='date', y="GOOG")

app = dash.Dash(__name__)

app.layout = html.Div([
    dcc.Graph(figure=fig),
    dcc.Graph(figure=fig1)
])

if __name__ == '__main__':
    app.run_server(debug=True)
