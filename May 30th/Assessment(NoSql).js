// 1
db.restaurants.find()

// 2
db.restaurants.find({}, {name:1, city:1, cuisine:1, _id:0})

// 3
db.restaurants.find({city:"Hyderabad"})

// 4
db.restaurants.find({cuisine:"Indian"})

// 5
db.restaurants.find({delivery_available:true})

// 6
db.restaurants.find({rating:{$gt:4.5}})

// 7
db.restaurants.find({avg_order_value:{$lt:400}})

// 8
db.restaurants.find({rating:{$gte:4.0,$lte:4.7}})

// 9
db.restaurants.find({avg_order_value:{$gte:600}})

// 10
db.restaurants.find({city:"Hyderabad",delivery_available:true})

// 11
db.restaurants.find({
$or:[
{city:"Chennai"},
{cuisine:"Indian"}
]
})

// 12
db.restaurants.find({delivery_available:false})

// 13
db.restaurants.find({
city:{$in:["Hyderabad","Delhi","Mumbai"]}
})

// 14
db.restaurants.find({
cuisine:{$in:["Indian","Italian","Cafe"]}
})

// 15
db.restaurants.find({
city:{$nin:["Hyderabad","Bangalore"]}
})

// 16
db.restaurants.find({name:/^P/})

// 17
db.restaurants.find({name:/Point/})

// 18
db.restaurants.find({cuisine:/Food/})

// 19
db.restaurants.find({"contact.phone":null})

// 20
db.restaurants.find({"contact.email":null})

// 21
db.restaurants.find({
$or:[ {"contact.phone":null}, {"contact.email":null} ]
})

// 22
db.restaurants.find({tags:"premium"})

// 23
db.restaurants.find({tags:"fast food"})

// 24
db.restaurants.find({
tags:{$all:["north indian","premium"]}
})

// 25
db.restaurants.find().sort({rating:-1})

// 26
db.restaurants.find().sort({rating:-1}).limit(3)

// 27
db.restaurants.find().sort({avg_order_value:1})

// 28
db.restaurants.find().sort({avg_order_value:-1}).limit(2)

// 29
db.restaurants.updateOne(
{name:"Burger Street"}, {$set:{rating:4.0}}
)

// 30
db.restaurants.updateOne(
{name:"Tea Tales"}, {$set:{delivery_available:true}}
)

// 31
db.restaurants.updateMany(
{},
{$set:{active:true}}
)

// 32
db.restaurants.updateOne(
{name:"Spice Hub"}, {$push:{tags:"popular"}}
)

// 33
db.restaurants.updateMany(
{},
{$unset:{active:""}}
)

// 34
db.restaurants.deleteOne({restaurant_id:6})

// 35
db.restaurants.deleteMany({rating:{$lt:4.0}})

// 36
db.restaurants.countDocuments()

// 37
db.restaurants.countDocuments({delivery_available:true})

// 38
db.restaurants.distinct("city")

// 39
db.restaurants.distinct("cuisine")

// 40
db.restaurants.aggregate([
{ 
  $group:{_id:"$city", count:{$sum:1}}
}
])

// 41
db.restaurants.aggregate([
{
$group:{_id:"$cuisine", count:{$sum:1}}
}
])

// 42
db.restaurants.aggregate([
{
$group:{_id:"$cuisine", avgRating:{$avg:"$rating"}}
}
])

// 43
db.restaurants.aggregate([
{
$group:{_id:"$city", avgOrderValue:{$avg:"$avg_order_value"}}
}
])

// 44
db.restaurants.aggregate([
{
$group:{_id:"$cuisine",avgOrderValue:{$avg:"$avg_order_value"}}
},
{$sort:{avgOrderValue:-1}},
{$limit:1}
])

// 45
db.restaurants.aggregate([
{
$group:{_id:"$cuisine", count:{$sum:1}}
},
{$match:{count:{$gt:1}}}
])
