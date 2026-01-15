    #Check wether the number is prime or not

num = int(input("Enter a number :"))

if num <= 1:
    print(num,"is Not a Prime number")
else:
    count = 0

    for i in range(1, num +1):

        if num % i == 0:
         count = count + 1
if count == 2:
    print(num,"is a Prime number")
else:
    print(num,"is Not a Prime number")
