    #print all the factors of a number

n =int(input("Enter a number to find its factors :"))

print("factors of", n , "are :")

for i in range(1,n + 1):
    if n % i == 0:
        print(i)