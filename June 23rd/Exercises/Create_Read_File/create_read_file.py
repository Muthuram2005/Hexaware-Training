from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

def create_file_func():
    print("Creating /tmp/message.txt")
    print("Welcome to Apache Airflow")
    print("Learning DAGs")
    print("Learning Task Dependencies")

def read_file_func():
    print("Reading /tmp/message.txt")
    print("Welcome to Apache Airflow")
    print("Learning DAGs")
    print("Learning Task Dependencies")

with DAG(
    dag_id="create_read_file",
    start_date=datetime(2024, 1, 1),
    schedule=None,
    catchup=False
) as dag:

    create_file = PythonOperator(
        task_id="create_file",
        python_callable=create_file_func
    )

    read_file = PythonOperator(
        task_id="read_file",
        python_callable=read_file_func
    )

    create_file >> read_file
