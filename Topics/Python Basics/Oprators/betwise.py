#bitwise oprators

x = 5  # In binary: 0101
y = 3  # In binary: 0011

print(x & y)  # Bitwise AND: 0101 & 0011 = 0001 -> 1
print(x | y)  # Bitwise OR:  0101 | 0011 = 0111 -> 7
print(x ^ y)  # Bitwise XOR: 0101 ^ 0011 = 0110 -> 6
print(~x)     # Bitwise NOT: ~0101 = 1010 -> -6
print(x << 1) # Bitwise Left Shift: 0101 << 1 = 1010 -> 10
print(x >> 1) # Bitwise Right Shift: 0101 >> 1 = 0010 -> 2


#This code demonstrates bitwise operators in Python:
#AND (&), OR (|), XOR (^), NOT (~), Left Shift (<<), and Right Shift (>>).