
# Create a tuple of squares of numbers using a loop
squares_list = []
for i in range(1, 6):
    squares_list.append(i**2)
squares = tuple(squares_list)
print(squares)
print(type(squares))