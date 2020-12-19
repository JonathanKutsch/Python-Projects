# By submitting this assignment, I agree to the following:
#  "Aggies do not lie, cheat, or steal, or tolerate those who do"
#  "I have not given or received any unauthorized aid on this assignment"
#
# Name:        Jonathan Kutsch
# Section:     514
# Assignment:  Lab 06b - Program 1
# Date:        25 September 2020

from statistics import *

measurements = [15.80, 19.60, 21.85, 33.61, 49.73, 51.27, 56.26, 63.06, 76.56, 76.57, 85.78, 90.74, 92.60, 99.71,
                100.51, 101.12, 101.25, 102.19, 104.85, 110.59, 125.92, 131.25, 136.04, 141.15, 148.54, 150.02]

measurements.append(162.76)
measurements.insert(8, 71.01)
print(('There were {} days of data measurements taken.'.format(len(measurements))))
print('-' * 50)

week1 = measurements[0:7]
print('Average moss mass in week 1 is:'.ljust(0), '{} g'.rjust(6).format(round(mean(week1), 2)))

week2 = measurements[7:14]
print('Average moss mass in week 2 is:'.ljust(0), '{} g'.rjust(6).format(round(mean(week2), 2)))

week3 = measurements[14:21]
print('Average moss mass in week 3 is:'.ljust(0), '{} g'.rjust(5).format(round(mean(week3), 2)))

week4 = measurements[21:28]
print('Average moss mass in week 4 is:'.ljust(0), '{} g'.rjust(5).format(round(mean(week4), 2)))
