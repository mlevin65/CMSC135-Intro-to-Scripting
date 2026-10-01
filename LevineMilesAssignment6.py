################################################################# 
# Class: CMSC135
# Instructor: Bahn
# Program Assignment: 6
# Program Name: LevineMilesAssignment6.py
# Author: Miles Levine
# Due Date: 
#05/3/2023 
# Description: Give a brief description of each Program collects 20 numbers and gets atributes of the numbers
# I pledge that I have completed the programming assignment independently.
# I have not copied the code from a student or any source.
# I have not given my code to any student.
# Print your Name here: Miles Levine
 
# Pseudocode: Write Pseudocode here for the program
#numbers variable to hold the array of 20 numbers
# for loop that reads each line in the txt folder until there is no next line
#low variable to get the lowest entered number
#high variable to get the highest entered number
#total variable to get sum of all numbers entered
#average variable to get the average of the 20 numbers entered
#get numbers function to collect each of the 20 numbers
    #for loop to get each number
#get lowest number function that passes the number array and returns the lowest number in the array
#get highest number function passes the number array and returns the highest number in the array
#get average function that passes the sum of the 20 numbers and returns the average of the 20 numbers
#get total function that passes the number array and returns the sum of all numbers entered
#call each function and print the correct output

###################################################################
def main():
    #numbers variable to hold the array of 20 numbers
    numbers  = GetNumbers()
    #low variable to get the lowest entered number
    low = getLow(numbers)
    #high variable to get the highest entered number
    high = getHigh(numbers)
    #total variable to get sum of all numbers entered
    total = getTotal(numbers)
    #average variable to get the average of the 20 numbers entered
    average = getAvg(total)
    #print the correct output
    print("Low:", low)
    print("High: ", high)
    print("Total: ", format(total,".2f"))
    print("Average: ", format(average,".2f"))
#get numbers function to collect each of the 20 numbers
def GetNumbers():
    numbs = []
    index = 1
    COUNT = 20
    #for loop to get each number
    for _ in range(COUNT):
        print('Enter number', index,'of 20: ')
        value = float(input())
        numbs.append(value)
        index = index + 1
    return numbs
#get lowest number function that passes the number array and returns the lowest number in the array
def getLow(nums):
    lowest = min(nums)
    return lowest
    
#get highest number function passes the number array and returns the highest number in the array
def getHigh(nums):
    highest = max(nums)
    return highest 
#get average function that passes the sum of the 20 numbers and returns the average of the 20 numbers
def getAvg(total):
    avg = total/20


    return avg 
#get total function that passes the number array and returns the sum of all numbers entered
def getTotal(nums):
    total = 0.0
    for x in nums:
        total += x
    return total

#call main function
main()
