from datetime import timedelta

import airflow
from airflow import DAG
from airflow.operators.bash_operator import BashOperator

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': airflow.utils.dates.days_ago(2)
	}

dag = DAG(
    'my_dag',
    default_args=default_args,
    description='trial DAG',
    schedule_interval=timedelta(days=1),
)

t1 = BashOperator(
    task_id='print_date',
    bash_command='date',
    dag=dag,
)

t2 = BashOperator(
    task_id='sleep',
    depends_on_past=False,
    bash_command='sleep 1',
    dag=dag,
)

t1 >> t2
