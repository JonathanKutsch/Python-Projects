# By submitting this assignment, I agree to the following:
#  �Aggies do not lie, cheat, or steal, or tolerate those who do�
#  �I have not given or received any unauthorized aid on this assignment�
#
# Name:         Jonathan Kutsch
# Section:      514
# Assignment:   Lab 3b - Program 1c
# Date:         05 September 2020

stefan_constant = 5.67 * 10**-8
temp = float(input('The temperature being calculated is: '))
stefan_boltzmann = stefan_constant * temp ** 4
print('Stefan Boltzmann Law =', stefan_boltzmann)
# Stefan-Boltzmann Law formula: Stefan's constant * Temperature^4