# File Handling
# 1
import csv 
with open("orders.csv","r") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)

# 2
import csv 
with open("orders.csv","r") as file:
    reader = csv.reader(file)
    next(reader)
    for row in reader:
        print(row)

# 3
import csv 
count = 0
with open("orders.csv","r") as file:
    reader = csv.reader(file)
    next(reader)
    for row in reader:
        count += 1
print("Total orders :",count)

# Revenue Analysis
# 4
import csv
revenue = 0
with open("orders.csv","r") as file:
    reader = csv.reader(file)
    next(reader)
    for row in reader:
        revenue += int(row[5]) * int(row[6])
print("Total Revenue :",revenue)

# 5
import csv
highest = 0
with open("orders.csv","r") as file:
    reader = csv.reader(file)
    next(reader)
    for row in reader:
        revenue = int(row[5]) * int(row[6])
        if revenue > highest:
            highest = revenue
print("Highest Order :",highest)

# 6
import csv
lowest = 99999999
with open("orders.csv","r") as file:
    reader = csv.reader(file)
    next(reader)
    for row in reader:
        revenue = int(row[5]) * int(row[6])
        if revenue < lowest:
            lowest = revenue
print("Lowest Order :",lowest)

# 7
import csv
total = 0
count = 0
with open("orders.csv","r") as file:
    reader = csv.reader(file)
    next(reader)
    for row in reader:
        total += int(row[5]) * int(row[6])
        count += 1
print("Average Order :",(total/count))

# Customer Analysis
# 8
import csv
customers = set()
with open("orders.csv","r") as file:
    reader = csv.reader(file)
    next(reader)
    for row in reader:
        customers.add(row[1])
print("Unique Customers :",customers)

# 9
import csv
customers = set()
with open("orders.csv","r") as file:
    reader = csv.reader(file)
    next(reader)
    for row in reader:
        customers.add(row[1])
print("Count of  Unique Customers :",len(customers))

# 10
import csv
customers_purchase = {}
with open("orders.csv","r") as file:
    reader = csv.reader(file)
    next(reader)
    for row in reader:
        revenue = int(row[5]) * int(row[6])
        if row[1] not in customers_purchase:
            customers_purchase[row[1]] = revenue
        else:
            customers_purchase[row[1]] += revenue
name = max(customers_purchase, key=customers_purchase.get)
print("Customer with Highest Purchase :",name)
print("Amount :",customers_purchase[name])

# Product Analysis
# 11
import csv
products = {}
with open("orders.csv", "r") as file:
    reader = csv.reader(file)
    next(reader)
    for row in reader:
        product = row[3]
        if product not in products:
            products[product] = 1
        else:
            products[product] += 1
print("Count of Orders by Products :",products)

# 12
import csv
products = {}
with open("orders.csv", "r") as file:
    reader = csv.reader(file)
    next(reader)
    for row in reader:
        product = row[3]
        revenue = int(row[5]) * int(row[6])
        if product not in products:
            products[product] = revenue
        else:
            products[product] += revenue
print("Count of Revenue by Products :",products)

# 13
import csv
quantity = {}
with open("orders.csv", "r") as file:
    reader = csv.reader(file)
    next(reader)
    for row in reader:
        if row[3] not in quantity:
            quantity[row[3]] = int(row[5])
        else:
            quantity[row[3]] += int(row[5])
product = max(quantity, key = quantity.get)
print("Most Sold Product. :",product)
print("Sold Quantity :",quantity[product])

# 14
import csv
quantity = {}
with open("orders.csv", "r") as file:
    reader = csv.reader(file)
    next(reader)
    for row in reader:
        if row[3] not in quantity:
            quantity[row[3]] = int(row[5])
        else:
            quantity[row[3]] += int(row[5])
product = min(quantity, key = quantity.get)
print("Least Sold Product :",product)
print("Sold Quantity :",quantity[product])

# 15
import csv
category = {}
with open("orders.csv", "r") as file:
    reader = csv.reader(file)
    next(reader)
    for row in reader:
        revenue = int(row[5]) * int(row[6])
        if row[4] not in category:
            category[row[4]] = revenue
        else:
            category[row[4]] += revenue
print("Revenue by Category :",category)

