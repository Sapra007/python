x = lambda a: a + 10
print(x(5))

#A lambda function is a small anonymous function defined using the lambda keyword.

#Lambda functions can take any number of arguments but can only have one expression.

#They are often used for short, throwaway functions that are not needed elsewhere in the code.




x = lambda a, b: a * b
print(x(5, 6))
#Lambda functions can take multiple arguments, separated by commas.




x = lambda a, b, c: a + b + c
print(x(5, 6, 2))
#Lambda functions can have multiple arguments and perform operations on them.