################################################################# 
# Class: CMSC135
# Instructor: Bahn
# Program Assignment: 5_1
# Program Name:  LevineMilesAssignment5_1.py
# Author: Miles Levine
# Due Date:               04/19/2023 
# Description: Give a brief description of each Program
#      I pledge that I have completed the programming assignment independently.
  	#     I have not copied the code from a student or any source.
 #  I have not given my code to any student.
  #   Print your Name here: Miles Levine
            
# Pseudocode: Write Pseudocode here for the program
# inside the main function
# try statement that tries to execute the open file function
# open the file "numbers.txt"
# for loop that reads each line in the txt folder until there is no next line
# make amount variable is where the value read on the line is being stored
# make the total variable adds the numbers in each line
# make the count variable is counting the lines of the txt file
# outside of for loop
# close the file
# calculate the average by having the total divided by the count
# print the average with the correct format
# throw the IOError exception if the file name is incorrect or if the file doesn't exist
# throw the ValueError exception if the .txt file has a value that is not an integer
# call the main function
###################################################################




def main():
    total = 0.0
    count = 0
    try:
        #open the file
        infile = open('numbers.txt', 'r')
        
        #for loop that reads each line in the txt folder until there is no next line
        for line in infile:
            #the amount variable is where the value read on the line is being stored
            amount = float(line)
            #the total variable adds the numbers in each line 
            total += amount
            #the count variable is counting the lines of the txt file 
            count += 1
        
        #close file
        infile.close()
        #calculate average
        avg = float(total/count)
        #print average with correct format
        print(format(avg, ',.2f'))

    except IOError:
        print("An error occurred while trying the read the file.")

    except ValueError:
        print("Non-numeric data found in the file.")
    
main()
