# By submitting this assignment, I agree to the following:
#  "Aggies do not lie, cheat, or steal, or tolerate those who do"
#  "I have not given or received any unauthorized aid on this assignment"
#
# Name:        Jonathan Kutsch
# Section:     514
# Assignment:  Lab 06b - Program 3
# Date:        26 September 2020

pairs = int(input("How many username/password pairs? "))
i = 0
usernames = []
passwords = []

while i <= pairs:
    username = input("Enter username: ")
    usernames.append(username)
    password = input("Enter password: ")
    passwords.append(password)
    dictionary = {username: password}
    i += 1
    if i == pairs:
        request_user = input("Please enter your username: ")
        request_pass = input("Please enter your password: ")
        for i in range(len(usernames)):
            if request_user == usernames[i] and request_pass == passwords[i]:
                print("Login Successful")
                break
        else:
            print("Incorrect")
        exit()
