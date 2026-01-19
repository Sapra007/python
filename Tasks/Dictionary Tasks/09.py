#Find student with highest marks
students = {"John": 85, "Alice": 92, "Bob": 78, "Diana": 90}
top_student = max(students, key=students.get)
print(f"The student with the highest marks is {top_student} with {students[top_student]} marks.")

