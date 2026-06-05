# Exercise on File Handling
# Text Document
# 1
with open("employees.txt", "r") as f:
    print(f.read())

# 2
with open("employees.txt", "r") as f:
    for line in f:
        print(line.strip())

# 3
count = 0
with open("employees.txt", "r") as f:
    for line in f:
        count = count + 1
print("Total Employees =", count)

# 4
with open("employees.txt", "r") as f:
    for line in f:
        data = line.strip().split(",")
        print(data[1])

# 5
with open("employees.txt", "r") as f:
    for line in f:
        data = line.strip().split(",")
        if data[4] == "Hyderabad":
            print(line.strip())
          
# 6
with open("employees.txt", "r") as f:
    for line in f:
        data = line.strip().split(",")
        if data[4] == "Bangalore":
            print(line.strip())

# 7
with open("employees.txt", "r") as f:
    for line in f:
        data = line.strip().split(",")
        if int(data[3]) > 80000:
            print(line.strip())

# 8
highest = 0
with open("employees.txt", "r") as f:
    for line in f:
        data = line.strip().split(",")
        salary = int(data[3])
        if salary > highest:
            highest = salary
print("Highest Salary =", highest)

# 9
lowest = 999999
with open("employees.txt", "r") as f:
    for line in f:
        data = line.strip().split(",")
        salary = int(data[3])
        if salary < lowest:
            lowest = salary
print("Lowest Salary =", lowest)

# 10
total = 0
count = 0
with open("employees.txt", "r") as f:
    for line in f:
        data = line.strip().split(",")
        total = total + int(data[3])
        count = count + 1
average = total / count
print("Average Salary =", average)

# 11
total = 0
with open("employees.txt", "r") as f:
    for line in f:
        data = line.strip().split(",")
        total = total + int(data[3])
print("Total Salary Payout =", total)

# 12
count = 0
with open("employees.txt", "r") as f:
    for line in f:
        data = line.strip().split(",")
        if data[2] == "AI Engineering":
            count = count + 1
print("AI Engineering Employees =", count)

# 13
count = 0
with open("employees.txt", "r") as f:
    for line in f:
        data = line.strip().split(",")
        if data[2] == "Data Engineering":
            count = count + 1
print("Data Engineering Employees =", count)

# 14
with open("employees.txt", "r") as f:
    for line in f:
        data = line.strip().split(",")
        if data[2] == "AI Engineering":
            print(line.strip())

# 15
with open("employees.txt", "r") as f:
    with open("high_salary_employees.txt", "w") as out:
        for line in f:
            data = line.strip().split(",")
            if int(data[3]) > 80000:
                out.write(line)
print("high_salary_employees.txt created")

# 16
with open("employees.txt", "r") as f:
    with open("hyderabad_employees.txt", "w") as out:
        for line in f:
            data = line.strip().split(",")
            if data[4] == "Hyderabad":
                out.write(line)
print("hyderabad_employees.txt created")

# 17
cities = []
with open("employees.txt", "r") as f:
    for line in f:
        data = line.strip().split(",")
        if data[4] not in cities:
            cities.append(data[4])
for city in cities:
    print(city)
print("Count =", len(cities))

# 18
dept_count = {}
with open("employees.txt", "r") as f:
    for line in f:
        dept = line.strip().split(",")[2]
        dept_count[dept] = dept_count.get(dept, 0) + 1
for dept, count in dept_count.items():
    print(dept, "=", count)

# 19
highest_salary = 0
employee_name = ""
with open("employees.txt", "r") as f:
    for line in f:
        data = line.strip().split(",")
        salary = int(data[3])
        if salary > highest_salary:
            highest_salary = salary
            employee_name = data[1]
print(employee_name)
print(highest_salary)

# 20
total = 0
count = 0
highest = 0
lowest = 999999
with open("employees.txt", "r") as f:
    for line in f:
        data = line.strip().split(",")
        salary = int(data[3])
        total = total + salary
        count = count + 1
        if salary > highest:
            highest = salary
        if salary < lowest:
            lowest = salary
