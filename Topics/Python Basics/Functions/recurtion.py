def tri_recursion(k):
  if(k > 0):
    result = k + tri_recursion(k - 1)
    print(result)
  else:
    result = 0
  return result

print("Recursion Example Results:")
tri_recursion(6)

#A recursive function is a function that calls itself in order to solve a problem.


#This technique is known as recursion and is commonly used to solve 
# problems that can be broken down into smaller, similar subproblems.


#In the example above, the function tri_recursion calls itself with a decremented 
# value of k until it reaches the base case of k being 0.   