# City Analysis
# 16
import csv
city = {}
with open("orders.csv", "r") as file:
    reader = csv.reader(file)
    next(reader)
    for row in reader:
        if row[2] not in city:
            city[row[2]] = 1
        else:
            city[row[2]] += 1
print("Orders by City :",city)

# 17
import csv
city = {}
with open("orders.csv", "r") as file:
    reader = csv.reader(file)
    next(reader)
    for row in reader:
        revenue = int(row[5]) * int(row[6])
        if row[2] not in city:
            city[row[2]] = revenue
        else:
            city[row[2]] += revenue
print("Revenue by City :",city)

# 18
import csv
cities = {}
with open("orders.csv", "r") as file:
    reader = csv.reader(file)
    next(reader)
    for row in reader:
        revenue = int(row[5]) * int(row[6])
        if row[2] not in cities:
            cities[row[2]] = revenue
        else:
            cities[row[2]] += revenue
city = max(cities, key = cities.get)
print("City of Highest Revenue :",city)
print("Revenue :",cities[city])

# Lists, Sets and Dictionaries
# 19
import csv
products = []
with open("orders.csv", "r") as file:
    reader = csv.reader(file)
    next(reader)
    for row in reader:
        products.append(row[3])
products.sort()
print("Sorted Prodcuts :",products)

# 20
import csv
cities = set()
with open("orders.csv", "r") as file:
    reader = csv.reader(file)
    next(reader)
    for row in reader:
        cities.add(row[2])
print("Unique Cities :",cities)

# 21
import csv
cities_revenue = {}
with open("orders.csv", "r") as file:
    reader = csv.reader(file)
    next(reader)
    for row in reader:
        revenue = int(row[5]) * int(row[6])
        if row[2] not in cities_revenue:
            cities_revenue[row[2]] = revenue
        else:
            cities_revenue[row[2]] += revenue
print("Dictionary ( city : revenue ) :",cities_revenue)

# 22
import csv
product_quantity = {}
with open("orders.csv", "r") as file:
    reader = csv.reader(file)
    next(reader)
    for row in reader:
        if row[3] not in product_quantity:
            product_quantity[row[3]] = int(row[5])
        else:
            product_quantity[row[3]] += int(row[5])
print("Dictionary (product : sold_quantity) :",product_quantity)

# Functions
# 23
import csv
def calculate_total_revenue():
    total = 0
    with open("orders.csv", "r") as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            total += int(row[5]) * int(row[6])
    return total
print("Total Revenue :",calculate_total_revenue())

# 24
import csv
def find_top_product():
    quantity = {}
    with open("orders.csv", "r") as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            if row[3] not in quantity:
                quantity[row[3]] = row[5]
            else:
                quantity[row[3]] += row[5]
    return max(quantity, key = quantity.get)
print("Top Product :",find_top_product())

# 25
import csv
def find_top_city():
    city = {}
    with open("orders.csv", "r") as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            revenue = int(row[5]) * int(row[6])
            if row[2] not in city:
                city[row[2]] = revenue
            else:
                city[row[2]] += revenue
    return max(city, key = city.get)
print("Top City :",find_top_city())

# 26
import csv
def find_average_order_value():
    total = 0
    count = 0
    with open("orders.csv", "r") as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            total += int(row[5]) * int(row[6]) 
            count += 1
    return total/count
print("Average Order Value :",find_average_order_value())

# Exception Handling
# 27
import csv
try:
    with open("orders.csv", "r") as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)
except FileNotFoundError:
    print("File Not Found")

# 28
import csv
try:
    with open("orders.csv", "r") as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            quantity = int(row[5])
            print(quantity)
except ValueError:
    print("Invalid Quantity Value")

# 29
import csv
try:
    with open("orders.csv", "r") as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            price = float(row[6])
            print(price)
except ValueError:
    print("Invalid Price Value")

# NumPy
# 30
import csv
import numpy as np
order_values = []
with open("orders.csv", "r") as file:
    reader = csv.reader(file)
    next(reader)
    for row in reader:
        order_values.append(int(row[5]) * int(row[6]))
