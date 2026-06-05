# Exception handling
a = 10
b = 0   
try:
    result = a/b
    print(result)
except:
    print("Error Detected")
print("Program Completed")

# Specific Exception 
a = 10
b = 0   
try:
    result = a/b
    print(result)
except ZeroDivisionError:
    print("Cannot divide by zero")

try:
    age = int(input("Enter age: "))
    print(age)
except ValueError:
    print("Please enter a numeric value")

# Multiple Exception
try:
    age = int(input("Enter age: "))
    result = 100/age    
    print(result)
except ValueError:
    print("Invalid Number")
except ZeroDivisionError:
    print("Age cannot be zero")

# Exception object
try:
    num = int("abc")
    print(num)
except Exception as e:
    print(e)

# Else block
try:
    num = 10
    print(num)
except:
    print("Error")
else:
    print("Success")    

# Finally Block
try:
    print(10/0)
except:
    print("Error")
finally:
    print("Connection Closed")

# Raise Error
salary = -1000
if salary < 0:
    raise ValueError("Salary cannot be negative")

# File Handling in Python
''' 
employees.txt
Rahul Sharma
Priya Reddy
Amit Kumar
Sneha Patel
Farhan Ali
Neha Singh
Arjun Verma
Meera Nair
Kiran Rao
Ravi Kumar 
'''

# Open a file
file = open("employees.txt", "r")

# Reading a file
data = file.read()
print(data)

# read one line
print(file.readline())

# Multiple lines
lines = file.readlines()    
print(lines)

# File object closing
file.close()

# Automatic file closing
with open("employees.txt", "r") as file:
    data = file.read()
    print(data)

# Write 
with open("employees1.txt", "w") as file:
    file.write("Rahul\n")
    file.write("Priya\n")

# Append
with open("employees.txt", "a") as file:
    file.write("Amit\n")

# Json Format
import json
employees = [
    {
        "employee_id": 101,
        "name": "Rahul Sharma",
        "department": "Data Engineering",
        "salary": 75000,
        "city": "Hyderabad"
    },

    {
        "employee_id": 102,
        "name": "Priya Reddy",
        "department": "AI Engineering",
        "salary": 85000,
        "city": "Bangalore"
    },

    {
        "employee_id": 103,
        "name": "Amit Kumar",
        "department": "Data Engineering",
        "salary": 65000,
        "city": "Mumbai"
    },

    {
        "employee_id": 104,
        "name": "Sneha Patel",
        "department": "Data Science",
        "salary": 95000,
        "city": "Chennai"
    },

    {
        "employee_id": 105,
        "name": "Farhan Ali",
        "department": "Cloud Engineering",
        "salary": 80000,
        "city": "Delhi"
    }
]

with open("employees.json","w") as file:
    json.dump(employees, file, indent = 4)

print("JSON file created successfully")

# Read json
with open("employees.json","r") as file:
    employees = json.load(file)
print(employees)

# All Employees
for employee in employees:
    print(employee)

# Names
for employee in employees:
    print(employee["name"])
    
# No of Employees
print(len(employees))

# Highest Salary
highest_salary = 0
for employee in employees:
    if employee["salary"] > highest_salary:
        highest_salary = employee["salary"]
print(highest_salary)

# CSV file
'''
employee_id,name,department,salary,city
101,Rahul Sharma,Data Engineering,75000,Hyderabad
102,Priya Reddy,AI Engineering,85000,Bangalore
103,Amit Kumar,Data Engineering,65000,Mumbai
104,Sneha Patel,Data Science,95000,Chennai
105,Farhan Ali,Cloud Engineering,80000,Delhi
'''
# Read
import csv 
with open("employees.csv","r") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)

# Skipping header
import csv 
with open("employees.csv","r") as file:
    reader = csv.reader(file)
    next(reader)
    for row in reader:
        print(row)

# Names
with open("employees.csv","r") as file:
    reader = csv.reader(file)
    next(reader)
    for row in reader:
        print(row[1])  

# Count Employees
count = 0
import csv 
with open("employees.csv","r") as file:
    reader = csv.reader(file)
    next(reader)
    for row in reader:
        count += 1
print(count)

# Numpy
# 1D array
import numpy as np
arr = np.array([10, 20, 30, 40, 50])
print(arr)

# Adding
print(arr + 5)

# Multiplication
print(arr * 2)

# Sum
print(np.sum(arr))

# Mean
print(np.mean(arr))

# Max
print(np.max(arr))

# Min
print(np.min(arr))

# S
print(arr.shape)

# 2D array
arr = np.array([[10, 20, 30], [40, 50, 60]])
print(arr)

# Zeros
arr = np.zeros((3,4))
print(arr)

# Ones
arr = np.ones((2,3))
print(arr)

# Arange
arr = np.arange(1, 11)
print(arr)

# Pandas
import pandas as pd
data = {
    "employee_id": [101,102,103],
    "name": [
        "Rahul",
        "Priya",
        "Amit"
    ],
    "salary": [
        75000,
        85000,
        65000
    ]
}
df = pd.DataFrame(data)
print(df) 

# Reading csv
df = pd.read_csv("employees.csv")
print(df)

# Head
print(df.head())

# Tail
print(df.tail())

# Data Types of each one
print(df.dtypes)

# DataFrame information
print(df.info())

# Statistics
print(df.describe())

# Particular Column
print(df["name"])

# Multiple Column
print(df[["name","salary"]])
