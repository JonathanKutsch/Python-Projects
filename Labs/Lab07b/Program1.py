# By submitting this assignment, I agree to the following:
#  "Aggies do not lie, cheat, or steal, or tolerate those who do"
#  "I have not given or received any unauthorized aid on this assignment"
#
# Name:        Jonathan Kutsch
# Section:     514
# Assignment:  Lab 07b - Program 1
# Date:        01 October 2020

list1 = [[1, 2], [2, 5], [3, 2]]
# list given

for i in list1:
    if sum(list1[0]) > (sum(list1[1]) or sum(list1[2])):
        print(list1[0], "with a sum of", sum(list1[0]))
        break
    # if first set of elements in list is greatest, add them and break
    elif sum(list1[1]) > (sum(list1[0]) or sum(list1[2])):
        print(list1[1], "with a sum of", sum(list1[1]))
        break
    # if second set of elements in list is greatest, add them and break
    elif sum(list1[2]) > (sum(list1[0]) or sum(list1[1])):
        print(list1[2], "with a sum of", sum(list1[2]))
        break
    # if third set of elements in list is greatest, add them and break
