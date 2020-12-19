# By submitting this assignment, I agree to the following:
#  “Aggies do not lie, cheat, or steal, or tolerate those who do”
#  “I have not given or received any unauthorized aid on this assignment”
#
# Name:           Jonathan Kutsch
# Section:        514
# Assignment:     Quiz 2 - Input, Variables, and Output
# Date:           27 September 2020

name = input("What is your name? ")
cookies = float(input("How many pounds of maroon cookies do you want? "))

total = (12.25 * cookies) + (1.23 * cookies) + 2.25
print("Howdy", name, "thank you for your purchase!\nThe total is", "$" + str(total))
