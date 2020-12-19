# By submitting this assignment, I agree to the following:
#  �Aggies do not lie, cheat, or steal, or tolerate those who do�
#  �I have not given or received any unauthorized aid on this assignment�
#
# Name:         Jonathan Kutsch
# Section:      514
# Assignment:   Lab 3b - Program 2
# Date:         05 September 2020

import math

# t = (x, y)
t1 = float(input('Time for first point is: '))
# tested with 50 s
x1 = float(input('Initial position in the x-direction is: '))
# tested with 25 m
y1 = float(input('Initial position in the y-direction is: '))
# tested with 10 m
t2 = float(input('Time for second point is: '))
# tested with 100 s
x2 = float(input('Second position in the x-direction is: '))
# tested with 50 m
y2 = float(input('Second position in the y-direction is: '))
# tested with 25 m

velocity_x = (x2-x1) / (t2-t1)
velocity_y = (y2-y1) / (t2-t1)

print('Velocity in the x-direction is:', velocity_x, 'm/s')
# test output = 0.5 m/s
print('Velocity in the y-direction is:', velocity_y, 'm/s')
# test output = 0.3 m/s

overall_velocity = math.hypot(velocity_x, velocity_y)
print("Red's velocity is:", overall_velocity, 'm/s')
# test output = 0.58309518948453 m/s

mass = 3
kinetic_energy = (1/2 * mass * (overall_velocity ** 2))
print("Red's kinetic energy is:", kinetic_energy)
# test output = 0.5099999999999999
