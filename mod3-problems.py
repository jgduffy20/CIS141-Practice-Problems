# 1. Prompt the user for a word. Then, prompt the user for how many times they'd like that word repeated. Use the skills you learned in this module to print the word the correct number of times.
word = input("Please provide a word for today: ") #Ask for word
rep = int(input("How many times shall I yell it to the void? ")) # Ask for repition amount & change to int for multiplying
print(word * rep) #Now YELL INTO THE VOID
#2. Prompt the user for their name and their age. Calculate their age next year. Use string concatenation to print "Hello, <name>! You are <age1> years old. Next year, you will be <age2> years old."
name = input("Please provide your name: ") #Ask for name
currentage = int(input("Please provide your current age: ")) #asking foor current age and changing to int for usage
futureage = currentage + 1 # it'll be next year so, one away
final = "Hi, " + name + "! You are currently " + str(currentage) +" years old. Next year, you're gonna be " + str(futureage) + " years old." #Convert the objects to strings so the message can be displayed
print(final) #Print out the victory line
#3. Prompt the user for a sentence and a word to try to find in that sentence. Have the program print out whether the word was found in the sentence. (i.e. True or False)
long = input("Enter a sentence please:\n") #ask for sentence from user
findr = input("Please provide a word to locate within the sentence:\n") #ask for locater word
foundr = findr in long #look for the word in the sentence
print(foundr) #print our mission success or failure
#4. Prompt the user for: a word, a first index, and a last index. Slice the word at the indexes provided by the user and print to the screen.
word1 = input("Please give me word, longer the better: ")#asking for the word, the longer the better
onst = int(input("Please provide the first index: ")) #One-st index
ndst = int(input("Please provide the second index: ")) #Secondst Index
chop = word1[onst:ndst] #At the end of the day, theyre all just variables and this is just math
print(chop) #Print the results
#5. Print 3 words with a | character (called a pipe) in between them. Use the appropriate keyword argument in print() to do so.
print("Since three words have already been accounted for, here they are:\n")
print(word, findr, word1, sep="|")
