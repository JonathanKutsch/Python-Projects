# By submitting this assignment, I agree to the following:
#  "Aggies do not lie, cheat, or steal, or tolerate those who do"
#  "I have not given or received any unauthorized aid on this assignment"
#
# Name:        Jonathan Kutsch
# Section:     514
# Assignment:  Lab 07b - Program 3
# Date:        02 October 2020

class_name = []
class_hour = []
class_grade = []

classes = int(input("How many classes are you taking?"))
for i in range(classes):
    # loops through questions until you reach number of inputted classes
    name = input("What is the name of the class?: ")
    class_name.append(name)
    # store name of class
    hours = int(input("How many credit hours?: "))
    class_hour.append(hours)
    # store credit hours
    grade = input("Final letter grade: ")
    class_grade.append(grade)
    # store grades
grade_points = {'A': 4,
                'B': 3,
                'C': 2,
                'D': 1,
                'F': 0,
                'U': 0}
# store grade points in dictionary

point_total = 0
for grade in class_grade:
    point_total += grade_points[grade]
    # points = point_total * sum(class_hour)
    break
# for every grade inputted, find total points and break

if 'U' not in class_grade:
    sum_pointTotal = point_total * sum(class_hour)
    # find sum of point total of all classes
    total_hours = sum(class_hour)
    # find total hours taken
    gpa = sum_pointTotal / total_hours
    print("GPA: ", gpa)

if 'U' in class_grade:
    sum_pointTotal = point_total * sum(class_hour) - 2
    # adjust the total points if a grade is Unsatisfactory (U)
    total_hours = sum(class_hour)
    gpa = sum_pointTotal / total_hours
    print("GPA: ", gpa)
