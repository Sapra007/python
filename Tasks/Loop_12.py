text = input("Enter string :")

reverse = ""

for ch in text:
    reverse = ch + reverse

if text == reverse:
    print(text,"is palindrom")
else:
    print(text,"is Not a Palindrome")