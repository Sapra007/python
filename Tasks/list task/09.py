#Replace all negative numbers with 0
num = [10, -1, 2, -3, 4, -5, 6, -7, 8, -9]

for i in range(len(num)):
    if num[i] < 0:
        num[i] = 0
print(num)