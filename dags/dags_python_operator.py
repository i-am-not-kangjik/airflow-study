from airflow import DAG
import pendulum
import datetime
from airflow.operators.python import PythonOperator
import random

with DAG(
    dag_id="dags_python_operator",
    schedule="0 0 * * *", 
    start_date=pendulum.datetime(2023, 3, 1, tz="Asia/Seoul"),
    catchup=False
) as dag:
    
    def select_fruit():
        fruits = ["apple", "banana", "cherry"]
        print(random.choice(fruits))
        return random.choice(fruits)
        
    py_t1 = PythonOperator(
        task_id="py_t1",
        python_callable=select_fruit
    )
        
    py_t1
        