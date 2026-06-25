from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime


def create_enrollment_file():
    data = [
        "Python,Rahul",
        "Python,Priya",
        "SQL,Amit",
        "Python,Sneha",
        "Power BI,Kiran",
        "SQL,Megha",
        "Power BI,Arjun"
    ]

    print("Enrollment Data")

    for row in data:
        print(row)


def count_students():
    data = [
        "Python,Rahul",
        "Python,Priya",
        "SQL,Amit",
        "Python,Sneha",
        "Power BI,Kiran",
        "SQL,Megha",
        "Power BI,Arjun"
    ]

    courses = {}

    for row in data:
        course, student = row.split(",")

        if course not in courses:
            courses[course] = 0

        courses[course] += 1

    for course, count in courses.items():
        print(course, "=", count)


def generate_course_report():
    print("Course Report Generated")
    print("Python = 3")
    print("SQL = 2")
    print("Power BI = 2")


with DAG(
    dag_id="course_enrollment_report",
    start_date=datetime(2026, 1, 1),
    schedule=None,
    catchup=False
) as dag:

    create_enrollment_file = PythonOperator(
        task_id="create_enrollment_file",
        python_callable=create_enrollment_file
    )

    count_students = PythonOperator(
        task_id="count_students",
        python_callable=count_students
    )

    generate_course_report = PythonOperator(
        task_id="generate_course_report",
        python_callable=generate_course_report
    )

    create_enrollment_file >> count_students >> generate_course_report
