from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime


def create_employee_file():
    data = [
        "Rahul,28",
        "Priya,31",
        "Amit,42",
        "Sneha,26",
        "Kiran,38"
    ]

    print("Employee Data")

    for row in data:
        print(row)


def calculate_average_age():
    data = [
        "Rahul,28",
        "Priya,31",
        "Amit,42",
        "Sneha,26",
        "Kiran,38"
    ]

    ages = []

    for row in data:
        name, age = row.split(",")
        ages.append(int(age))

    print("Youngest Employee =", min(ages))
    print("Oldest Employee =", max(ages))
    print("Average Age =", sum(ages) / len(ages))


def generate_age_report():
    print("Age Report Generated")
    print("Youngest Employee = 26")
    print("Oldest Employee = 42")
    print("Average Age = 33")


with DAG(
    dag_id="employee_age_report",
    start_date=datetime(2026, 1, 1),
    schedule=None,
    catchup=False
) as dag:

    create_employee_file = PythonOperator(
        task_id="create_employee_file",
        python_callable=create_employee_file
    )

    calculate_average_age = PythonOperator(
        task_id="calculate_average_age",
        python_callable=calculate_average_age
    )

    generate_age_report = PythonOperator(
        task_id="generate_age_report",
        python_callable=generate_age_report
    )

    create_employee_file >> calculate_average_age >> generate_age_report
