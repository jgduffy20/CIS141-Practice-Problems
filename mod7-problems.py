'''
#1. Write a function called count_vowels(input) that takes a string
    and returns the number of vowels (a, e, i, o, u) in it. Why not Y?
'''
def count_vowels(input_str):# Count vowels in a string (case-insensitive)

    count = 0                                  # Initialize a counter for vowels
    for char in input_str.lower():             # Convert to lowercase and iterate through each character
        if char in {'a', 'e', 'i', 'o', 'u'}:  # Check if character is a vowel
            count += 1                         # Increment counter if it's a vowel
    return count                               # Return the total count of vowels
'''
#2. Write a function called is_palindrome(s) that checks whether a string is a palindrome
    (reads the same forward and backward, ignoring case). The function should returns
    either True or False.
'''
def is_palindrome(s):
    lower_s = s.lower()              # Convert string to lowercase
    return lower_s == lower_s[::-1]  # Compare string with its reverse
    # [::-1] is slicing the syntax that reverses the string
    # If they're equal, it's a palindrome, so return True; otherwise, False

'''
#3. In the game Pokemon, certain types of Pokemon do extra damage to other types.
    For example, water is very effective to fight fire.
    Write a function called type_advantage(attacker, defender) that takes two Pokémon types as
    strings and returns "Super Effective", "Not Very Effective", or "Neutral" based on
    simple type effectiveness rules. Your solution only needs to work for these three sets of input:
    print(type_advantage("Water", "Fire"))  # "Super Effective"
    print(type_advantage("Fire", "Water"))  # "Not Very Effective"
    print(type_advantage("Electric", "Grass"))  # "Neutral"
'''
def type_advantage(attacker, defender): # Determine type effectiveness for specific matchups
    if attacker == "Water" and defender == "Fire":
        return "Super Effective"     # Water beats Fire
    if attacker == "Fire" and defender == "Water":
        return "Not Very Effective"  # Fire is weak against Water, burnz up
    return "Neutral"                 # Default case for all other matchups


'''
#4. Write a function called ferry_fare(age, vehicle) that calculates the Washington State Ferry fare
    based on age and whether the person has a vehicle. Assume the following rates:
    * Adults (19-64): $10 without a vehicle, $20 with a vehicle.
    * Seniors (65+): $5 without a vehicle, $15 with a vehicle.
    * Children (0-18): Free.
'''
def ferry_fare(age, vehicle):
    if age <= 18:
        return 0                     # Children (0-18) ride free, yay!
    elif 19 <= age <= 64:
        return 20 if vehicle else 10 # Adults: $20 with vehicle, $10 without
    else:                            # This covers ages 65 and above
        return 15 if vehicle else 5  # Seniors: $15 with vehicle, $5 without

'''
#5. Write a function called level_up(experience) that takes a player's experience points
    and returns their new level based on these rules:
    * 0-99 XP → Level 1
    * 100-199 XP → Level 2
    * 200+ XP → Level 3
'''
def level_up(experience):# Figure out player level based on experience points
    if experience < 100:
        return 1         # Level 1 for 0-99 XP
    elif experience < 200:
        return 2         # Level 2 for 100-199 XP
    return 3             # Level 3 for 200+ XP
    # No need for final else, as all other cases are covered

''' Now i intend to use these functions? I feel weird just defining something and not using it but i didn't see where that was exactly said. '''

print("Vowels in 'Hello World':", count_vowels("Hello World"))

# Test is_palindrome function
print("Is 'racecar' a palindrome?", is_palindrome("racecar"))
print("Is 'hello' a palindrome?", is_palindrome("hello"))

# Test type_advantage function
print("Water vs Fire:", type_advantage("Water", "Fire"))
print("Electric vs Grass:", type_advantage("Electric", "Grass"))

# Test ferry_fare function
print("Ferry fare for 25 year old with vehicle:", ferry_fare(25, True))
print("Ferry fare for 70 year old without vehicle:", ferry_fare(70, False))

# Test level_up function
print("Level for 150 XP:", level_up(150))
print("Level for 250 XP:", level_up(250))
