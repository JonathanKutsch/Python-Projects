# By submitting this assignment, I agree to the following:
#  “Aggies do not lie, cheat, or steal, or tolerate those who do”
#  “I have not given or received any unauthorized aid on this assignment”
#
# Name:           Jonathan Kutsch
# Section:        514
# Assignment:     Quiz 4 - Loops
# Date:           30 September 2020

day = 0
night = 0
measurement = int(input("Enter measurement: "))
while -5000000 < measurement < 5000000:
    # set exaggerated bounds
    if measurement < 50:
        day += measurement
        print("Day: ", day)
    if measurement < 0:
        break
    if measurement > 100:
        print("Invalid input.")
        continue
    measurement = int(input("Enter measurement: "))
    if measurement >= 50:
        night += measurement
        print("Night: ", night)
    elif measurement < 0:
        break
    elif measurement > 100:
        print("Invalid input.")
        continue
# submitting twice because text box was not available to submit code on first attempt
