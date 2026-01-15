cel = int(input("enter temperature in celcious:"))

if cel <= 0:
    print("Freezing cold")
elif cel >= 0 and cel < 10:
    print("very cold")
elif cel >= 10 and cel < 20:
    print("cold")
elif cel >= 20 and cel < 30:
    print("Pleasent")
elif cel >= 30 and cel < 40:
    print("Hot")
elif cel >= 40:
    print("Extremely hot")
else:
    print("Very hot")