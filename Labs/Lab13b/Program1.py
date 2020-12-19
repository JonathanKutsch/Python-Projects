# By submitting this assignment, I agree to the following:
#  Aggies do not lie, cheat, or steal, or tolerate those who do
#  I have not given or received any unauthorized aid on this assignment
#
# Name:         Jonathan Kutsch
# Section:      514
# Assignment:   Lab 13b - Program 1
# Date:         15 November 2020

import numpy as np
from operator import itemgetter
# import necessary libraries

# month = [3" pipe, 4" pipe, 3" valve, 4" valve, pump]
pipeline_req = np.array([[200, 975, 3, 2, 1],
                        [225, 850, 8, 2, 1],
                        [250, 850, 3, 3, 1],
                        [100, 850, 3, 3, 2],
                        [0, 500, 0, 5, 0],
                        [0, 500, 0, 5, 1],
                        [150, 595, 5, 8, 1],
                        [175, 675, 20, 8, 3],
                        [250, 1080, 9, 10, 1],
                        [250, 800, 8, 10, 1],
                        [800, 850, 0, 12, 2],
                        [0, 725, 50, 12, 0]])

# [shop A, shop B, shop C]
cost = np.array([[0.14, 0.09, 0.10],
                [0.22, 0.21, 0.22],
                [5.50, 5.75, 5.65],
                [8.95, 8.94, 7.00],
                [185, 195, 205]])

result = np.dot(pipeline_req, cost)
# compute product of pipeline requirements and cost

shopA = list(map(itemgetter(0), result))
shopB = list(map(itemgetter(1), result))
shopC = list(map(itemgetter(2), result))
# divide data set into three columns using itemgetter function

print("Shop A: ", sum(shopA))
print("Shop B: ", sum(shopB))
print("Shop C: ", sum(shopC))
# display the sum of all costs to reveal cheapest

print("\nShop B will be the least expensive\nwith a total cost of $6230.45")
