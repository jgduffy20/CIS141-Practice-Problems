import math
# 1. Create a program that prints the following output to the screen: "Water. Earth. Fire. Air. Long ago, the four nations lived together in harmony. Then, everything changed when the Fire Nation attacked."
print("Water. Earth. Fire. Air. Long ago, the four nations lived together in harmony. Then, everything changed when the Fire Nation attacked.")
# 2. Create a program that prompts for 2 numbers and then outputs the addition, subtraction, multiplication, and division of the first number by the second number.
num_one = float(input("Please provide a number: "))
num_two = float(input("Please provide a second number: "))#asks nicely, then produces results
num_add = float(num_one + num_two)
num_sub = float(num_one - num_two)
num_mult = float(num_one * num_two)
num_div = float(num_one / num_two)
print(f"Here are your two numbers Added - {num_add}, Subtracted - {num_sub}, Multiplied - {num_mult}, Divided - {num_div}")
# 3. Create a program that prompts for the side lengths of a triangle and computes the area using Heron's formula.
a = float(input("Enter the side length of side A: "))
b = float(input("Enter the side length of side B: "))
c = float(input("Enter the side length of side C: ")) #first, ask for all sides, then calcs semi-perimeter:
s = (a+b+c)/2
area = math.sqrt(s*(s-a)*(s-b)*(s-c)) #then we Heron it:
print(f"The area of your very fun triangle is {area:.2f} units")
# 4. Create a program that computes different statistics given five numbers including the total, average, minimum, maximum, range, and standard deviation
num1 = float(input("Next, I'll need five more numbers from you, First number? "))
num2 = float(input("Second Number? "))
num3 = float(input("Third Number? "))
num4 = float(input("Fourth Number? "))
num5 = float(input("Fifth Number? "))
total = (num1+num2+num3+num4+num5) #start with adding them all together for the total
average = total/5 #easy average with five numbers
minimum = min(num1,num2,num3,num4,num5) #finding the minimum
maximum = max(num1,num2,num3,num4,num5)#using the max function since it kept popping up as i was typing maximum.
range_value = maximum - minimum #sub the max from the min
variance = (((num1 - average) ** 2) + #first we find the mean and subtract it from each value
    ((num2 - average) ** 2) +          #Then square each one and add them together
    ((num3 - average) ** 2) +           #divide by number of values
    ((num4 - average) ** 2) +           #square root.
    ((num5 - average) ** 2)) / 5
std_deviation = math.sqrt(variance)
print(f"Your Total is: {total:.2f}")
print(f"Average: {average:.2f}")
print(f"Minimum: {minimum:.2f}")
print(f"Maximum: {maximum:.2f}")
print(f"Range: {range_value:.2f}")
print(f"Standard Deviation: {std_deviation:.2f}")#and we finialize with eveything!
