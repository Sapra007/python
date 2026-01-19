#Count frequency of characters in a string
# string = "hello world"
# freq = {}   
# for char in string:
#     if char in freq:
#         freq[char] += 1
#     else:
#         freq[char] = 1
# print(freq)

s = "hello world"
freq = {}

for ch in s:
    freq[ch] = freq.get(ch, 0) + 1

print(freq)
