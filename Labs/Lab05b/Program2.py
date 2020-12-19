# By submitting this assignment, I agree to the following:
#  "Aggies do not lie, cheat, or steal, or tolerate those who do"
#  "I have not given or received any unauthorized aid on this assignment"
#
# Name:        Jonathan Kutsch
# Section:     514
# Assignment:  Lab 05b - Program 2
# Date:        18 September 2020

for i in range(2, 101):
    # outer loop that goes through all numbers in range, not including 101
    for j in range(2, i+1):
        # sets the second number j, but ensuring it doesn't go over number i
        if i % j == 0:
            # check to make sure i divides by j evenly
            print(j, "divides", i)
            # all numbers that are only divided by itself is prime
