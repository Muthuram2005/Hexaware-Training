from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime


def create_orders():
    orders = [
        ["Laptop", 1, 70000],
        ["Mouse", 4, 500],
        ["Monitor", 2, 12000],
        ["Keyboard", 3, 1500]
    ]

    print("Orders Created")

    for order in orders:
        print(order)


def calculate_order_value():
    orders = [
        ["Laptop", 1, 70000],
        ["Mouse", 4, 500],
        ["Monitor", 2, 12000],
        ["Keyboard", 3, 1500]
    ]

    total_revenue = 0
    highest_product = ""
    highest_revenue = 0

    for product, qty, price in orders:
        revenue = qty * price
        total_revenue += revenue

        print(product, "=", revenue)

        if revenue > highest_revenue:
            highest_revenue = revenue
            highest_product = product

    print("Total Revenue =", total_revenue)
    print("Highest Selling Product =", highest_product)


def generate_sales_report():
    print("Sales Report Generated")
    print("Total Revenue = 100500")
    print("Highest Selling Product = Laptop")


with DAG(
    dag_id="online_orders",
    start_date=datetime(2026, 1, 1),
    schedule=None,
    catchup=False
) as dag:

    create_orders = PythonOperator(
        task_id="create_orders",
        python_callable=create_orders
    )

    calculate_order_value = PythonOperator(
        task_id="calculate_order_value",
        python_callable=calculate_order_value
    )

    generate_sales_report = PythonOperator(
        task_id="generate_sales_report",
        python_callable=generate_sales_report
    )

    create_orders >> calculate_order_value >> generate_sales_report
