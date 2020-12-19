# By submitting this assignment, I agree to the following:
#  Aggies do not lie, cheat, or steal, or tolerate those who do
#  I have not given or received any unauthorized aid on this assignment
#
# Name:         Jonathan Kutsch
# Section:      514
# Assignment:   Lab 11b - Program 1
# Date:         1 November 2020

def find_least_profitable(facilities, annual_cost, produce_values):
    # define the function and set variables

    facility_list = len(facilities)
    least_profitable = produce_values[0] - annual_cost[0]
    least_facility = facilities[0]
    # create a list for easy access in function

    for i in range(1, facility_list):
        profit = produce_values[i] - annual_cost[i]
        # for every element in facilities list, find profit
        if least_profitable > profit:
            least_profitable = profit
            least_facility = facilities[i]
        # reassign until the smallest profit is found

    return least_facility, least_profitable


def main():
    # new function to implement data

    facilities = ['Facility 1', 'Facility 2', 'Facility 3']
    annual_cost = [250, 500, 750]
    produce_values = [500, 1000, 1200]
    # hard code data

    result = find_least_profitable(facilities, annual_cost, produce_values)
    # store data from first function into a list to grab for answer

    print("Facility Name: ", result[0])
    print("Facility Profit: ", result[1])
    # pull answer from list and run the function


main()