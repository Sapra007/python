#Write a program to do arithmetic operations addition and division
#addition
num1 = float(input("enter the first number: "))
num2 = float(input("enter the second number: "))
sum_result = num1 + num2
print(f"sum: {num1} + {num2} = {sum_result}")



#divison
num3 = float(input("enter the divident for divison: "))
num4 = float(input("enter the divisor for divison: "))
if num4 == 0:
    print("Error: Division by zero is not allowed.")
else:
    div_result = num3 / num4
    print(f"Divison: {num3} / {num4} = {div_result}")





