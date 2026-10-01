################################################################# 
# Class: CMSC135
# Instructor: Last Name First Name
# Program Assignment:  ## Assignment Number
# Program Name: LevineMilesAssignment4.py
# Author:  Miles Levine
# Due Date: 04/5/2023
# Description: Give a brief description of each Program
#      I pledge that I have completed the programming assignment independently.
  	#     I have not copied the code from a student or any source.
 #  I have not given my code to any student.
  #   Print your Name here: Miles Levine
            
# Pseudocode: Write Pseudocode here for the program
# Create the function showIncome with 3 params to take in each count for seats A, B, and C
# inside the showIncome calculate the income for seats A, B, and C
# calculate the total income of all seats
# print the incomes with correct format
# prompt the user to imput the data
# call the showIncome function whle passing the 3 inputs for the parameters.
#
#
###################################################################




def showIncome(seatA, seatB, seatC):
    incomeA = float(20 * seatA )# Calculate income for A tickets
    incomeB = float(15 * seatB )# Calculate income for B tickets
    incomeC = float(10 * seatC) # Calculate income for C tickets

    totalIncome = float(incomeA + incomeB + incomeC) #Calculate the total income
    print ("\nIncome from class A seats: $", format(incomeA, ',.2f'), sep='')
    print ("Income from class B seats: $", format(incomeB, ',.2f'), sep='')
    print ("Income from class C seats: $", format(incomeC, ',.2f'), sep='')
    print ("\nTotal income: $", format(totalIncome, ',.2f'), sep='')

#propmpt user to imput the data
seatA = float(input("Enter count of A seats: "))
seatB = float(input("Enter count of B seats: "))
seatC = float(input("Enter count of C seats: "))

showIncome(seatA, seatB, seatC) # call function