arr = np.array(order_values)
print("Total Revenue :", np.sum(arr))
print("Average Revenue :", np.mean(arr))
print("Maximum Revenue :", np.max(arr))
print("Minimum Revenue :", np.min(arr))
print("Standard Deviation :", np.std(arr))

# Pandas
# 31
import pandas as pd
df = pd.read_csv("orders.csv")
print(df)

# 32
import pandas as pd
df = pd.read_csv("orders.csv")
df["Revenue"] = df["quantity"] * df["price"]
print(df)

# 33
import pandas as pd
df = pd.read_csv("orders.csv")
df["Revenue"] = df["quantity"] * df["price"]
print(df.sort_values("Revenue", ascending=False).head())

# 34
import pandas as pd
df = pd.read_csv("orders.csv")
df["Revenue"] = df["quantity"] * df["price"]
print(df.groupby("city")["Revenue"].sum())

# 35
import pandas as pd
df = pd.read_csv("orders.csv")
df["Revenue"] = df["quantity"] * df["price"]
print(df.groupby("product")["Revenue"].sum())

# 36
import pandas as pd
df = pd.read_csv("orders.csv")
df["Revenue"] = df["quantity"] * df["price"]
sales = df.groupby("product")["quantity"].sum()
print("Top Selling Product :",sales.idxmax())

# 37
import pandas as pd
df = pd.read_csv("orders.csv")
print(df.groupby("city")["order_id"].count())

# Report Generation
import csv
total_revenue = 0
highest = 0
lowest = 999999999
count = 0
city_revenue = {}
category_revenue = {}
product_quantity = {}
with open("orders.csv", "r") as file:
    reader = csv.reader(file)
    next(reader)
    for row in reader:
        revenue = int(row[5]) * int(row[6])
        total_revenue += revenue
        count += 1
        if revenue > highest:
            highest = revenue
        if revenue < lowest:
            lowest = revenue
        if row[2] not in city_revenue:
            city_revenue[row[2]] = revenue
        else:
            city_revenue[row[2]] += revenue

        if row[4] not in category_revenue:
            category_revenue[row[4]] = revenue
        else:
            category_revenue[row[4]] += revenue

        if row[3] not in product_quantity:
            product_quantity[row[3]] = int(row[5])
        else:
            product_quantity[row[3]] += int(row[5])
average = total_revenue / count
top_product = max(product_quantity, key=product_quantity.get)
top_city = max(city_revenue, key=city_revenue.get)
with open("sales_summary_report.txt", "w") as file:
    file.write("Total Orders : " + str(count) + "\n")
    file.write("Total Revenue : " + str(total_revenue) + "\n")
    file.write("Average Order Value : " + str(average) + "\n")
    file.write("Highest Order Value : " + str(highest) + "\n")
    file.write("Lowest Order Value : " + str(lowest) + "\n")
    file.write("Revenue By City : " + str(city_revenue) + "\n")
    file.write("Revenue By Category : " + str(category_revenue) + "\n")
    file.write("Top Selling Product : " + str(top_product) + "\n")
    file.write("Top Revenue Generating City : " + str(top_city) + "\n")
print("Report Generated Successfully")

# Bonus Tasks
# 38
import pandas as pd
df = pd.read_csv("orders.csv")
df["Revenue"] = df["quantity"] * df["price"]
high_value_orders = df[df["Revenue"] > 50000]
high_value_orders.to_csv("high_value_orders.csv", index=False)
print("high_value_orders.csv created successfully")

# 39
import pandas as pd
df = pd.read_csv("orders.csv")
electronics = df[df["category"] == "Electronics"]
electronics.to_csv("electronics_orders.csv", index=False)
print("electronics_orders.csv created successfully")

