# By submitting this assignment, I agree to the following:
#  �Aggies do not lie, cheat, or steal, or tolerate those who do�
#  �I have not given or received any unauthorized aid on this assignment�
#
# Name:         Jonathan Kutsch
# Section:      514
# Assignment:   Lab 04b - Program 2
# Date:         12 September 2020

# take input of fluid velocity, kinematic viscosity, and linear dimension
# compute Reynold's number
# Report whether flow is laminar, transient, or turbulent

fluid_velocity = float(input("The fluid velocity is: "))
linear_dimension = float(input("The linear dimension is: "))
viscosity = float(input("The viscosity is: "))
reynolds_number = fluid_velocity * linear_dimension / viscosity

# Reynold's Number: velocity of fluid * linear dimension / viscosity

print('\nReynolds Number =', reynolds_number)

if reynolds_number < 2300:
    print("Laminar Flow")
elif 2300 <= reynolds_number < 4000:
    print("Transient Flow")
elif reynolds_number >= 4000:
    print("Turbulent Flow")

# Source: www.engineeringtoolbox.com/reynolds-number-d_237.html
