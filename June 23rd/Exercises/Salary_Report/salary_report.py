from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

def create_salary_file():
    print("Creating employees.txt")
    print("Rahul,45000")
    print("Priya,52000")
    print("Amit,61000")
    print("Sneha,48000")

def calculate_total_salary():
    print("Calculating Total Salary")
    print("Total Salary = 206000")

def generate_report():
    print("Salary Report")
    print("Employees = 4")
    print("Total Salary = 206000")

with DAG(
    dag_id="salary_report",
    start_date=datetime(2024, 1, 1),
    schedule=None,
    catchup=False
) as dag:

    create_salary_file_task = PythonOperator(
        task_id="create_salary_file",
        python_callable=create_salary_file
    )

    calculate_total_salary_task = PythonOperator(
        task_id="calculate_total_salary",
        python_callable=calculate_total_salary
    )

    generate_report_task = PythonOperator(
        task_id="generate_report",
        python_callable=generate_report
    )

    create_salary_file_task >> calculate_total_salary_task >> generate_report_task
