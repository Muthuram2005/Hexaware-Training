from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime


def create_department_file():
    departments = [
        "IT,45000",
        "HR,35000",
        "Finance,50000",
        "IT,55000",
        "Finance,40000",
        "HR,30000"
    ]

    print("Department Data")

    for row in departments:
        print(row)


def calculate_department_salary():
    departments = [
        "IT,45000",
        "HR,35000",
        "Finance,50000",
        "IT,55000",
        "Finance,40000",
        "HR,30000"
    ]

    salary = {}

    for row in departments:
        dept, amount = row.split(",")

        if dept not in salary:
            salary[dept] = 0

        salary[dept] += int(amount)

    print("Department Salary")

    for dept, total in salary.items():
        print(dept, "=", total)


def generate_department_report():
    print("Department Report Generated")
    print("IT = 100000")
    print("HR = 65000")
    print("Finance = 90000")


with DAG(
    dag_id="department_salary_report",
    start_date=datetime(2026, 1, 1),
    schedule=None,
    catchup=False
) as dag:

    create_department_file = PythonOperator(
        task_id="create_department_file",
        python_callable=create_department_file
    )

    calculate_department_salary = PythonOperator(
        task_id="calculate_department_salary",
        python_callable=calculate_department_salary
    )

    generate_department_report = PythonOperator(
        task_id="generate_department_report",
        python_callable=generate_department_report
    )

    create_department_file >> calculate_department_salary >> generate_department_report
