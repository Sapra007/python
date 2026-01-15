n = int(input("Enter age: "))

if n < 17:
    print("CHILD")

elif( n >=17 and n < 30):
    print("MATURE")
elif( n >=30 and n <60):
    print("sinior")
elif(n >=60 and n < 100):
    print("super sinior")
else:
    print("invalid number")