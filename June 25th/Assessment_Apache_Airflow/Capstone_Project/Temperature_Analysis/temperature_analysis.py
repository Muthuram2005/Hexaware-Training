from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime


def create_temperature_file():
    data = [
        "Monday,34",
        "Tuesday,36",
        "Wednesday,31",
        "Thursday,38",
        "Friday,35",
        "Saturday,33",
        "Sunday,32"
    ]

    print("Temperature Data")

    for row in data:
        print(row)


def find_highest_temperature():
    data = [
        "Monday,34",
        "Tuesday,36",
        "Wednesday,31",
        "Thursday,38",
        "Friday,35",
        "Saturday,33",
        "Sunday,32"
    ]

    total = 0
    highest = 0

    for row in data:
        day, temp = row.split(",")
        temp = int(temp)

        total += temp

        if temp > highest:
            highest = temp

    print("Highest Temperature =", highest)
    print("Average Temperature =", total / len(data))


def generate_weather_report():
    print("Weather Report Generated")
    print("Highest Temperature = 38")
    print("Average Temperature = 34.14")


with DAG(
    dag_id="temperature_analysis",
    start_date=datetime(2026, 1, 1),
    schedule=None,
    catchup=False
) as dag:

    create_temperature_file = PythonOperator(
        task_id="create_temperature_file",
        python_callable=create_temperature_file
    )

    find_highest_temperature = PythonOperator(
        task_id="find_highest_temperature",
        python_callable=find_highest_temperature
    )

    generate_weather_report = PythonOperator(
        task_id="generate_weather_report",
        python_callable=generate_weather_report
    )

    create_temperature_file >> find_highest_temperature >> generate_weather_report
