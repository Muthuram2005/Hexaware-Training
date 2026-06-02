# Food Delivery Business Analysis using MongoDB

## Database Design

The database is designed to support the operations of a food delivery platform. Four collections are used:

### customers

Stores customer information such as customer ID, name, city, membership type, and phone number.

### restaurants

Stores restaurant details including restaurant ID, restaurant name, city, cuisine type, and rating.

### delivery_partners

Stores delivery partner information such as partner ID, partner name, city, and rating.

### orders

Stores order transactions including customer information, restaurant information, delivery partner information, ordered items, payment details, delivery status, ratings, and order amount.

---

## Collection Relationships

Although MongoDB is a NoSQL database, logical relationships exist between collections.

### customers → orders

One customer can place multiple orders.

Relationship:
customer_id → orders.customer_id

### restaurants → orders

One restaurant can receive multiple orders.

Relationship:
restaurant_id → orders.restaurant_id

### delivery_partners → orders

One delivery partner can deliver multiple orders.

Relationship:
partner_id → orders.partner_id

These relationships are connected using MongoDB's $lookup aggregation operator whenever reporting or analysis is required.

---

## Key Insights from Reports

### Revenue Analysis

Revenue can be analyzed based on payment modes and order status. UPI payments generated the highest contribution among successful transactions.

### Customer Analysis

Gold members contributed significantly to total revenue. Repeat customers generated higher order volumes compared to other membership categories.

### Restaurant Performance

Restaurants with higher ratings generally received more customer orders and generated greater revenue.

### Delivery Performance

Delivered orders had an average delivery time between 30 and 50 minutes. Delivery partner ratings can be used to evaluate operational efficiency.

### Payment Analysis

Most payments were successful, while failed and pending payments represented a small percentage of total transactions.

### Business Benefits

The MongoDB solution enables the company to:

* Track customer behavior
* Monitor restaurant performance
* Analyze revenue trends
* Evaluate delivery efficiency
* Improve customer satisfaction through ratings analysis
* Generate city-wise business insights
