# By submitting this assignment, I agree to the following:
#  Aggies do not lie, cheat, or steal, or tolerate those who do
#  I have not given or received any unauthorized aid on this assignment
#
# Name:         Jonathan Kutsch
# Section:      514
# Assignment:   Lab 10b - Program 2
# Date:         24 October 2020

import csv

loan_amount = float(input("What is the amount of the loan? "))
interest_rate = float(input("What is the annual interest rate? "))
month_pay = float(input("What is the monthly payment? "))

titles = ['Month', 'Principal Balance', 'Accrued Interest']

store = []
month = 0
accrued_interest = 0
interest_rate = interest_rate / 100
# create empty list
# preset variables
# convert interest rate to percent

if month_pay <= 0:
    for month in range(0, 31):
        data = [month, loan_amount, accrued_interest]
        store.append(data)
        accrued_interest += loan_amount * (interest_rate / 12)
        loan_amount = loan_amount + loan_amount * (interest_rate / 12)
        loan_amount -= month_pay
else:
    for month in range(0, 31):
        if loan_amount > 0:
            data = [month, loan_amount, accrued_interest]
            store.append(data)
            accrued_interest += loan_amount * (interest_rate / 12)
            loan_amount = loan_amount + loan_amount * (interest_rate / 12)
            loan_amount -= month_pay
        else:
            break
# use if/else statements to iterate through month calculations based on month payment

n = len(store)
for i in range(0, n):
    print(store[i], end='\n')
# assign to each line
# prints for convenient view before requesting to write to file

portfolio = open(input("Enter Filename: ") + '.csv', 'w', newline='')

write = csv.writer(portfolio)
write.writerow(titles)
csv.writer(portfolio, delimiter=' ')
write.writerows(store)
# write to file with proper titles, separation, and calculated data

portfolio.close()