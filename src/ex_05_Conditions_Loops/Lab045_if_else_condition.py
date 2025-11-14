# Problem to find the max between two.

# Logic Building Formula

# 1 . user inputs -> two integers
# 2. o/ p ->  int 1 which ever is grater max number it will return.
# 31.4 or 45.34 - float

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
if num1 >= num2:
    print(f"{num1} is the max")
else:
    print(f"{num2} is the max")