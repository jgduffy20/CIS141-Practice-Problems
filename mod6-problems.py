#1. Given a list of numbers, write code to iterate through the list and calculate the sum of all even numbers. Print the resulting sum.

spacePotatoCollection = [2, 5, 8, 3, 10] # List of really cool space potatoes 
moonCheeseTotal = 0                     # Stores sum of even numbers for some cheesy moon math!

for cosmicSpud in spacePotatoCollection:  
    if cosmicSpud % 2 == 0:             # Check if spud is even  
        moonCheeseTotal += cosmicSpud  # Add to cheese hoard

print("Sum of even spuds:", moonCheeseTotal)  

#2. With a list of strings provided, write code that counts how many times the word "Olympic" appears in the list, and then print the count.

magicWordPile = ["Olympic", "College", "Olympic", "CIS"]  # List of magical incantations to summon the unicorn, dupilcates do it!
unicornTally = 0                    # Counts "Olympic" sightings

for sparkleWord in magicWordPile:   # If a repeated word is found,
    if sparkleWord == "Olympic":  
        unicornTally += 1           # Then Unicorn detected!  

print("Count of Olympic in list:", unicornTally)  


#3. Given a list of strings, write code to create a new list that includes only the strings longer than three characters. Print the resulting filtered list.

tinyDinosaurList = ["cat", "book", "python", "a"]  # List of tiny dinosaurs 
megaDinoStorage = []                        # Holds only BIG dinos, bigger than 3 characters 

for stegoSnack in tinyDinosaurList:         # For each snack in list, 
    if len(stegoSnack) > 3:                 # Check snack size  
        megaDinoStorage.append(stegoSnack)  # If bigger, Save for dino brunch  

print("Mega dinos:", megaDinoStorage) # Time to show the brunch to everyone!

#4. For a list of integers, write code that counts how many numbers are positive and how many are negative, then print both counts.

# I'm having fun with it at this point so please let me know if its too goofy for readabilities sake
numberZoo = [3, -2, 5, 0, -4, 7, 12, -9]  # Zoo of number animals 
happyHippoCount = 0     # Count the positive numbers  
grumpyGatorCount = 0    # & the negative numbers  

for zooCritter in numberZoo:  
    if zooCritter > 0:  
        happyHippoCount += 1  # Happy hippo!  
    elif zooCritter < 0:  
        grumpyGatorCount += 1  # Grumpy gator!  

print("Hippos:", happyHippoCount, "| Gators:", grumpyGatorCount)  


#5. For a list of integers, use a loop to build a new list where each element is the square of the corresponding element in the original list. Print the new list.

plainBreadLoaf = [1, 2, 3, 4]  # Boring bread
toastyCroutonCrate = []        # Stores squared bread cubes  

for slice in plainBreadLoaf:  
    toastyCroutonCrate.append(slice ** 2)  # Toast the bread and add to the end of the crate!

print("Croutons:", toastyCroutonCrate)  # Says how many in the crate

