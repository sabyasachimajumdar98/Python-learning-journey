temp=int(input("Enter the Temperature: "))
if temp>=-5 and temp<=5:
    print("Very Cold")
elif temp>=6 and temp<=18:
    print("Cold")
elif temp>=18 and temp<=30:
    print("Hot")
else:
    print("Cannot read the tempareture!!")

