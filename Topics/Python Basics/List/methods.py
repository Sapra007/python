thislist = ["apple", "banana", "cherry"]

thislist.append("orange")

print(thislist)

#add an item to the end of the list using the append() method.



thislist = ["apple", "banana", "cherry"]
thislist.insert(1, "orange")
print(thislist)

#add an item at the specified index using the insert() method.




thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)

#remove an item from the list using the remove() method.




thislist = ["apple", "banana", "cherry"]
thislist.pop()
print(thislist)

#remove the last item of the list using the pop() method.




thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)

#remove all items from the list using the clear() method.





thislist = list(("apple", "banana", "cherry"))
print(thislist)

#create a list using the list() constructor.