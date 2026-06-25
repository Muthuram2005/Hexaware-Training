from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime


def create_transactions():
    data = [
        "Deposit,10000",
        "Withdraw,2500",
        "Deposit,4000",
        "Withdraw,1500",
        "Deposit,2000"
    ]

    print("Transactions Created")

    for row in data:
        print(row)


def calculate_balance():
    data = [
        "Deposit,10000",
        "Withdraw,2500",
        "Deposit,4000",
        "Withdraw,1500",
        "Deposit,2000"
    ]

    deposit = 0
    withdrawal = 0

    for row in data:
        transaction, amount = row.split(",")
        amount = int(amount)

        if transaction == "Deposit":
            deposit += amount
        else:
            withdrawal += amount

    print("Total Deposit =", deposit)
    print("Total Withdrawal =", withdrawal)
    print("Final Balance =", deposit - withdrawal)


def generate_account_report():
    print("Account Report Generated")
    print("Total Deposit = 16000")
    print("Total Withdrawal = 4000")
    print("Final Balance = 12000")


with DAG(
    dag_id="bank_transaction_summary",
    start_date=datetime(2026, 1, 1),
    schedule=None,
    catchup=False
) as dag:

    create_transactions = PythonOperator(
        task_id="create_transactions",
        python_callable=create_transactions
    )

    calculate_balance = PythonOperator(
        task_id="calculate_balance",
        python_callable=calculate_balance
    )

    generate_account_report = PythonOperator(
        task_id="generate_account_report",
        python_callable=generate_account_report
    )

    create_transactions >> calculate_balance >> generate_account_report
