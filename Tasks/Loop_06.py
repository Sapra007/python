        # factorial of a number

def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result
print(factorial(5)) 


# n = 5
# n =int(input("Enter a number to find factorial :"))
# factorial = 1

# for i in range(1,n + 1):
#     factorial = factorial * i

# print(factorial)   