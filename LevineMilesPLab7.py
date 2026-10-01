################################################################# 
# Class: CMSC135
# Instructor: Prof. Bahn
# Program Assignment: 7
# Program Name:      LevineMilesPLab7.py
# Author:           Miles Levine
# Due Date:               05/10/2023 
#      I pledge that I have completed the programming assignment independently.
  	#     I have not copied the code from a student or any source.
 #  I have not given my code to any student.
  #   Print your Name here: Miles Levine
            
# Pseudocode: Write Pseudocode here for the program
    #Ask user to input date in mm/dd/yyyy format
    #collects the input
    #split the string input where the "/" is
    #getMonth function gets the corresponding month in words as opposed to the number and returns that month
    #make a list containing every month
    #compare the first element of the split string to the month list to determine the corresponding month
    #return the month in letter format
    #print the date in the correct format
###################################################################


def main():
    #Ask user to input date in mm/dd/yyyy format
    date = input("Enter a date in the format mm/dd/yyyy: ")
    #collects the input
    #split the string input where the "/" is 
    x = date.split("/")
    #print the date in the correct format
    print(getMonth(x[0]) + " " + x[1] + ", " + x[2])

#getMonth function gets the corresponding month in words as opposed to the number and returns that month
def getMonth(x):
    #list containing every month
    monthList = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October','November', 'December']
    month = monthList[int(x) - 1]
    return month

main()
