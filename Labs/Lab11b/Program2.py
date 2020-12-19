# By submitting this assignment, I agree to the following:
#  Aggies do not lie, cheat, or steal, or tolerate those who do
#  I have not given or received any unauthorized aid on this assignment
#
# Name:         Jonathan Kutsch
# Section:      514
# Assignment:   Lab 11b - Program 2
# Date:         1 November 2020

def label_me():

    name = input("What is your name? ")
    city = input("What city do you live in? ")
    state = input("What state do you live in? ")
    zip_code = input("What is the zip code? ")
    address = input("What is your address? (enter comma for two lines) ")

    if '\n' not in address:
        print('', name, '\n', address, '\n', city, state, zip_code)
    # if the address is single line, print this
    two_line = []
    if ',' in address:
        two_line = str(address).split(',')
        print('', name, '\n', two_line[0], '\n', two_line[1], '\n', city, state, zip_code)
    # if the address is two lines, assign parts to list and print on separate lines


label_me()
