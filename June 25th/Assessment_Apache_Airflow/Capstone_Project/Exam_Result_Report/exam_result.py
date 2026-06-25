from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime


def create_result_file():
    results = [
        "Rahul,Pass",
        "Priya,Fail",
        "Amit,Pass",
        "Sneha,Pass",
        "Kiran,Fail",
        "Megha,Pass"
    ]

    print("Result Data")

    for row in results:
        print(row)


def count_pass_fail():
    results = [
        "Rahul,Pass",
        "Priya,Fail",
        "Amit,Pass",
        "Sneha,Pass",
        "Kiran,Fail",
        "Megha,Pass"
    ]

    total_pass = 0
    total_fail = 0

    for row in results:
        name, result = row.split(",")

        if result == "Pass":
            total_pass += 1
        else:
            total_fail += 1

    print("Total Pass =", total_pass)
    print("Total Fail =", total_fail)


def generate_result_summary():
    print("Result Summary Generated")
    print("Total Pass = 4")
    print("Total Fail = 2")


with DAG(
    dag_id="exam_result_report",
    start_date=datetime(2026, 1, 1),
    schedule=None,
    catchup=False
) as dag:

    create_result_file = PythonOperator(
        task_id="create_result_file",
        python_callable=create_result_file
    )

    count_pass_fail = PythonOperator(
        task_id="count_pass_fail",
        python_callable=count_pass_fail
    )

    generate_result_summary = PythonOperator(
        task_id="generate_result_summary",
        python_callable=generate_result_summary
    )

    create_result_file >> count_pass_fail >> generate_result_summary
