
#count strings ,letter or symbols in given strings


# str1 = "P@#yn26at^&i5ve"

# letter = 0
# digit = 0
# symbol = 0

# for ch in str1:
#     if ch.isalpha():
#         letter += 1
#     elif ch.isdigit():
#         digit += 1
#     else:
#         symbol += 1

# print("char =",letter)
# print("digit =",digit)
# print("symbol =",symbol)




str1 = "P@#yn26at^&i5ve"

letters = 0
digit = 0
symbols = 0

for ch in str1:

    if ('A' <= ch <= 'Z') or ('a' <= ch <= 'z'):
        letters += 1

    elif '0' <= ch <= '9':
        digit += 1

else:
    symbols += 1

print("Char = ",letters)
print("Digit = ",digit)
print("symbol =",symbols)






















