from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

def create_bill_file():
    records = [
        "Rahul,210",
        "Priya,180",
        "Amit,300",
        "Sneha,150",
        "Kiran,260"
    ]

    print("Electricity Bill Data")

    for row in records:
        print(row)

def calculate_total_units():
    records = [
        "Rahul,210",
        "Priya,180",
        "Amit,300",
        "Sneha,150",
        "Kiran,260"
    ]

    total_units = 0

    for row in records:
        name, units = row.split(",")
        total_units += int(units)

    average_units = total_units / len(records)

    print("Customers =", len(records))
    print("Total Units =", total_units)
    print("Average Units =", average_units)

def generate_bill_summary():
    print("Bill Summary Generated")
    print("Customers = 5")
    print("Total Units = 1100")
    print("Average Units = 220")


with DAG(
    dag_id="electricity_bill_summary",
    start_date=datetime(2026, 1, 1),
    schedule=None,
    catchup=False
) as dag:

    create_bill_file = PythonOperator(
        task_id="create_bill_file",
        python_callable=create_bill_file
    )

    calculate_total_units = PythonOperator(
        task_id="calculate_total_units",
        python_callable=calculate_total_units
    )

    generate_bill_summary = PythonOperator(
        task_id="generate_bill_summary",
        python_callable=generate_bill_summary
    )

    create_bill_file >> calculate_total_units >> generate_bill_summary
