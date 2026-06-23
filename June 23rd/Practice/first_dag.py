from airflow.sdk import DAG
from airflow.providers.standard.operators.python import PythonOperator
from datetime import datetime

def task1_function():
    print("Task 1 Started")

def task2_function():
    print("Task 2 Running")

def task3_function():
    print("Task 3 Completed")

with DAG(
    dag_id="first_training_dag",
    start_date=datetime(2025, 1, 1),
    schedule="@daily",
    catchup=False,
    tags=["training"]
) as dag:

    task1 = PythonOperator(
        task_id="task1",
        python_callable=task1_function
    )

    task2 = PythonOperator(
        task_id="task2",
        python_callable=task2_function
    )

    task3 = PythonOperator(
        task_id="task3",
        python_callable=task3_function
    )

    task1 >> task2 >> task3
