import queries as q
import plotly.express as px

def generate_avg_price_per_litre_chart():

    df = q.get_average_daily_price_per_litre()
    fig = px.bar(df, x='created_at', y="average_usd_price_per_litre", color='country', title="daily avarage fuel price per litre (usd)", barmode="group")

    return fig

def generate_hourly_price_per_litre_chart():

    df = q.get_hourly_price_per_litre()
    fig = px.line(df, x='created_at', y="usd_price_per_litre", color='country', title="hourly fuel price per litre (usd)")

    return fig

def generate_hourly_temperature_chart():

    df = q.get_hourly_temperature()
    fig = px.line(df, x='created_at', y="temperature", color='country', title="hourly temperature (deg cel)")

    return fig