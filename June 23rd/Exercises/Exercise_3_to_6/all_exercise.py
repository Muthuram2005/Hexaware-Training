from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

default_args = {
    "owner": "airflow"
}

dag = DAG(
    dag_id="all_airflow_exercises",
    default_args=default_args,
    start_date=datetime(2024, 1, 1),
    schedule=None,
    catchup=False
)

def create_marks_file():
    print("Creating marks.txt")
    print("Math,80")
    print("Science,75")
    print("English,90")
    print("Python,95")

def calculate_average():
    print("Average Marks = 85")

def generate_result():
    print("Generating result.txt")
    print("Average Marks = 85")
    print("Result = PASS")

exercise_3_create_marks_file = PythonOperator(
    task_id="exercise_3_create_marks_file",
    python_callable=create_marks_file,
    dag=dag
)

exercise_3_calculate_average = PythonOperator(
    task_id="exercise_3_calculate_average",
    python_callable=calculate_average,
    dag=dag
)

exercise_3_generate_result = PythonOperator(
    task_id="exercise_3_generate_result",
    python_callable=generate_result,
    dag=dag
)

exercise_3_create_marks_file >> exercise_3_calculate_average >> exercise_3_generate_result


def create_inventory():
    print("Creating inventory")
    print("Rice,50")
    print("Oil,7")
    print("Soap,35")
    print("Sugar,10")
    print("Tea,5")

def find_low_stock():
    print("Finding low stock items")
    print("Oil")
    print("Sugar")
    print("Tea")

def generate_alert():
    print("Generating alerts.txt")
    print("Oil")
    print("Sugar")
    print("Tea")

exercise_4_create_inventory = PythonOperator(
    task_id="exercise_4_create_inventory",
    python_callable=create_inventory,
    dag=dag
)

exercise_4_find_low_stock = PythonOperator(
    task_id="exercise_4_find_low_stock",
    python_callable=find_low_stock,
    dag=dag
)

exercise_4_generate_alert = PythonOperator(
    task_id="exercise_4_generate_alert",
    python_callable=generate_alert,
    dag=dag
)

exercise_4_create_inventory >> exercise_4_find_low_stock >> exercise_4_generate_alert


def create_attendance():
    print("Creating attendance file")
    print("Rahul,Present")
    print("Priya,Present")
    print("Amit,Absent")
    print("Sneha,Present")
    print("Kiran,Absent")

def count_present():
    print("Present = 3")

def count_absent():
    print("Absent = 2")

def generate_summary():
    print("Attendance Report")
    print("Total Students = 5")
    print("Present = 3")
    print("Absent = 2")

exercise_5_create_attendance = PythonOperator(
    task_id="exercise_5_create_attendance",
    python_callable=create_attendance,
    dag=dag
)

exercise_5_count_present = PythonOperator(
    task_id="exercise_5_count_present",
    python_callable=count_present,
    dag=dag
)

exercise_5_count_absent = PythonOperator(
    task_id="exercise_5_count_absent",
    python_callable=count_absent,
    dag=dag
)

exercise_5_generate_summary = PythonOperator(
    task_id="exercise_5_generate_summary",
    python_callable=generate_summary,
    dag=dag
)

exercise_5_create_attendance >> exercise_5_count_present >> exercise_5_count_absent >> exercise_5_generate_summary


def create_csv():
    print("Creating sales.csv")
    print("product,quantity,price")
    print("Laptop,2,70000")
    print("Mouse,5,500")
    print("Keyboard,3,1200")

def read_csv():
    print("Reading sales.csv")

def calculate_revenue():
    print("Laptop Revenue = 140000")
    print("Mouse Revenue = 2500")
    print("Keyboard Revenue = 3600")
    print("Total Revenue = 146100")

def create_summary():
    print("Creating summary")
    print("Laptop Revenue = 140000")
    print("Mouse Revenue = 2500")
    print("Keyboard Revenue = 3600")
    print("Total Revenue = 146100")

exercise_6_create_csv = PythonOperator(
    task_id="exercise_6_create_csv",
    python_callable=create_csv,
    dag=dag
)

exercise_6_read_csv = PythonOperator(
    task_id="exercise_6_read_csv",
    python_callable=read_csv,
    dag=dag
)

exercise_6_calculate_revenue = PythonOperator(
    task_id="exercise_6_calculate_revenue",
    python_callable=calculate_revenue,
    dag=dag
)

exercise_6_create_summary = PythonOperator(
    task_id="exercise_6_create_summary",
    python_callable=create_summary,
    dag=dag
)

exercise_6_create_csv >> exercise_6_read_csv >> exercise_6_calculate_revenue >> exercise_6_create_summary
