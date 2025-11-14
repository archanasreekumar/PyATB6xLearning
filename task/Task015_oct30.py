"""
Q - Create a function which will take the 3 values from the user, which are length of the triangle.  side1, side2, side2
i/p - int side1 == side2 =side3 → isoceles
o/p = result in string - iso, eq, scalene
"""

side1 = int(input("Enter side 1: "))
side2 = int(input("Enter side 2: "))
side3 = int(input("Enter side 3: "))

def find_traingle_type(a, b, c):
    if a>0 and b>0 and c>0:
        if a+b>c and a+c>b and b+c>a:
            if a==b==c:
                print("Equilateral triangle")
            elif a==b or a==c or b==c:
                print("Isoceles")
            else:
                print("Scalene")
        else:
            print("Not a triangle")
    else:
        print("Not a valid length")

find_traingle_type(side1, side2, side3)
