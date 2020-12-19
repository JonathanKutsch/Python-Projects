# By submitting this assignment, I agree to the following:
#  “Aggies do not lie, cheat, or steal, or tolerate those who do”
#  “I have not given or received any unauthorized aid on this assignment”
#
# Name:           Jonathan Kutsch
# Section:        514
# Assignment:     Quiz 3 - Conditionals & Booleans
# Date:           30 September 2020

name = input("Enter username: ")
win = int(input("Number of moonbeams won: "))
hit = int(input("Number of asteroid hits suffered: "))

star_points = ((win ** 2) - hit) / 102.4

if star_points < 1000:
    print("Howdy", name, "you have", star_points, "Star Points, which makes you a Space Cadet!")
elif 1000 <= star_points <= 100000:
    print("Howdy", name, "you have", star_points, "Star Points, which makes you a Celestial Captain!")
elif star_points > 100000:
    print("Howdy", name, "you have", star_points, "Star Points, which makes you an Interstellar Chuck Norris!")

