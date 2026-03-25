# Student Data Manager - Upgraded Version

# Function to calculate grade
def calculate_grade(marks):
    if marks >= 90:
        return "A+"
    elif marks >= 75:
        return "A"
    elif marks >= 60:
        return "B"
    elif marks >= 50:
        return "C"
    else:
        return "Fail"

# Store data for 5 students
students = {}

for i in range(5):
    print(f"\nEnter details for Student {i+1}")
    name = input("Name: ")

    while True:
        marks = float(input("Marks (0-100): "))
        if 0 <= marks <= 100:
            break
        else:
            print("Invalid marks! Please enter between 0 and 100.")

    students[name] = {
        "Marks": marks,
        "Grade": calculate_grade(marks)
    }

# ---- Calculations ----

# Topper
topper = max(students, key=lambda x: students[x]["Marks"])

# Lowest scorer
lowest = min(students, key=lambda x: students[x]["Marks"])

# Class Average
total_marks = sum(student["Marks"] for student in students.values())
average = total_marks / len(students)

# Grade Distribution
grade_count = {}
for details in students.values():
    grade = details["Grade"]
    grade_count[grade] = grade_count.get(grade, 0) + 1

# Sort students by marks (highest to lowest)
sorted_students = sorted(students.items(), key=lambda x: x[1]["Marks"], reverse=True)

# ---- Display Results ----
print("\n----- Student Report -----")

for name, details in sorted_students:
    print(f"Name: {name}, Marks: {details['Marks']}, Grade: {details['Grade']}")

print("\nTopper:", topper, "-", students[topper]["Marks"])
print("Lowest Marks:", lowest, "-", students[lowest]["Marks"])
print("Class Average:", round(average, 2))

print("\nGrade Distribution:")
for grade, count in grade_count.items():
    print(grade, ":", count)