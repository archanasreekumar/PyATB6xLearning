# Problem  Find the Max between 3 numbers

# Logic Building

# User inputs - num1, num2, num3 -> int
# O/p -> int or String with max number .

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
num3 = float(input("Enter third number: "))

if num1 > num2 and num1 > num3:
    print(f"{num1}")
elif num2 > num1 and num2 > num3:
    print(f"{num2}")
else:
    print(f"{num3}")