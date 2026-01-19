#Check whether an element exists in a tuple
tuple = (1, 2, 3, 4, 5)
element_to_find = 3

if element_to_find in tuple:
    print(f"Element {element_to_find} exists in the tuple.")
    print(f"Index of element {element_to_find}: {tuple.index(element_to_find)}")
else:
    print(f"Element {element_to_find} does not exist in the tuple.")
