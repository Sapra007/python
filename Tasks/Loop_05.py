   #Sum up to n terms

n =int(input("Enter a nnumber to sum up to n terms :"))

sum = 0

for i in range(1, n+1):
    sum += i
    print(sum)
