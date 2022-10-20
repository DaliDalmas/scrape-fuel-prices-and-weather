from airflow import DAG
from datetime import datetime
from airflow.operators.python import PythonOperator

from fetch.fuel import Fuel
from fetch.weather import Weather
from scrape.scrape_fuel import ScrapeFuel
from scrape.scrape_weather import ScrapeWeather


dag = DAG(
    dag_id="run_hourly_tasks",
    start_date=datetime(2022, 10, 20),
    schedule_interval="@hourly"
    )

run_fetch_kenyan_fuel = PythonOperator(
    dag=dag,
    task_id = 'run_fetch_kenyan_fuel',
    python_callable=Fuel('Kenya').fetch_fuel
)

run_fetch_ugandan_fuel = PythonOperator(
    dag=dag,
    task_id = 'run_fetch_ugandan_fuel',
    python_callable=Fuel('Uganda').fetch_fuel
)

run_fetch_kenyan_weather = PythonOperator(
    dag=dag,
    task_id = 'run_fetch_kenyan_weather',
    python_callable=Weather(251, 'nairobi').fetch_weather
)

run_fetch_ugandan_weather = PythonOperator(
    dag=dag,
    task_id = 'run_fetch_ugandan_weather',
    python_callable=Weather(1328, 'kampala').fetch_weather
)

run_scrape_kenyan_fuel = PythonOperator(
    dag=dag,
    task_id = 'run_scrape_kenyan_fuel',
    python_callable=ScrapeFuel('tmp/kenya_fuel_price.html').scrape,
    op_kwargs={'country': 'KE'},
)

run_scrape_ugandan_fuel = PythonOperator(
    dag=dag,
    task_id = 'run_scrape_ugandan_fuel',
    python_callable=ScrapeFuel('tmp/uganda_fuel_price.html').scrape,
    op_kwargs={'country': 'UG'},
)

run_scrape_kenyan_weather = PythonOperator(
    dag=dag,
    task_id = 'run_scrape_kenyan_weather',
    python_callable=ScrapeWeather('tmp/kampala_weather.html').scrape,
    op_kwargs={'country': 'UG'},
)

run_scrape_ugandan_weather = PythonOperator(
    dag=dag,
    task_id = 'run_scrape_ugandan_weather',
    python_callable=ScrapeWeather('tmp/nairobi_weather.html').scrape,
    op_kwargs={'country': 'KE'},
)

def clean_up_files():
    pass

run_clean_up = PythonOperator(
    dag=dag,
    task_id = 'run_clean_up',
    python_callable=clean_up_files
)

run_fetch_kenyan_fuel >> run_scrape_kenyan_fuel >> run_clean_up
run_fetch_ugandan_fuel >> run_scrape_ugandan_fuel >> run_clean_up
run_fetch_kenyan_weather >> run_scrape_kenyan_weather >> run_clean_up
run_fetch_ugandan_weather >> run_scrape_ugandan_weather >> run_clean_up
