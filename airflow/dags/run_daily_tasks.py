from airflow import DAG
from datetime import datetime
from airflow.operators.python import PythonOperator

from scripts import rotational_deletion

dag = DAG(
    dag_id="run_daily_tasks",
    start_date=datetime(2022, 10, 22),
    schedule_interval="@daily"
    )

run_rotational_deletion = PythonOperator(
    dag=dag,
    task_id = 'run_rotational_deletion',
    python_callable=rotational_deletion.run
)

run_rotational_deletion