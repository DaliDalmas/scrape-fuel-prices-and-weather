import pandas as pd
import psycopg2 as pg


def engine_create():
    engine = pg.connect("host=localhost dbname=scraped_data user=fastapi_user password=fastapi_user")
    return engine

def get_average_daily_price_per_litre():
    q = """
        select AVG(usd_price_per_litre) average_usd_price_per_litre,
                country,
                DATE(created_at) created_at
        from data.fuel
        group by 2, 3
        order by 3;
        """
    return pd.read_sql(q, con=engine_create())

def get_hourly_price_per_litre():
    q = """
        select usd_price_per_litre,
                country,
                created_at
        from data.fuel
        order by 3;
        """
    return pd.read_sql(q, con=engine_create())

def get_hourly_temperature():
    q = """
        select 
            temperature,
            created_at,
            country
        from data.weather;
        """
    return pd.read_sql(q, con=engine_create())