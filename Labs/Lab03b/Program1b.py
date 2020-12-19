# By submitting this assignment, I agree to the following:
#  �Aggies do not lie, cheat, or steal, or tolerate those who do�
#  �I have not given or received any unauthorized aid on this assignment�
#
# Name:         Jonathan Kutsch
# Section:      514
# Assignment:   Lab 3b - Program 1b
# Date:         05 September 2020

fluid_velocity = float(input('The fluid velocity is: '))
linear_dimension = float(input('The linear dimension is: '))
viscosity = float(input('The viscosity is: '))
reynolds_number = fluid_velocity * linear_dimension / viscosity
print('Reynolds Number =', reynolds_number)
# Reynold's Number formula: velocity of fluid * linear dimension / viscosity