# Online Retail Sales Analytics Database

## 1. Database Design

The Online Retail Sales Analytics Database was designed to manage and analyze sales transactions of an online retail company operating across multiple Indian cities.

The database consists of six tables:

1. Customers – Stores customer information.
2. Products – Stores product details and pricing.
3. Orders – Stores customer orders.
4. Order_Items – Stores products purchased in each order.
5. Payments – Stores payment information for orders.
6. Deliveries – Stores shipment and delivery information.

The design follows relational database principles and minimizes data redundancy by separating data into logical entities.

---

## 2. Table Relationships

### Customers → Orders

One customer can place multiple orders.

Relationship:
Customers (1) → Orders (Many)

### Orders → Order_Items

One order can contain multiple products.

Relationship:
Orders (1) → Order_Items (Many)

### Products → Order_Items

One product can appear in multiple orders.

Relationship:
Products (1) → Order_Items (Many)

### Orders → Payments

Each order has a payment record.

Relationship:
Orders (1) → Payments (1)

### Orders → Deliveries

Each order has a delivery record.

Relationship:
Orders (1) → Deliveries (1)

Foreign keys are used to maintain referential integrity between related tables.

---

## 3. Key Insights from Reports

### Customer Analysis

* Customers are distributed across multiple cities.
* Gold and Platinum members contribute significantly to revenue.
* Some customers place multiple orders, indicating loyal customers.

### Product Analysis

* Electronics products generate the highest revenue.
* Frequently purchased products can be identified using quantity sold reports.
* Product categories can be compared using category-wise revenue analysis.

### Sales Analysis

* Total revenue can be calculated using successful payments.
* Average order value helps evaluate customer spending behavior.
* High-value orders contribute significantly to overall sales.

### Payment Analysis

* UPI is a commonly used payment method.
* Failed and pending payments can be tracked for operational improvements.

### Delivery Analysis

* Pending deliveries help monitor logistics performance.
* Delivered orders measure fulfillment success.
* Cancelled orders can be analyzed for business improvements.

### Data Quality Analysis

* Missing payment records and delivery records can be identified.
* Invalid customer IDs and product IDs can be detected.
* Zero-value or NULL payments can be investigated for data issues.

Overall, the database provides a complete analytical solution for customer behavior, product performance, sales revenue, payment tracking, and delivery monitoring.
