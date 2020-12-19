# By submitting this assignment, I agree to the following:
#  Aggies do not lie, cheat, or steal, or tolerate those who do
#  I have not given or received any unauthorized aid on this assignment
#
# Name:         Jonathan Kutsch
# Section:      514
# Assignment:   Lab 10b - Program 1
# Date:         23 October 2020

values = []
# create empty list to store converted values
with open("Celsius.dat", 'r') as Celsius:
    tempC = Celsius.readlines()
    # reads all lines that we will be working with
    for line in tempC:
        if line != '\n':
            line = int(line)
            result = line * (9/5) + 32
            # iterate through every line, convert to int
            # use equation to convert to Fahrenheit
            values.append(float(round(result)))
            # append all values to list to extract later

degrees_F = '\n'.join(map(str, values))
# convert all integers in list to a string using map function
with open("Fahrenheit.dat", 'w') as Fahrenheit:
    Fahrenheit.write(degrees_F)
    # writes all converted values into new file
