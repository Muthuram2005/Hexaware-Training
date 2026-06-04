# print statement
print("Hello World!") 

# Variables and Data types
customer_name = "Rahul Sharma"
age = 28
salary = 75000.50
is_active = True

print(customer_name)
print(age)
print(salary)
print(is_active)

# type function
print(type(customer_name))
print(type(age))
print(type(salary))
print(type(is_active))

# if-else statement
salary = 35000 

if salary > 50000:
    print("High Income")
else:
    print("Low Income") 

# Multiple conditions
salary = 75000
experience = 5

if salary > 50000 and experience >= 3:
    print("Eligible")
else:
    print("Not Eligible")

# if-elif-else statement
marks = 85

if marks >= 90:
    print("Grade A")
elif marks >= 75:
    print("Grade B")    
elif marks >= 60:
    print("Grade C")
else:
    print("Grade D")

# and operator 
experience = 5
salary = 80000

if experience >= 3 and salary >= 50000:
    print("Eligible")
else:
    print("Not Eligible")

# or operator
experience = 1
salary = 80000

if experience >= 3 or salary >= 50000:
    print("Eligible")
else:
    print("Not Eligible")

# not operator
is_blocked = False

if not is_blocked:
    print("Login Allowed")

# for loop
for i in range(1, 6):
    print(i)

# while loop
count = 1
while count <= 5:
    print(count)
    count += 1

# Data structures
# List
cities = ["Hyderabad","Mumbai","Delhi"]
print(cities)

# Accessing Elements
print(cities[0])
print(cities[1])
print(cities[2])

# Negative indexing
print(cities[-1])
print(cities[-2])

# Slicing
print(cities[0:2])

# Update an Element
cities[0] = "Bangalore"
print(cities)

# Append
cities.append("Chennai")
print(cities)

# Insert
cities.insert(1,"Pune")
print(cities)

# Multiple values
cities.extend(["Kochi","Pondi"])
print(cities)

# Remove
cities.remove("Mumbai")
print(cities)

# Pop
cities.pop(1)
print(cities)

# del
del cities[0]
print(cities)

# Clear
cities.clear()  
print(cities)

# Length
print(len(cities))

# Check Membership
print("Mumbai" in cities)
print("Pune" in cities)

# index 
print(cities.index("Mumbai"))

# sort
cities.sort()
print(cities)

# Tuple 
cities = ("Hyderabad","Mumbai","Delhi","Chennai","Pune")
print(cities)

# Accessing Elements
print(cities[0])
print(cities[1])

# Negative indexing
print(cities[-1])
print(cities[-2])

# Length
print(len(cities))

# Slicing
print(cities[1:4])

# Packing
employee = (101, "Rahul", 75000)
print(employee)

# Unpacking
emp_id, emp_name, salary = employee
print(emp_id)
print(emp_name)     
print(salary)

# Multiple Values
def get_employee():
    return 101, "Rahul", 75000

result = get_employee()
print(result)

# Each row represents as a Tuple
record = (
    101, 
    "Rahul",
    "Hyderabad", 
    75000
    )
print(record)

# Set
cities = {"Hyderabad", "Mumbai", "Delhi"}
print(cities)

# Remove Duplicates
cities = {"Hyderabad", "Mumbai", "Delhi", "Mumbai"}
print(cities)

# Add
cities.add("Chennai")
print(cities)

# Update
cities.update(["Delhi", "Pune"])
print(cities)

# Remove
cities.remove("Mumbai")
print(cities)
 
# Discard
cities.discard("Pune")
print(cities)

# union
set1 = {"Python", "SQL"}
set2 = {"MongoDB", "Python"}
result = set1.union(set2)
print(result)

# intersection
result = set1.intersection(set2)    
print(result)

# difference
result1 = set1.difference(set2)
result2 = set2.difference(set1)
print(result1)
print(result2)

# symmetric difference
result = set1.symmetric_difference(set2)
print(result)

# Dictornary
customer = {"customer_id": 101, "name": "Rahul", "city": "Hyderabad"}
print(customer)

# Accessing Values
print(customer["name"])
print(customer["city"])

# using get method
print(customer.get("name"))
print(customer.get("customer_id"))

# Adding
customer["salary"] = 75000
print(customer)

# Updating
customer["name"] = "Rahul Sharma"
print(customer)

# Pop
customer.pop("salary")
print(customer)

# del
del customer["salary"]
