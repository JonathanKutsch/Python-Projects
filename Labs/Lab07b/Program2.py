# By submitting this assignment, I agree to the following:
#  "Aggies do not lie, cheat, or steal, or tolerate those who do"
#  "I have not given or received any unauthorized aid on this assignment"
#
# Name:        Jonathan Kutsch
# Section:     514
# Assignment:  Lab 07b - Program 2
# Date:        02 October 2020

margin = 1000
# allows the loop to continue until manual termination with 'stop' user input

word = str(input("Enter word or 'stop' to exit: "))
for i in range(margin):
    if word == 'stop':
        exit()
    if word[0] in ['a', 'e', 'i', 'o', 'u']:
        print(word + 'yay')
        word = str(input("Enter word or 'stop' to exit: "))
    # if first letter of word starts with vowel, add 'yay' at end and repeat
    if word[0] not in ['a', 'e', 'i', 'o', 'u']:
        print(word[1:] + word[0] + 'ay')
        word = str(input("Enter word or 'stop' to exit: "))
    # if first letter of word starts with consonant, move the it to back, add 'ay' and repeat
