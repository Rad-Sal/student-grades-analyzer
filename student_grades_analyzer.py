"""
Created on Fri Aug 29 2025

@author: Lenovo
"""

import time

print("\nHello there :) I'm a teacher who just graded my students' exams and I want to see:\n")
print("1. A list of my students and their scores")
print("2. The average score of the whole class")
print("3. The best and worst students and their scores\n")
time.sleep(3)

# Get student names and scores from input
user_input = input("Enter students and their scores (e.g. Alice 85 Bob 90): ")
entries = user_input.split()

# Build a dictionary of student: score
students = {}
for i in range(0, len(entries), 2):
    students[entries[i]] = int(entries[i + 1])

# Number of students
num_students = len(students)
print(f"\nSo I have {num_students} students:\n")
time.sleep(2)

# Print each student's score
for name, score in students.items():
    print(f"{name}'s score is: {score}")
time.sleep(2)

# Calculate class average
total_score = sum(students.values())
average_score = total_score / num_students
print(f"\nThe class average of {num_students} students is: {average_score:.2f}\n")
time.sleep(2)

# Find best and worst students
best_student = max(students, key=students.get)
best_score = students[best_student]

worst_student = min(students, key=students.get)
worst_score = students[worst_student]

# Announce results
print("And finally, ladies and gentlemen, the best student of the class is:")
time.sleep(2)
print(f"*shouting* {best_student} with a score of {best_score}\n")
time.sleep(2)
print(f"Hey {worst_student}, it's ok... life is not just about school scores.")
print(f"You scored {worst_score} here, and 100 somewhere else where YOU are the best at!")
time.sleep(5)
