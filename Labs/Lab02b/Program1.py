# By submitting this assignment, I agree to the following:
#  �Aggies do not lie, cheat, or steal, or tolerate those who do�
#  �I have not given or received any unauthorized aid on this assignment�
#
# Name:         Jonathan Kutsch
# Section:      514
# Assignment:   Lab 2b - Program 1
# Date:         31 August 2020

# note from directions: print statements should print just a single variable

from math import tan
from numpy import pi

name = "Jonathan Kutsch "
UIN = "830002561"
a = name + UIN
print(a)

fun_fact = "I have {} brothers that also went to {}.".format(2, "Texas A&M")
print(fun_fact)

current = 5
resistance = 20
voltage = current * resistance
print(voltage)
# multiplication using Ohm's Law: Voltage = Current * Resistance

mass = 100
velocity = 21
velocity_squared = velocity ** 2
kinetic_energy = 1/2 * mass * velocity_squared
print(kinetic_energy)
# kinetic energy formula: KE = mass * velocity^2

fluid_velocity = 100
linear_dimension = 2.5
viscosity = 1.2
reynolds_number = fluid_velocity * linear_dimension / viscosity
print(reynolds_number)
# Reynold's Number formula: velocity of fluid * linear dimension / viscosity

stefan_constant = 5.67 * 10**-8
temp = 2200
stefan_boltzmann = stefan_constant * temp ** 4
print(stefan_boltzmann)
# Stefan-Boltzmann Law formula: Stefan's constant * Temperature^4

normal_stress = 20
cohesion = 2
angle_degrees = 35
angle_radians = tan(angle_degrees * pi / 180)
shear_stress = normal_stress * angle_radians + cohesion
print(shear_stress)
# Shear Stress: Normal stress * tan(angle in radians) + cohesion
