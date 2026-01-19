#Remove duplicate elements from a list
my_list = [1, 2, 2, 3, 4, 4, 5, 5, 5]

new = []

for i in my_list:
    if i not in new:
        new.append(i)
print(new)