# 40
import csv
orders = []
try:
    with open("orders.csv", "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            row["quantity"] = int(row["quantity"])
            row["price"] = int(row["price"])
            row["revenue"] = row["quantity"] * row["price"]
            orders.append(row)
except FileNotFoundError:
    print("orders.csv File Not Found")
    exit()

def view_orders():
    print("\nALL ORDERS\n")
    for order in orders:
        print(order["order_id"], order["customer_name"], order["city"], order["product"], order["category"], order["quantity"], order["price"])

def revenue_analysis():
    total_revenue = 0
    highest = 0
    lowest = orders[0]["revenue"]
    for order in orders:
        revenue = order["revenue"]
        total_revenue += revenue
        if revenue > highest:
            highest = revenue
        if revenue < lowest:
            lowest = revenue
    average = total_revenue / len(orders)
    print("\nREVENUE ANALYSIS")
    print("Total Revenue :", total_revenue)
    print("Highest Order Value :", highest)
    print("Lowest Order Value :", lowest)
    print("Average Order Value :", average)

def product_analysis():
    quantity = {}
    revenue = {}
    for order in orders:
        product = order["product"]
        if product not in quantity:
            quantity[product] = order["quantity"]
        else:
            quantity[product] += order["quantity"]
        if product not in revenue:
            revenue[product] = order["revenue"]
        else:
            revenue[product] += order["revenue"]
    top_product = max(quantity, key=quantity.get)
    least_product = min(quantity, key=quantity.get)
    print("\nPRODUCT ANALYSIS")
    print("\nQuantity Sold")
    for product in quantity:
        print(product, ":", quantity[product])
    print("\nRevenue By Product")
    for product in revenue:
        print(product, ":", revenue[product])
    print("\nMost Sold Product :", top_product)
    print("Least Sold Product :", least_product)

def city_analysis():
    city_revenue = {}
    city_orders = {}
    for order in orders:
        city = order["city"]
        if city not in city_revenue:
            city_revenue[city] = order["revenue"]
        else:
            city_revenue[city] += order["revenue"]
        if city not in city_orders:
            city_orders[city] = 1
        else:
            city_orders[city] += 1
    top_city = max(city_revenue, key=city_revenue.get)
    print("\nCITY ANALYSIS")
    print("\nOrders By City")
    for city in city_orders:
        print(city, ":", city_orders[city])
    print("\nRevenue By City")
    for city in city_revenue:
        print(city, ":", city_revenue[city])
    print("\nTop Revenue City :", top_city)

def export_report():
    total_revenue = 0
    highest = 0
    lowest = orders[0]["revenue"]
    city_revenue = {}
    category_revenue = {}
    product_quantity = {}
    for order in orders:
        revenue = order["revenue"]
        total_revenue += revenue
        if revenue > highest:
            highest = revenue
        if revenue < lowest:
            lowest = revenue
        city = order["city"]
        if city not in city_revenue:
            city_revenue[city] = revenue
        else:
            city_revenue[city] += revenue
        category = order["category"]
        if category not in category_revenue:
            category_revenue[category] = revenue
        else:
            category_revenue[category] += revenue
        product = order["product"]
        if product not in product_quantity:
            product_quantity[product] = order["quantity"]
        else:
            product_quantity[product] += order["quantity"]
    average = total_revenue / len(orders)
    top_product = max(product_quantity, key=product_quantity.get)
    top_city = max(city_revenue, key=city_revenue.get)
    with open("sales_summary_report.txt", "w") as file:
        file.write("Total Orders : " + str(len(orders)) + "\n")
        file.write("Total Revenue : " + str(total_revenue) + "\n")
        file.write("Average Order Value : " + str(average) + "\n")
        file.write("Highest Order Value : " + str(highest) + "\n")
        file.write("Lowest Order Value : " + str(lowest) + "\n")
        file.write("Revenue By City : " + str(city_revenue) + "\n")
        file.write("Revenue By Category : " + str(category_revenue) + "\n")
        file.write("Top Selling Product : " + top_product + "\n")
        file.write("Top Revenue City : " + top_city + "\n")
    print("\nReport Generated Successfully")

while True:
    print("\n==============================")
    print("E-COMMERCE ORDER ANALYTICS")
    print("==============================")
    print("1. View Orders")
    print("2. Revenue Analysis")
    print("3. Product Analysis")
    print("4. City Analysis")
    print("5. Export Reports")
    print("6. Exit")
    choice = input("\nEnter Choice : ")
    if choice == "1":
        view_orders()
    elif choice == "2":
        revenue_analysis()
    elif choice == "3":
        product_analysis()
    elif choice == "4":
        city_analysis()
    elif choice == "5":
        export_report()
    elif choice == "6":
        print("Thank You")
        break
    else:
        print("Invalid Choice")
