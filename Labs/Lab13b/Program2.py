# By submitting this assignment, I agree to the following:
#  Aggies do not lie, cheat, or steal, or tolerate those who do
#  I have not given or received any unauthorized aid on this assignment
#
# Name:         Jonathan Kutsch
# Section:      514
# Assignment:   Lab 13b - Program 2
# Date:         15 November 2020

import matplotlib.pyplot as plt
import numpy as np
# import necessary libraries

point = np.array([[1, 0]])
# define starting point in a 1x2 matrix (x,y)

M = np.array([[1.00583, -0.087156],
              [0.087156, 1.00583]])
# define the 2x2 matrix

v = point.transpose()
# make new variable to transpose point into 2x1 because 2x2 doesn't align with 1x2

x = []
y = []
# create empty list to store data that is collected through loop

for i in range(0, 200):
    new_point = np.dot(M, v)
    x = np.append(x, new_point[0][0])
    y = np.append(y, new_point[1][0])
    v = new_point
    # loop between 150 and 250 times
    # compute product of M and v and
    # append first element to x list and second element to y list

plt.plot(x, y)
plt.title("Lab 13b - Program 2")
plt.show()
# plot the data
