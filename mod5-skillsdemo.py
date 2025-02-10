'''
Write a program that solves this problem:

Use a loop (for or while) to go through numbers from 1 to 20.
If a number is a multiple of 3, use continue to skip printing it.
Otherwise, print the number.
'''
for numba in range(1, 21): #Goes through the range 1-20
    if numba % 3 == 0: #if divisable by 3
        continue #Skip over with continue
    print(numba) #print out the numba
