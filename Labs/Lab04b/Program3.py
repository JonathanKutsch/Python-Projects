# By submitting this assignment, I agree to the following:
#  �Aggies do not lie, cheat, or steal, or tolerate those who do�
#  �I have not given or received any unauthorized aid on this assignment�
#
# Name:         Jonathan Kutsch
# Section:      514
# Assignment:   Lab 04b - Program 3
# Date:         12 September 2020

import math
import cmath

print("Quadratic Equation: (a * x^2) + (b * x) + c")
a = float(input("Enter first coefficient: "))
b = float(input("Enter second coefficient: "))
c = float(input("Enter third coefficient: "))

discriminant = (b ** 2) - (4 * a * c)

if discriminant > 0:
    print("Real and Different Roots")
    root1 = ((-b + math.sqrt(discriminant)) / (2 * a))
    root2 = ((-b - math.sqrt(discriminant)) / (2 * a))
    print(root1)
    print(root2)
elif discriminant == 0:
    print("Real and Same Roots")
    root = -b / (2 * a)
    print(root)
else:
    print("Complex Roots")
    print(-b / (2*a), "\b+i", cmath.sqrt(discriminant))
    print(-b / (2*a), "\b-i", cmath.sqrt(discriminant))
