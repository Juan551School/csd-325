# Juan Macias Vasquez
# Date 06/28/2025
# Module 8.2 JSON Practice
# student_nabager.py

import json

# Load the JSON data from the file
def load_students(filename):
    with open(filename, 'r') as file:
        return json.load(file)

# Print each student's details
def print_students(students):
    for student in students:
        print(f"{student['L_Name']}, {student['F_Name']} : ID = {student['Student_ID']} , Email = {student['Email']}")

# Append new student data to the list
def add_student(students, first_name, last_name, student_id, email):
    new_student = {
        "F_Name": first_name,
        "L_Name": last_name,
        "Student_ID": student_id,
        "Email": email
    }
    students.append(new_student)

# Save the new updated student list to the JSON file
def save_students(filename, students):
    with open(filename, 'w') as file:
        json.dump(students, file, indent=4)

# === Main Program ===
filename = 'student.json'

# Load original data
students = load_students(filename)

# Display the original student list
print("\nOriginal Student List:")
print_students(students)

# Add my student info
add_student(students, "Juan", "Macias", 10000, "Student.email@example.com")

# Display the updated student list
print("\nUpdated Student List:")
print_students(students)

# Save the updated list back to the file
save_students(filename, students)

print("\nThe JSON file has been updated.")

