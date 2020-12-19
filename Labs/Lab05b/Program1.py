# By submitting this assignment, I agree to the following:
#  "Aggies do not lie, cheat, or steal, or tolerate those who do"
#  "I have not given or received any unauthorized aid on this assignment"
#
# Name:        Jonathan Kutsch
# Section:     514
# Assignment:  Lab 05b - Program 1
# Date:        18 September 2020

theSum = 0
count = 0
max_num = None
min_num = None
# set variables

while True:
    num = int(input("Enter number: "))
    count += 1
    # add one to count each time input is received -- needed to find average
    theSum += num
    if max_num is None:
        max_num = num
    elif max_num < num:
        max_num = num
    # if the largest number < number inputted, then replace it
    if min_num is None:
        min_num = num
    elif num < min_num:
        min_num = num
    # if the smallest number > number inputted, then replace it
    if num < 0:
        break
    # program terminates when negative number is inputted
    print("The largest number is", max_num)
    print("The smallest number is", min_num)
    print("The average is", theSum / count)
# program continuously outputs data as it is being collected
