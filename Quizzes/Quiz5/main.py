# By submitting this assignment, I agree to the following:
#  "Aggies do not lie, cheat, or steal, or tolerate those who do"
#  "I have not given or received any unauthorized aid on this assignment"
#
# Name:        Jonathan Kutsch
# Section:     514
# Assignment:  Quiz 5 - Lists
# Date:        05 October 2020

list1 = [85, 79.5, 95, 62, 92.7, 89, 63, 91.5, 93, 90.5, 83, 87, 75]

print("The original list of quizzes is", list1)
list1.insert(4, 80)
# insert week 5 grade
list1.append(100)
# add last quiz grade to end
print("The updated list of quizzes is", list1)

print("The number of weeks of quizzes taken is", len(list1))
# total weeks of quizzes
print("The average of all the quiz grades is", sum(list1) / len(list1))
# finding the overall average

first_five = list1[0:5]
print("The first five quizzes are", first_five)
print("The average for the first five quizzes is", sum(first_five) / len(first_five))
# divide list of 15 items into 3 sections, then print average of each 3 sections

second_five = list1[5:10]
print("The second five quizzes are", second_five)
print("The average for the second five quizzes is", sum(second_five) / len(second_five))

third_five = list1[10:15]
print("The third five quizzes are", third_five)
print("The average for the third five quizzes is", sum(third_five) / len(third_five))
