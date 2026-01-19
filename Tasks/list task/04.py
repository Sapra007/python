#Reverse a list without using reverse()

list = ["a","b","c","d","e"]

reversed_list = []
for item in list:
    reversed_list = [item] + reversed_list
print(reversed_list)