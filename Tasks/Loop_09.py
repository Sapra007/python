    #accept a number and check if numbe ris perfct or not.
    #a number whose sum of factors is eual to the number itself is called perfect number.

num = int(input("Enter a number to check if it is perfect number or not :"))

sum = 0

for i in range(1, num):
    if num % i == 0:
        sum += i
if sum == num :
    print(num,"is a Perfect number")

else:
    print(num,"is Not a Perfect number")