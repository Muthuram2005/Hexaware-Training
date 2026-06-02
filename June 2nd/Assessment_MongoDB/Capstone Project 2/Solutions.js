// Basic Find Queries
// 1
db.learners.find()

// 2
db.courses.find()

// 3
db.learners.find({},{ _id: 0, name: 1, city: 1, goal: 1 })

// 4
db.learners.find({ city: "Hyderabad" })

// 5
db.learners.find({ goal: "AI Engineer" })

// 6
db.courses.find({ category: "Data Engineering" })

// 7
db.courses.find({ price: { $gt: 10000 } })

// 8
db.courses.find({ level: "Beginner" })

// 9
db.enrollments.find({ "payment.status": "Success" })

// 10
db.learners.find({ phone: null })

// Operators
// 11
db.learners.find({experience_years: { $gt: 2 }})

// 12
db.courses.find({price: { $gte: 8000, $lte: 18000 }})

// 13
db.courses.find({level: { $in: ["Beginner", "Intermediate"] }})

// 14
db.enrollments.find({"progress.completion_percent": { $gte: 80 }})

// 15
db.enrollments.find({"payment.status": { $ne: "Success" }})

// 16
db.learners.find({city: { $in: ["Hyderabad", "Bangalore", "Pune"] }})

// 17
db.courses.find({category: { $ne: "Cloud" }})

// Array Queries
// 18
db.instructors.find({expertise: "AI"})

// 19
db.instructors.find({expertise: "SQL"})

// 20
db.courses.find({tools: "Python"})

// 21
db.courses.find({tools: "Databricks"})

// 22
db.enrollments.find({quiz_scores: 95})

// 23
db.enrollments.find({quiz_scores: { $gt: 85 }})

// Sorting and Limit
// 24
db.courses.find().sort({ price: -1 })

// 25
db.courses.find().sort({ price: -1 }).limit(3)

// 26
db.learners.find().sort({ experience_years: -1 })

// 27
db.learners.find().sort({ experience_years: -1 }).limit(2)

// 28
db.instructors.find().sort({ rating: -1 })

// Update Operations
// 29
db.learners.updateOne({ learner_id: 1 },{ $set: { city: "Secunderabad" } })

// 30
db.courses.updateOne({ course_id: 203 },{ $set: { price: 9000 } })

// 31
db.enrollments.updateOne({ enrollment_id: 1006 },{ $set: { "progress.completion_percent": 30 } })

// 32
db.enrollments.updateOne({ enrollment_id: 1005 },{ $set: { status: "Inactive" } })

// 33
db.learners.updateMany({},{ $set: { active: true } })

// 34
db.learners.updateMany({},{ $unset: { active: "" } })

// 35
db.courses.updateOne({ course_id: 201 },{ $push: { tools: "MongoDB" } })

// Delete Operations
// 36
db.enrollments.deleteMany({"payment.status": "Failed"})

// 37
db.learners.deleteMany({experience_years: 0 })

// Count and Distinct
// 38
db.learners.countDocuments()

// 39
db.courses.countDocuments()

// 40
db.enrollments.countDocuments({"payment.status": "Success"})

// 41
db.learners.distinct("city")

// 42
db.courses.distinct("category")

// 43
db.enrollments.distinct("payment.mode")

// Aggregation
// 44
db.enrollments.aggregate([
{
 $group: {
  _id: "$payment.mode",
  totalRevenue: { $sum: "$payment.amount" }
 }
}
])

// 45
db.enrollments.aggregate([
{
 $group: {
  _id: "$course_id",
  revenue: { $sum: "$payment.amount" }
 }
}
])

// 46 
db.learners.aggregate([
{
 $group: {
  _id: "$goal",
  totalLearners: { $sum: 1 }
 }
}
])

// 47 
db.courses.aggregate([
{
 $group: {
  _id: "$category",
  averagePrice: { $avg: "$price" }
 }
}
])

// 48 
db.enrollments.aggregate([
{
 $group: {
  _id: "$course_id",
  averageCompletion: {
   $avg: "$progress.completion_percent"
  }
 }
}
])

// 49
db.enrollments.aggregate([
{
 $group: {
  _id: "$status",
  totalEnrollments: { $sum: 1 }
 }
}
])

// 50 
db.enrollments.aggregate([
{
 $group: {
  _id: "$course_id",
  revenue: { $sum: "$payment.amount" }
 }
},
{
 $match: {
  revenue: { $gt: 15000 }
 }
}
])

// Lookup / Join Queries
// 51 
db.enrollments.aggregate([
{
 $lookup: {
  from: "learners",
  localField: "learner_id",
  foreignField: "learner_id",
  as: "learner"
 }
},
{ $unwind: "$learner" },
{
 $project: {
  _id: 0,
  enrollment_id: 1,
  learner_name: "$learner.name",
  city: "$learner.city",
  course_id: 1,
  status: 1
 }
}
])

// 52 
db.enrollments.aggregate([
{
 $lookup: {
  from: "courses",
  localField: "course_id",
  foreignField: "course_id",
  as: "course"
 }
},
{ $unwind: "$course" },
{
 $project: {
  _id: 0,
  enrollment_id: 1,
  course_name: "$course.course_name",
  category: "$course.category",
  amount: "$payment.amount",
  payment_status: "$payment.status"
 }
}
])

// 53
db.courses.aggregate([
{
 $lookup: {
  from: "instructors",
  localField: "instructor_id",
  foreignField: "instructor_id",
  as: "instructor"
 }
},
{ $unwind: "$instructor" },
{
 $project: {
  _id: 0,
  course_name: 1,
  category: 1,
  instructor_name: "$instructor.instructor_name",
  instructor_rating: "$instructor.rating"
 }
}
])

// 54
db.enrollments.aggregate([
{
 $lookup: {
  from: "learners",
  localField: "learner_id",
  foreignField: "learner_id",
  as: "learner"
 }
},
{ $unwind: "$learner" },
{
 $lookup: {
  from: "courses",
  localField: "course_id",
  foreignField: "course_id",
  as: "course"
 }
},
{ $unwind: "$course" },
{
 $lookup: {
  from: "instructors",
  localField: "course.instructor_id",
  foreignField: "instructor_id",
  as: "instructor"
 }
},
{ $unwind: "$instructor" },
{
 $project: {
  _id: 0,
  enrollment_id: 1,
  learner_name: "$learner.name",
  city: "$learner.city",
  goal: "$learner.goal",
  course_name: "$course.course_name",
  category: "$course.category",
  instructor_name: "$instructor.instructor_name",
  payment_amount: "$payment.amount",
  payment_status: "$payment.status",
  completion_percent: "$progress.completion_percent",
  enrollment_status: "$status"
 }
}
])
