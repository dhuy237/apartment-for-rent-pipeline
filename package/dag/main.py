from datetime import datetime, timedelta
import pendulum
import os
from airflow.decorators import dag
from airflow.operators.dummy_operator import DummyOperator


default_args = {
    'owner': 'dhuy',
    'start_date': pendulum.now(),
    'depends_on_past': False,
    'retries': 3,
    'retry_delay': timedelta(minutes=5),
    'catchup_by_default': False,
    'email_on_retry': False
}


@dag(
    default_args=default_args,
    description='Load data from PostgreSQL to ClickHouse with Airflow',
    schedule_interval='0 * * * *'
)
def apartments_for_rent_pipeline():
    start_operator = DummyOperator(task_id='Begin_execution')

    end_operator = DummyOperator(task_id='Stop_execution')

    start_operator >> end_operator


project_dag = apartments_for_rent_pipeline()