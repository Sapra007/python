thisset = {"apple", "banana", "cherry"}

thisset.remove("banana")

print(thisset)

#remove an item from a set using the remove() method.




thisset = {"apple", "banana", "cherry"}

thisset.discard("banana")

print(thisset)
#remove an item from a set using the discard() method.




thisset = {"apple", "banana", "cherry"}

x = thisset.pop()

print(x) 

print(thisset) 
#remove a random item from a set using the pop() method.


thisset = {"apple", "banana", "cherry"}

thisset.clear()

print(thisset)
#remove all items from a set using the clear() method.





thisset = {"apple", "banana", "cherry"}

del thisset

print(thisset) #this will raise an error because the set no longer exists
#delete a set using the del keyword.






thisset = set(("apple", "banana", "cherry"))
print(thisset)
# Note: the set list is unordered, so the result will display the items in a random order.
# create set using the set() constructor.