# By submitting this assignment, I agree to the following:
#  �Aggies do not lie, cheat, or steal, or tolerate those who do�
#  �I have not given or received any unauthorized aid on this assignment�
#
# Name:         Jonathan Kutsch
# Section:      514
# Assignment:   Lab 04b - Program 4
# Date:         12 September 2020

# report calculated stress for a given strain

# Variables:
#  pointO = [(0, 0)]
#  pointA = [(0.01, 42)]
#  pointC = [(0.06, 44)]
#  pointD = [(0.18, 60)]
#  pointE = [(0.26, 50)]
#  # to display data given

YM1 = 4200
YM2 = 40
YM3 = 133.3333
YM4 = -125
# calculate the value of Young's Modulus for each line segment using change in stress / change in strain

strain = float(input("Enter strain: "))
# request user input

if 0 <= strain < 0.01:
    y1 = 0 + YM1 * (strain - 0)
    print("Increasing linear elastic region at", y1, "ksi")
elif 0.01 <= strain < 0.06:
    y2 = 42 + YM2 * (strain - 0.01)
    print("Plastic region at", y2, "ksi")
elif 0.06 <= strain < 0.18:
    y3 = 44 + YM3 * (strain - 0.06)
    print("Strain hardening region at", y3, "ksi")
elif 0.18 <= strain <= 0.26:
    y4 = 60 + YM4 * (strain - 0.18)
    print("Necking region at", y4, "ksi")
else:
    print("The stress level is not indicated.")
# loop the strain given to find proper category, then calculated to find stress in ksi
