# EdTech Learning Analytics Management System Using MongoDB

## Database Design

The database is designed to support the operations and analytics of an EdTech learning platform. Four collections are used:

### learners

Stores learner information such as learner ID, name, city, years of experience, career goal, and contact details.

### instructors

Stores instructor details including instructor ID, instructor name, areas of expertise, and instructor ratings.

### courses

Stores course information including course ID, course name, category, instructor ID, price, difficulty level, and tools covered in the course.

### enrollments

Stores enrollment transactions including learner information, course information, enrollment date, payment details, course progress, quiz scores, and enrollment status.

---

## Collection Relationships

Although MongoDB is a NoSQL database, logical relationships exist between collections.

### learners → enrollments

One learner can enroll in multiple courses.

Relationship:

learner_id → enrollments.learner_id

### courses → enrollments

One course can have multiple learner enrollments.

Relationship:

course_id → enrollments.course_id

### instructors → courses

One instructor can teach multiple courses.

Relationship:

instructor_id → courses.instructor_id

These relationships are connected using MongoDB's $lookup aggregation operator whenever reporting or analytics are required.

---

## Key Insights from Reports

### Revenue Analysis

Revenue can be analyzed by payment mode and course. UPI and Card payments contribute the majority of successful revenue transactions.

### Learner Analysis

Learners with goals such as AI Engineer and Data Engineer represent significant enrollment demand. Experience levels help identify beginner and advanced learner segments.

### Course Performance

Popular courses generate higher revenue and enrollment counts. Course completion percentages provide insight into learner engagement and course effectiveness.

### Instructor Performance

Instructor ratings can be used to evaluate teaching quality. Highly rated instructors generally attract more enrollments and contribute to learner success.

### Payment Analysis

Most enrollments have successful payments, while pending and failed payments help identify potential revenue leakage and operational issues.

### Learning Progress Analysis

Completion percentages and quiz scores provide valuable insights into learner performance, engagement levels, and course effectiveness.

### Business Benefits

The MongoDB solution enables the organization to:

* Track learner progress and performance
* Monitor course popularity and completion rates
* Analyze revenue trends across courses and payment modes
* Evaluate instructor effectiveness
* Identify high-performing learning programs
* Generate learner, course, and instructor analytics reports
* Support data-driven business decisions for the EdTech platform
