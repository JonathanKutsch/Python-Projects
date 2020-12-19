# By submitting this assignment, I agree to the following:
#  "Aggies do not lie, cheat, or steal, or tolerate those who do"
#  "I have not given or received any unauthorized aid on this assignment"
#
# Name:        Jonathan Kutsch
# Section:     514
# Assignment:  Lab 06b - Program 2
# Date:        25 September 2020


import matplotlib.pyplot as plt

number = int(input('Enter a positive integer: '))
list1 = []
list2 = []

count = 0
while number != 1:
    count += 1
    if number % 2 == 0:
        number = number // 2
        list1.append(number)
        list2.append(count)
    else:
        number = number * 3 + 1
        list1.append(number)
        list2.append(count)


print(list1)
print(list2)

plt.plot(list1, list2, '-o')
plt.title("Collatz Conjecture")
plt.xlabel("Number")
plt.ylabel("Steps Taken")
plt.show()