import math

def f(a, b, c):
    x = (pow(a, 2) + pow(b, 2) - pow(c, 2)) / (2 * a * b)
    try:
        y = math.acos(x)
        ydeg = (y*180)/math.pi
    except ValueError:
        print("Given sides can not form a triangle.")
    return ydeg

print("Triangles")

sides = list()

for x in range(0, 3):
    while True:
        side = input("Enter side length of a triangle: ")
        try:
            x = float(side)
            if x < 0: raise ValueError("Side must be positive.")
        except ValueError:
            print("Try entering again...")
        else:
            sides.append(x)
            break

a = sides[0]
b = sides[1]
c = sides[2]

if a + b <= c or a + c <= b or b + c <= a:
    print("Given sides can not form a triangle.")
else:
    C = f(a, b, c)
    A = f(b, c, a)
    B = f(c, a, b)

    if (C == A == B):
        print("Triangle is Equilateral Triangle.")
    elif (C == A or C == B or A == B):
        print("Triangle is Isosceles Triangle.")
    else:
        print("Triangle is Scalene Triangle.")

    if (C < 90 and A < 90 and B < 90):
        print("Triangle is Acute Triangle.")
    elif (C == 90 or A == 90 or B == 90):
        print("Triangle is a Right Triangle.")
    elif (C > 90 or A > 90 or B > 90):
        print("Triangle is Obtuse Triangle.")


