# By submitting this assignment, I agree to the following:
#  Aggies do not lie, cheat, or steal, or tolerate those who do
#  I have not given or received any unauthorized aid on this assignment
#
# Name:         Jonathan Kutsch
# Section:      514
# Assignment:   Lab 11b - Program 3
# Date:         1 November 2020

def is_perfect():
    sum1 = 0
    # preset the sum to zero

    for i in range(1, num):
        if num % i == 0:
            sum1 += i
        # iterate through every integer to num and if num divisible to 0, then add to sum
    if sum1 == num:
        return True
    # if the end sum equals the num, return True
    else:
        return False
    # if not, then return False


num = int(input("Enter number greater than 1: "))
print(is_perfect())

