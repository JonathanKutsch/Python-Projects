# By submitting this assignment, I agree to the following:
#  �Aggies do not lie, cheat, or steal, or tolerate those who do�
#  �I have not given or received any unauthorized aid on this assignment�
#
# Name:         Jonathan Kutsch
# Section:      514
# Assignment:   Lab 04b - Program 1
# Date:         12 September 2020

# Read in person's height and weight
# Report if person is underweight, healthy, overweight, or obese

height = float(input("Enter your height in inches: "))
weight = float(input("Enter your weight in pounds: "))
BMI = (703 * weight / height **2)

print("\nYou're Body Mass Index is", BMI)

if BMI < 18.5:
    print("This means that you are Underweight.")
elif 18.5 <= BMI <= 24.9:
    print("This means that you are Healthy.")
elif 25.0 <= BMI <= 29.9:
    print("This means that you are Overweight.")
elif BMI >= 30.0:
    print("This means that you are Obese.")

# I noticed an issue with the model provided:
# If you enter 150 inches and 123.5 lbs, it outputs 24.9494 BMI
# This puts it right in between 24.9 and 25.0, so there is no Weight Status provided


