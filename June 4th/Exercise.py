# List
salaries = [45000, 55000, 65000, 75000, 85000]

# 1
print(salaries)

# 2
print("Maximum Salary:", max(salaries))
print("Minimum Salary:", min(salaries))

# 3
print("Total Salary Payout:", sum(salaries))

# 4
print("Average Salary:", sum(salaries) / len(salaries))

# 5
salaries.append(95000)
salaries.append(105000)

# 6
salaries.remove(55000)

# 7
print(sorted(salaries))

# 8
print(sorted(salaries, reverse=True))

# 9
print(sorted(salaries, reverse=True)[1])

# 10
print([salary for salary in salaries if salary > 70000])

# Tuple
employee = (
    101,
    "Rahul Sharma",
    "Data Engineering",
    75000
)

# 11
print(employee)

# 12
print(employee[1])

# 13
print(employee[2])

# 14
emp_id, name, department, salary = employee
print(emp_id, name, department, salary)

# 15
print(len(employee))
print(employee[0])
print(employee[-1])

# Set
batch_a = {"Rahul", "Priya", "Amit", "Sneha", "Farhan"}
batch_b = {"Priya", "Sneha", "Neha", "Arjun", "Farhan"}

# 16
print(batch_a.intersection(batch_b))

# 17
print(batch_a - batch_b)

# 18
print(batch_b - batch_a)

# 19
print(batch_a.union(batch_b))

# 20
print(batch_a.symmetric_difference(batch_b))

# Dictionary
employee_info = {
    "employee_id": 101,
    "name": "Rahul Sharma",
    "department": "Data Engineering",
    "salary": 75000,
    "city": "Hyderabad"
}

# 21
print(employee_info["name"])

# 22
print(employee_info["department"])
print(employee_info["city"])

# 23
employee_info["experience"] = 5

# 24
employee_info["salary"] = 85000

# 25
employee_info.pop("city")

# 26
print(employee_info.keys())

# 27
print(employee_info.values())

# 28
print(employee_info.items())

# List of Dictionaries
employees = [
    {"id": 101, "name": "Rahul", "department": "IT", "salary": 50000},
    {"id": 102, "name": "Priya", "department": "HR", "salary": 70000},
    {"id": 103, "name": "Amit", "department": "IT", "salary": 60000},
    {"id": 104, "name": "Sneha", "department": "Finance", "salary": 80000},
    {"id": 105, "name": "Farhan", "department": "IT", "salary": 90000}
]

# 29
for emp in employees:
    print(emp["name"])

# 30
for emp in employees:
    if emp["department"] == "IT":
        print(emp)

# 31
print(max(employees, key=lambda x: x["salary"]))

# 32
print(min(employees, key=lambda x: x["salary"]))

# 33
print(sum(emp["salary"] for emp in employees) / len(employees))

# 34
print(sum(emp["salary"] for emp in employees))

# 35
for emp in employees:
    if emp["salary"] > 70000:
        print(emp)

# 36
print(sum(1 for emp in employees if emp["department"] == "IT"))

# 37
for emp in sorted(employees, key=lambda x: x["salary"], reverse=True):
    print(emp["name"])

# 38
print(sorted(employees, key=lambda x: x["salary"], reverse=True)[1])

# 39
print({emp["department"] for emp in employees})
