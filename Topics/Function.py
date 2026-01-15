

# # Function is a Block of statement that perform a specific task.

# def number(a, b): # parameter
#     sum = a + b 
#     print(sum)
#     return sum


# number(10,20)
# # number(50,20)

#                     # different way

# def cal(a,b):   # parameter
#     return a + b

# sum = cal(10,20)  # function call; arguments

# print(sum)


# def cal_sum (a,b):
#     return a + b
# sum = cal_sum(1,2)
# print(sum)



    # avarage of 3 numbers 
# def cal_avg(a,b,c):
#     sum = a + b + c
#     avg = sum/3
#     print(avg)
#     return avg
# cal_avg(98, 97, 95)

# cities = ["delhi", "gurgaon", "noida","pune","mumbai","chennai"]
# heroes = ["thor","ironman","captain_amarika","hulk"]
# def print_len(list):
#     print(len(list))

# print_len(cities)
# print_len(heroes)



    
    
        #practice question :

        # Basic Functin Syntex
# 1.wrete a function to calculate and return the square of a number.

# def square(number):
#     return number ** 2

# result = square(4)
# print(result)

        # Function with Multiple Parameters
# 2.create a function that takes two numbers as parameters and returns their sum.

# def add(num1, num2):
#     return num1 + num2

# print(add(5, 5))

        # Polymorphism in Function
#3. write a function multiply that multiplies two numbers, but can also 
# accept and multiple strings. 

# def multiply(p1,p2):
#     return p1 * p2

# print(multiply(8, 5))
# print(multiply('a', 5))
# print(multiply(10,'a'))

        # Function Returning Multiple Values
# 4. Create a function thatreturns both the area and cirumference of a circle 
# given its radius.

# import math
# def circle_stats(radius):
#     area = math.pi * radius ** 2
#     circumference = 2 *math.pi * radius
#     return area , circumference
# a,c = circle_stats(3)

# print("Area: ",a, "\n""Circumference",c)

        #Default Parameter value
# 5. Write a function that greets a user. if ni name is provided, 
# it should greet with a default name.

# def greet(name = "User"):
#     return "Hello," + name + "!" 

# print(greet("chai"))

        # Lamda Function
# 6. create a lamda function to compute the cube of number.

# cube = lambda x: x ** 3

# print(cube(3))


  # Function with *args
# 7. Write a  function that takes variable number of arguments
#    and returns their sum.

# def sum_all(*args):
#     return sum(args)

# print(sum_all(1, 2, 3))

# print(sum_all(1, 2, 3, 4, 5))

# print(sum_all(1, 2, 3, 4, 5, 6, 7))


        #Function with **kwargs
# 8. Create a function that accept any number of keyword arguments 
#    and prints them in the format key:value.


def print_kwargs(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}:{value}")

print_kwargs(name = "iron man", power = "lazer")  

print_kwargs(name = "iron man",

enemy = "Dr. jakaal")







