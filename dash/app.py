from dash import Dash, html, dcc
import charts
import pandas as pd


app = Dash(__name__)


app.layout = html.Div(children=[
    html.H1(children='Kenya and Uganda: Fuel and Weather comparison Data Dashboard.'),

    html.Div(children='''
        Developed by DaliCodes
    '''),
        dcc.Graph(
        id='hourly-temp-litre',
        figure=charts.generate_hourly_temperature_chart()
    ),

    dcc.Graph(
        id='daily-price-per-litre',
        figure=charts.generate_avg_price_per_litre_chart()
    ),

    dcc.Graph(
        id='hourly_price-pre-litre',
        figure=charts.generate_hourly_price_per_litre_chart()
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)