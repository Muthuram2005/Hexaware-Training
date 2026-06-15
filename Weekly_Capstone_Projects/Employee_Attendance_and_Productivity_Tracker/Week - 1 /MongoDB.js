// DATABASE
use EmployeeAttendanceDB

// employee_notes COLLECTION
db.createCollection("employee_notes")

// CRUD 

// CREATE

// 1
db.employee_notes.insertOne({
    note_id: 1,
    employee_id: 101,
    employee_name: "Rahul Sharma",
    department: "IT",
    feedback: "Excellent productivity and punctual attendance",
    rating: 5,
    note_date: new Date("2026-06-01")
})

// 2
db.employee_notes.insertMany([
{
    note_id: 2,
    employee_id: 102,
    employee_name: "Priya Singh",
    department: "HR",
    feedback: "Good communication skills",
    rating: 4
},
{
    note_id: 3,
    employee_id: 103,
    employee_name: "Arjun Kumar",
    department: "Finance",
    feedback: "Consistent performance",
    rating: 5
}
])

// 3
db.employee_notes.insertOne({
    note_id: 4,
    employee_id: 104,
    employee_name: "Sneha Patel",
    performance: {
        tasks_completed: 20,
        attendance_percentage: 98
    }
})

// 4
db.employee_notes.insertOne({
    note_id: 5,
    employee_id: 105,
    tags: ["punctual","team-player","productive"]
})

// 5
var doc = {
    note_id: 6,
    employee_id: 106,
    employee_name: "Vikram Rao",
    rating: 3
}
db.employee_notes.insertOne(doc)

// 6
db.employee_notes.bulkWrite([
{
insertOne:{
document:{
note_id:7,
employee_id:107,
employee_name:"Anjali"
}
}
},
{
insertOne:{
document:{
note_id:8,
employee_id:108,
employee_name:"Karan"
}
}
}
])

// READ

// 1
db.employee_notes.find()

// 2
db.employee_notes.find(
{},
{
employee_name:1,
department:1,
rating:1,
_id:0
}
)

// 3
db.employee_notes.find({
rating:{$gte:4},
department:"IT"
})

// 4
db.employee_notes.find().sort({
rating:-1
})

// 5
db.employee_notes.find()
.sort({rating:-1})
.limit(5)

// 6
db.employee_notes.aggregate([
{
$group:{
_id:"$department",
avgRating:{
$avg:"$rating"
}
}
}
])

// UPDATE

// 1
db.employee_notes.updateOne(
{note_id:1},
{$set:{rating:4}}
)

// 2
db.employee_notes.updateMany(
{department:"IT"},
{$set:{department:"Technology"}}
)

// 3
db.employee_notes.updateOne(
{note_id:2},
{$inc:{rating:1}}
)

// 4
db.employee_notes.updateMany(
{},
{$rename:{"feedback":"employee_feedback"}}
)

// 5
db.employee_notes.updateOne(
{note_id:5},
{$push:{tags:"hardworking"}}
)

// 6
db.employee_notes.updateOne(
{note_id:20},
{
$set:{
employee_name:"New Employee",
rating:5
}
},
{
upsert:true
}
)

// DELETE

// 1
db.employee_notes.deleteOne(
{note_id:8}
)

// 2
db.employee_notes.deleteMany(
{rating:{$lt:2}}
)

// 3
db.employee_notes.deleteMany(
{department:"Finance"}
)

// 4
db.employee_notes.deleteMany({
rating:1,
department:"HR"
})

// 5
db.employee_notes.deleteMany({
employee_id:106
})

// 6
db.employee_notes.drop()

// INDEXES

// 1
db.employee_notes.createIndex(
{
employee_id:1
}
)

// 2
db.employee_notes.createIndex(
{
department:1
}
)

// 3
db.employee_notes.createIndex(
{
employee_id:1,
department:1
}
)

// 4
db.employee_notes.createIndex(
{
note_id:1
},
{
unique:true
}
)

// 5
db.employee_notes.createIndex(
{
employee_feedback:"text"
}
)

// 6
db.employee_notes.getIndexes()
