# By submitting this assignment, I agree to the following:
#  Aggies do not lie, cheat, or steal, or tolerate those who do
#  I have not given or received any unauthorized aid on this assignment
#
# Name:         Jonathan Kutsch
# Section:      514
# Assignment:   Quiz 9 - Defining Functions
# Date:         21 November 2020

def even_or_odd():
    if n % 2 == 0:
        print("even")
    elif n == 0:
        print("neither even or odd")
    else:
        print("odd")
# test if integer is even, odd, or even


def pos_or_neg():
    if n > 0:
        print("positive")
    elif n == 0:
        print("neither positive or negative")
    else:
        print("negative")
# test if integer is positive, negative, or neither


def integer_info():
    print("Here is information about your integer!")
    even_or_odd()
    pos_or_neg()
# print what the user is gaining from program
# utilize the two functions


n = int(input("Enter integer: "))
# request user input of integer to test

integer_info()
# run main function
