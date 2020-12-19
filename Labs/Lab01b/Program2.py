# By submitting this assignment, I agree to the following:
#  �Aggies do not lie, cheat, or steal, or tolerate those who do�
#  �I have not given or received any unauthorized aid on this assignment�
#
# Name:         Jonathan Kutsch
# Section:      514
# Assignment:   Lab 1b-2
# Date:         22 August 2020

from math import sin
from math import cos

print("This shows the function (12 * x) / (x - 5) evaluated close to x = 2")
print(12 * 2.1 / (2.1 - 5))
print(12 * 2.01 / (2.01 - 5))
print(12 * 2.001 / (2.001 - 5))
print(12 * 2.0001 / (2.0001 - 5))
print(12 * 2.00001 / (2.00001 - 5))
print(12 * 2.000001 / (2.000001 - 5))
print(12 * 2.0000001 / (2.0000001 - 5))
print(12 * 2.00000001 / (2.00000001 - 5))
# this function gives an evaluation that gets closer and closer to -8

# Function 1:
print("\n")
print("This shows the function f(X) = sin x / x evaluating between the range 1 to 10**-7")
print(sin(1) / 1)
print(sin(0.1) / 0.1)
print(sin(0.01) / 0.01)
print(sin(0.001) / 0.001)
print(sin(0.0001) / 0.0001)
print(sin(0.00001) / 0.00001)
print(sin(0.000001) / 0.000001)
print(sin(0.0000001) / 0.0000001)
# this function gives an evaluation that gets closer and closer to 1.0 as you approach x = 10**-7

# Function 2:
print("\n")
print("This shows the function g(X) = 1 - cos x / x**2 evaluating between the range 1 to 10**-7")
print((1 - cos(1)) / 1**2)
print((1 - cos(0.1)) / 0.1**2)
print((1 - cos(0.01)) / 0.01**2)
print((1 - cos(0.001)) / 0.001**2)
print((1 - cos(0.0001)) / 0.0001**2)
print((1 - cos(0.00001)) / 0.00001**2)
print((1 - cos(0.000001)) / 0.000001**2)
print((1 - cos(0.0000001)) / 0.0000001**2)
# this function is similar to Function 1 above

# Function 3:
print("\n")
print("This shows the function h(X) = (1 + 1/x)**x evaluating between the range 1 to 10**7")
print((1 + 1/1)**1)
print((1+1/10)**10)
print((1+1/100)**100)
print((1+1/1000)**1000)
print((1+1/10000)**10000)
print((1+1/100000)**100000)
print((1+1/1000000)**1000000)
print((1+1/10000000)**10000000)
