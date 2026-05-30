// use database
use retail_db

// create table
db.createCollection("customers")

// insert one value
db.customers.insertOne({
  customer_id: 1,
  name: "Rahul",
  city: "Hyderabad",
  phone: "8963547582"
})

// insert many values
db.customers.insertMany([
  {
    customer_id: 2,
    name: "Anu",
    city: "Chennai",
    phone: "8958278910"
  },
  {
    customer_id: 3,
    name: "Bala",
    city: "Mumbai",
    phone: "8956741252"
  }
])

// view all values
db.customers.find()

// where
db.customers.find({
  city: "Hyderabad"
})

// greater than 
db.customers.find({
  customer_id: { $gt: 2 }
})

// less than
db.customers.find({
  customer_id: { $lt: 3 }
})

// less than and equal
db.customers.find({
  customer_id: { $lte: 3 }
})

// greater than and equal
db.customers.find({
  customer_id: { $gte: 2 }
})

// in
db.customers.find({
  city: { $in: ["Mumbai", "Chennai"] }
})

// and
db.customers.find({
  city: "Mumbai",
  name: "Bala"
})

// or
db.customers.find({
  $or: [
    { city: "Mumbai" },
    { city: "Chennai" }
  ]
})

// Projection
db.customers.find(
  {},
  {
    name: 1,
    city: 1,
    _id: 0
  }
)

// sort (ASC)
db.customers.find().sort({
  name: 1
})

// sort(DESC)
db.customers.find().sort({
  name: -1
})

// limiting
db.customers.find().limit(2)
