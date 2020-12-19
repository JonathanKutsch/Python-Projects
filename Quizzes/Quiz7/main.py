# By submitting this assignment, I agree to the following:
#  Aggies do not lie, cheat, or steal, or tolerate those who do
#  I have not given or received any unauthorized aid on this assignment
#
# Name:         Jonathan Kutsch
# Section:      514
# Assignment:   Quiz 7 - File Input
# Date:         20 November 2020

user_name = input("Enter username: ")
date = input("Enter the date? ")
playlist_name = input("Enter name of the playlist: ")
num = int(input("How many songs would you like to add to the playlist? "))
# request all user inputs to produce file output

songs = []
# make empty list to store songs

for i in range(0, num):
    song = input("Enter name of song: ")
    songs.append(song)
# iterate through every number up to number of songs inputted
# request name of song and append to list

create_list = '\n'.join(map(str, songs))
# join the list using map function to display line by line

# Then, the program should write the following:
with open("myplaylist.txt", 'w') as my_playlist:
    my_playlist.write(user_name)
    my_playlist.write("\n")
    my_playlist.write(date)
    my_playlist.write("\n")
    my_playlist.write(playlist_name)
    my_playlist.write("\n")
    my_playlist.write("--------------------------------")
    my_playlist.write("\n")
    my_playlist.write(create_list)
# write all code to output file

