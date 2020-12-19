# By submitting this assignment, I agree to the following:
#  �Aggies do not lie, cheat, or steal, or tolerate those who do�
#  �I have not given or received any unauthorized aid on this assignment�
#
# Name:         Jonathan Kutsch
# Section:      514
# Assignment:   Lab 3b - Program 1a
# Date:         05 September 2020

mass = float(input('The mass being calculated is: '))
velocity = float(input('The velocity being calculated is: '))
velocity_squared = velocity ** 2
kinetic_energy = 1/2 * mass * velocity_squared
print('Kinetic Energy =', kinetic_energy)
# kinetic energy formula: KE = mass * velocity^2