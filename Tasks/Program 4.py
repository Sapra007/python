#input two variables
a = int(input("enter the value of a: "))
b = int(input("enter the value of b: "))

print(f"original values: a = {a}, b = {b}")

#swap the value using a temporary variable
temp = a
a = b
b = temp

print(f"swapped values: a = {a}, b = {b}")