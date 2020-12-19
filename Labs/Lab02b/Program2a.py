# By submitting this assignment, I agree to the following:
#  �Aggies do not lie, cheat, or steal, or tolerate those who do�
#  �I have not given or received any unauthorized aid on this assignment�
#
# Name:         Jonathan Kutsch
# Section:      514
# Assignment:   Lab 2b - Program 2a
# Date:         31 August 2020

# data = [(t1, var1), (t2, var2)] -- var representing x,y,z
x = [(13, 1), (84, 23)]
y = [(13, 3), (84, -5)]
z = [(13, 7), (84, 10)]

print("Time: 50 seconds")

x0 = 1 + ((23-1) / (84-13)) * (50-13)
print("x0 =", x0, "m")

y0 = 3 + ((-5-3) / (84-13) * (50-13))
print("y0 =", y0, "m")

z0 = 7 + ((10-7) / (84-13) * (50-13))
print("z0 =", z0, "m")

# equation: var1 + ((var2 - var1) / (t2 - t1) * (t - t1)