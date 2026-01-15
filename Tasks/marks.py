name = input("Enter student name: ")

m1 = int(input("Enter subject 1 marks: "))
m2 = int(input("Enter subject 2 marks: "))
m3 = int(input("Enter subject 3 marks: "))

total = m1 + m2 + m3
percentage = total // 3

if m1 >= 35 and m2 >= 35 and m3 >= 35:
    result = "PASS"
    if percentage >= 75:
        grade = "A"
    elif percentage >= 60:
        grade = "B"
    elif percentage >= 50:
        grade = "C"
    else:
        grade = "D"
else:
    result = "FAIL"
    grade = "No Grade"

print("\nStudent Name:", name)
print("Total Marks:", total)
print("Percentage:", percentage)
print("Result:", result)
print("Grade:", grade)
# w=56.8886868
# e=45.22

# total=w//e


# print("total:", total)