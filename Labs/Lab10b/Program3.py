# By submitting this assignment, I agree to the following:
#  Aggies do not lie, cheat, or steal, or tolerate those who do
#  I have not given or received any unauthorized aid on this assignment
#
# Name:         Jonathan Kutsch
# Section:      514
# Assignment:   Lab 10b - Program 3
# Date:         26 October 2020

import csv
import matplotlib.pyplot as plt

x = []
y = []

with open("Portfolio.csv", 'r') as Portfolio:
    reader = csv.reader(Portfolio, delimiter=',')
    for row in reader:
        x.append(row[0])
        y.append(row[1])
    # append each row of data to array to plot on proper axis

x = x[1:]
y = y[1:]
# take titles out of plot

plt.plot(x, y, marker='o', linestyle="None")
# plot values, mark each point with dot, and remove line as seen in example
plt.xlabel('Month')
plt.ylabel('Principal Balance')
plt.title('Amortization Schedule')
# label all proper axis
plt.gca().invert_yaxis()
# invert to correlate x and y values
plt.tight_layout()
plt.show()
# make the layout look nice and present it when code is run
