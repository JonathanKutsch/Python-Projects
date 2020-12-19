# By submitting this assignment, I agree to the following:
#  Aggies do not lie, cheat, or steal, or tolerate those who do
#  I have not given or received any unauthorized aid on this assignment
#
# Name:         Jonathan Kutsch
# Section:      514
# Assignment:   Quiz 8 - File Input/Output
# Date:         20 November 2020

like_list = []
# create empty array
with open("SocialMediaLikes.dat", 'r') as Likes:
    like = Likes.readlines()
    for line in like:
        if line != '\n':
            like_list.append(float(line))
# create data file that holds number of social media likes
copy_list = like_list[:]

weeks = int((len(copy_list)) / 7)
# find number of weeks

result = []
for i in range(weeks):
    result.append(sum(copy_list[0:7]) / 7)
    copy_list[0:7] = []
# pull every 7 elements of list and get average

with open('WeeklyAverages.dat', 'w') as averages:
    for i in result:
        averages.write(str(i) + '\n')
# convert each value to a string in order to write
# output the average values to a file
