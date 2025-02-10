
# Mod5-Problems
#1. Prompt the user for a positive integer n. Use a while loop to sum all the integers from 1 up to n. Print the final sum.

numba = int(input("Enter a positive numba please: ")) #Ask user for a positive number

total = 0
counter = 1 # Define sum and counter

while counter <= numba:# Use while loop to sum numbas from 1 to numba
    total += counter #Go up on the total
    counter += 1 #go up on the counter

print(f"The sum of numbas from 1 to {numba} is: {total}, its the total number of pets my cat allows before he gets ya")

#2. Define a string variable (e.g., my_string = "Olympic College"). Use a for loop to print each character on its own line. Convert each character to uppercase before printing.

my_string = "That's not my wallet"# Here is your wallet

for char in my_string: # Define char for the characters to use, then use for loop to print each character in uppercase
    print(char.upper()) # Print them on each line

#3. Use a for loop and the range() function to print all even numbers from 2 to 20.

for numb in range(2, 21): #Define numb and set it through the ranges
    if numb % 2 == 0: #But if ol numb is even(or just divisable by 2), Print em
        print(numb)

#4. Use nested for loops to create a simple multiplication table for numbers 1 through 5. Format your output so that each row corresponds to multiplying by a specific number. Example output:
# 1   2   3   4   5
# 2   4   6   8   10
# 3   6   9   12  15
# 4   8   12  16  20
# 5   10  15  20  25


for i in range(1, 6):# Define i and loop 1-5 to start the multiplication table
    for j in range(1, 6): # Define j and loop through 5, so many loops, feeling like the circus
        print(f"{i*j:4}", end="") #print each number in its spot
    print()  # Move to next line after each row

'''
#5. Write a program that continuously asks the user to input a number. If the user enters 0, immediately stop asking for more numbers. Otherwise, print the number they entered. Sample interaction:

Enter a number (0 to stop): 4
You entered 4
Enter a number (0 to stop): 7
You entered 7
Enter a number (0 to stop): 0
Exiting...
'''

while True:
    numf = int(input("Gimmie a number (0 to stop): ")) # Ask for the first number and keep going until said otherwise
    if numf == 0:#this is the otherwise
        print("Nothing? Ugh, Bye...")#Printing that it is over between us
        break
    print(f"You gave me {numf}, i asked for {numf}. Can't hear or somethin?")#This is the other half to the loop circle we created, it'll keep printing until inputted again

