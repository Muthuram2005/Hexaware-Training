import pandas as pd
import numpy as np

# LOAD DATA
df = pd.read_csv("employee_attendance.csv")

# CLEANING
df.drop_duplicates(inplace=True)
df["employee_name"] = df["employee_name"].astype(str).str.strip()
df["employee_name"] = df["employee_name"].replace(r"^\s*$", "Unknown Employee", regex=True)
df["department"] = df["department"].astype(str).str.strip().str.title()
df["attendance_date"] = pd.to_datetime(df["attendance_date"], errors="coerce")
df["clock_in"] = pd.to_datetime(df["clock_in"], errors="coerce")
df["clock_out"] = pd.to_datetime(df["clock_out"], errors="coerce")
num_cols = ["tasks_completed", "break_minutes", "absent_days"]
for col in num_cols:
    df[col] = pd.to_numeric(df[col], errors="coerce")

# VALIDATION 
df.loc[df["tasks_completed"] < 0, "tasks_completed"] = np.nan
df.loc[df["break_minutes"] < 0, "break_minutes"] = np.nan
df.loc[df["break_minutes"] > 480, "break_minutes"] = np.nan
df.loc[df["absent_days"] < 0, "absent_days"] = np.nan
df["tasks_completed"] = df["tasks_completed"].fillna(df["tasks_completed"].median())
df["break_minutes"] = df["break_minutes"].fillna(df["break_minutes"].median())
df["absent_days"] = df["absent_days"].fillna(0)

# REMOVE INVALID ROWS
df = df.dropna(subset=["attendance_date", "clock_in", "clock_out"])
df = df[df["clock_out"] >= df["clock_in"]]

# FEATURE ENGINEERING (NUMPY)
df["work_hours"] = (df["clock_out"] - df["clock_in"]).dt.total_seconds() / 3600
df["break_hours"] = df["break_minutes"] / 60
df["effective_work_hours"] = df["work_hours"] - df["break_hours"]
df = df[df["effective_work_hours"] > 0]
df["productivity_score"] = np.where(df["effective_work_hours"] > 0,np.round(df["tasks_completed"] / df["effective_work_hours"], 2),0)
df["attendance_status"] = np.where(df["absent_days"] > 0, "Absent", "Present")

# Top performers
top_performers = ( df.groupby("employee_name")["productivity_score"].mean().sort_values(ascending=False).head(10))

# Frequent absentees
frequent_absentees = (df.groupby("employee_name")["absent_days"].sum().sort_values(ascending=False).head(10))

# Department performance
department_summary = (df.groupby("department")
    .agg({
        "effective_work_hours": "mean",
        "productivity_score": "mean",
        "tasks_completed": "sum"
    }).round(2)
)

# OUTPUT 
print("\n========== TOP PERFORMERS ==========")
print(top_performers)

print("\n========== FREQUENT ABSENTEES ==========")
print(frequent_absentees)

print("\n========== DEPARTMENT SUMMARY ==========")
print(department_summary)

print("\n========== KPI SUMMARY ==========")
print("Total Employees:", df["employee_id"].nunique())
print("Total Records:", len(df))
print("Average Work Hours:", round(df["work_hours"].mean(), 2))
print("Average Productivity Score:", round(df["productivity_score"].mean(), 2))
print("Total Tasks Completed:", int(df["tasks_completed"].sum()))
print("Total Absent Days:", int(df["absent_days"].sum()))

# SAVE CLEAN DATA
df.to_csv("cleaned_employee_attendance.csv", index=False)
print("\nCleaned dataset saved successfully.")
