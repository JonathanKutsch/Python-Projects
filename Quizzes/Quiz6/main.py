# By submitting this assignment, I agree to the following:
#  Aggies do not lie, cheat, or steal, or tolerate those who do
#  I have not given or received any unauthorized aid on this assignment
#
# Name:         Jonathan Kutsch
# Section:      514
# Assignment:   Quiz 6 - Plotting
# Date:         15 November 2020

import matplotlib.pyplot as plt
# import necessary libraries

x = []
engineers = []
non_engineers = []
# create empty lists

for i in range(0, 61):
    x.append(i)
    engineers.append(1 / 60 * ((i - 100)**2) + 10)
    non_engineers.append((-1 / 8) * i + 30)
    # utilize loop to populate lists for plotting

plt.plot(x, engineers, color="blue", linewidth=1.0, label="Engineering Majors")
plt.plot(x, non_engineers, color="red", linewidth=1.0, label="Non-Engineering Majors")
plt.legend(loc="upper right")
plt.title('Excitement Level by Major for the Release of "The Mandalorian" Season 2', fontsize=9.5)
plt.xlabel("Days until Release")
plt.ylabel("Excitement Level")
plt.show()
# plot data with proper labels
