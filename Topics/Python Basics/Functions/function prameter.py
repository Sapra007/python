def my_function(fname):
  print(fname + " Refsnes")

my_function("Emil")
my_function("Tobias")
my_function("Linus")

#A function parameter is a variable that is used to pass information into a function.
# In this example, the function my_function() has one parameter, fname.




def my_function(country = "Norway"):
  print("I am from " + country)

my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil")

#Default parameter value is used when no argument is provided during the function call.
# In this example, the function my_function() has one parameter, country, with a default value of "Norway".