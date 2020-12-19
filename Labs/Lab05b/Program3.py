# By submitting this assignment, I agree to the following:
#  "Aggies do not lie, cheat, or steal, or tolerate those who do"
#  "I have not given or received any unauthorized aid on this assignment"
#
# Name:        Jonathan Kutsch
# Section:     514
# Assignment:  Lab 05b - Program 3
# Date:        18 September 2020

from math import *
import matplotlib.pyplot as plt

y = 0
y1 = 0
x = 202.4
gEarth = 9.8
v0 = float(input("Initial Velocity: "))
theta1 = 0
gMars = 3.711
# assign variables

while abs(1 - y) >= 0.0001:
    # difference between angle and height must be >= tolerance
    theta1 += 0.1
    # angle increases by 0.1 each time through loop
    y = x * tan(radians(theta1)) - ((gEarth * x ** 2) / (2 * v0 ** 2 * cos(radians(theta1)) ** 2))
    # equation inside loop, ensuring angle is in radians
    if y > 1.1:
        # if the angle outputs a height > 1.1, print statement and break loop
        print("Earth: No solution.")
        break
    elif 0.9 <= y <= 1.1:
        print("Earth: Red needs an angle of", theta1, "degrees.")
        print("Earth: Red will hit the wall at a height of", y, "m.")
        break
        # if 0.9 <= height <= 1.1, print angle and height and break loop
    elif abs(90 - theta1) <= 0.1:
        print("Earth: No solution.")
        break
    # if the angle goes beyond 90 degrees, then print No solution and break loop
    # this avoids an infinite loop

theta2 = 0
# need to reassign theta for mars equation

# repeat with Mars gravity
while abs(1 - y1) >= 0.0001:
    theta2 += 0.1
    y1 = x * tan(radians(theta2)) - ((gMars * x ** 2) / (2 * v0 ** 2 * cos(radians(theta2)) ** 2))
    if y1 > 1.1:
        print("Mars: No solution.")
        break
    elif 0.9 <= y1 <= 1.1:
        print("Mars: Red needs an angle of", theta2, "degrees.")
        print("Mars: Red will hit the wall at a height of", y1, "m.")
        break
    elif abs(90 - theta2) <= 0.1:
        break

if 0.9 <= y <= 1.1:
    plt.plot(theta1, x * tan(radians(theta1)) - ((gEarth * x ** 2) / (2 * v0 ** 2 * cos(radians(theta1)) ** 2)), '-o')
    plt.title("Earth graph")
    plt.xlabel("Degrees")
    plt.ylabel("Height (m)")
    plt.show()
if 0.9 <= y1 <= 1.1:
    plt.plot(theta2, x * tan(radians(theta2)) - ((gMars * x ** 2) / (2 * v0 ** 2 * cos(radians(theta2)) ** 2)), '-o')
    plt.title("Mars graph")
    plt.xlabel("Degrees")
    plt.ylabel("Height (m)")
    plt.show()
    # plot point on graph if solution is valid
    # if no solution is outputted, then no graph will be displayed
