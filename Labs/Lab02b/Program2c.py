# By submitting this assignment, I agree to the following:
#  �Aggies do not lie, cheat, or steal, or tolerate those who do�
#  �I have not given or received any unauthorized aid on this assignment�
#
# Name:         Jonathan Kutsch
# Section:      514
# Assignment:   Lab 2b - Program 2c
# Date:         31 August 2020

x = [(13, 1), (84, 23)]
y = [(13, 3), (84, -5)]
z = [(13, 7), (84, 10)]
# from t=20 to t=50, increment of 7.5 seconds

changeT = 84-13
time1 = 20-13
time2 = 27.5-13
time3 = 35 - 13
time4 = 42.5 - 13
time5 = 50 - 13
positionX_T1 = 1
positionY_T1 = 3
positionZ_T1 = 7
changeX1 = 23-1
changeY1 = -5-3
changeZ1 = 10-7

print("Time: 20 seconds")
x0 = positionX_T1 + (changeX1 / changeT) * time1
print("x0 =", x0, "m")
y0 = positionY_T1 + (changeY1 / changeT) * time1
print("y0 =", y0, "m")
z0 = positionZ_T1 + (changeZ1 / changeT) * time1
print("z0 =", z0, "m")
print(25 * '-')

print("Time: 27.5 seconds")
x0 = positionX_T1 + (changeX1 / changeT) * time2
print("x0 =", x0, "m")
y0 = positionY_T1 + (changeY1 / changeT) * time2
print("y0 =", y0, "m")
z0 = positionZ_T1 + (changeZ1 / changeT) * time2
print("z0 =", z0, "m")
print(25 * '-')

print("Time: 35 seconds")
x0 = positionX_T1 + (changeX1 / changeT) * time3
print("x0 =", x0, "m")
y0 = positionY_T1 + (changeY1 / changeT) * time3
print("y0 =", y0, "m")
z0 = positionZ_T1 + (changeZ1 / changeT) * time3
print("z0 =", z0, "m")
print(25 * '-')

print("Time: 42.5 seconds")
x0 = positionX_T1 + (changeX1 / changeT) * time4
print("x0 =", x0, "m")
y0 = positionY_T1 + (changeY1 / changeT) * time4
print("y0 =", y0, "m")
z0 = positionZ_T1 + (changeZ1 / changeT) * time4
print("z0 =", z0, "m")
print(25 * '-')

print("Time: 50 seconds")
x0 = positionX_T1 + (changeX1 / changeT) * time5
print("x0 =", x0, "m")
y0 = positionY_T1 + (changeY1 / changeT) * time5
print("y0 =", y0, "m")
z0 = positionZ_T1 + (changeZ1 / changeT) * time5
print("z0 =", z0, "m")
print(25 * '-')