average = total / count
with open("employee_report.txt", "w") as report:
    report.write("Employee Report\n")
    report.write("-------------------\n")
    report.write("Total Employees = " + str(count) + "\n")
    report.write("Highest Salary = " + str(highest) + "\n")
    report.write("Lowest Salary = " + str(lowest) + "\n")
    report.write("Average Salary = " + str(average) + "\n")
    report.write("Total Salary = " + str(total) + "\n")
print("employee_report.txt created")

# JSON File
# 1
import json
with open("employees.json", "r") as file:
    employees = json.load(file)
highest_salary = employees[0]
for employee in employees:
    if employee["salary"] > highest_salary["salary"]:
        highest_salary = employee
print(highest_salary["name"], ":", highest_salary["salary"])

# 2
import json
with open("employees.json", "r") as file:
    employees = json.load(file)
total = 0
for employee in employees:
    total += employee["salary"]
avg_sal = total / len(employees)
print(avg_sal)

# 3
import json
with open("employees.json", "r") as file:
    employees = json.load(file)
for employee in employees:
    if employee["department"] == "Data Engineering":
        print(employee)

# 4
import json
with open("employees.json", "r") as file:
    employees = json.load(file)
for employee in employees:
    if employee["salary"] > 80000:
        print(employee)

# 5
import json
with open("employees.json", "r") as file:
    employees = json.load(file)
for employee in employees:
    if employee["employee_id"] == 103:
        employee["salary"] = 70000
with open("employees.json", "w") as file:
    json.dump(employees, file, indent=4)
print("Salary Updated")

# 6
import json
with open("employees.json", "r") as file:
    employees = json.load(file)
new_employee = {
    "employee_id": 106,
    "name": "Kiran Rao",
    "department": "Data Engineering",
    "salary": 88000,
    "city": "Pune"
}
employees.append(new_employee)
with open("employees.json", "w") as file:
    json.dump(employees, file, indent=4)
print("Employee Added")

# 7
import json
with open("employees.json", "r") as file:
    employees = json.load(file)
for employee in employees:
    if employee["employee_id"] == 102:
        employees.remove(employee)
        break
with open("employees.json", "w") as file:
    json.dump(employees, file, indent=4)
print("Employee Deleted")

# CSV File
# 4
import csv
highest_salary = 0
highest_employee = ""
with open("employees.csv", "r") as file:
    reader = csv.reader(file)
    next(reader)
    for row in reader:
        salary = int(row[3])
        if salary > highest_salary:
            highest_salary = salary
            highest_employee = row[1]
print(highest_employee)
print(highest_salary)

# 5
import csv
lowest_salary = None
lowest_employee = ""
with open("employees.csv", "r") as file:
    reader = csv.reader(file)
    next(reader)
    for row in reader:
        salary = int(row[3])
        if lowest_salary is None or salary < lowest_salary:
            lowest_salary = salary
            lowest_employee = row[1]
print(lowest_employee)
print(lowest_salary)

# 6
import csv
total = 0
count = 0
with open("employees.csv", "r") as file:
    reader = csv.reader(file)
    next(reader)
    for row in reader:
        total += int(row[3])
        count += 1
print(total / count)

# 7
import csv
total = 0
with open("employees.csv", "r") as file:
    reader = csv.reader(file)
    next(reader)
    for row in reader:
        total += int(row[3])
print(total)

# 8
import csv
with open("employees.csv", "r") as file:
    reader = csv.reader(file)
    next(reader)
    for row in reader:
        if row[4] == "Hyderabad":
            print(row)

# 9
import csv
with open("employees.csv", "r") as file:
    reader = csv.reader(file)
    next(reader)
    for row in reader:
        if row[2] == "AI Engineering":
            print(row)

# 10
import csv
with open("employees.csv", "r") as file:
    reader = csv.reader(file)
    next(reader)
    for row in reader:
        if int(row[3]) > 80000:
            print(row)
