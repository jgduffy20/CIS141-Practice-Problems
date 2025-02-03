# 1. Construct a truth table for the expression: (A AND B) OR (NOT B) where A and B each can be True or False.
# Your truth table should be commented out (as it's not valid Python code!)

# A | B | NOT B | A AND B | (A AND B) OR (NOT B) #Starting with stating the requested variables.
# ----------------------------------------------
# T | T |   F   |    T    |         T            # If A is True and B is true, then Not B is the flip, A&B are true, w/ (A&B) or (Not B) being true.
# T | F |   T   |    F    |         T            # If A is true and B is false, then Not B is true. A&B are false due to mismatch, OR is true.
# F | T |   F   |    F    |         F            # I don't like truth tables much, to be honest, but mostly because theyre tedious. This is the only combinationin which A&B and Not B are both False, due to A being true and B being false, resulting in the OR expression being false.
# F | F |   T   |    F    |         T            # Because Both A and B seprately are false, not b is true, A&B is false, and the OR is true.

# 2. The headlights of a car should only automatically turn on when the daylight outside is below a certain threshold.
# If a sensor threshold is below the number 8, print "Headlights On"; otherwise, print "Headlights Off".

sensor_value = int(input("Heyo, on a scale of 1(Midnight) to 10(Highnoon), how bright is it right now?"))  # This is how much the sensor detects
if sensor_value < 8: # If threshold is less than 8
    print("Headlights On") # Then let us know the Headlights are on
else:                      # Otherwise
    print("Headlights Off")# Say the headlights are off.

# 3. Prompt the user for their bank balance. Evaluate whether the balance is less than $100.
# Print True if the user’s balance is below $100; print False, otherwise.

balance = float(input("Please enter your bank balance: "))  # Request balance from the user
if balance < 100:
    print(True) # Is the balance less than 100? then print true
else:
    print(False)# Otherwise, print false

# 4. A theater wants to enforce age restrictions for movie tickets. Ask the user for their age,
# and tell them whether they can see G (appropriate for under 13), PG-13 (appropriate for 13 to 17),
# or R (appropriate for over 18) rated movies.

age = int(input("Hello and welcome to the Movie Theater, we have lots of mives but require your age to begin: ")) #Ask the user for their age
if age < 13:    #If younger than 13, You only get G rated films
    print("You can see G Rated movies, you can watch 2001 A Space Odyssey!")
elif age <= 17: #If 17 or younger, can only watch PG-13 films
    print("You're able to watch PG-13 Rated films, Ghostbusters and Gremlins right this way!")
else:           #If an adult, R rated films are ok
    print("An adult heh? For R Rated films, we are showing The Matrix right now")

# 5. A store charges $5 for shipping on any order under $50. If the order amount is $50 or more, shipping is free.
# Ask the user for the order total and print the total cost, including shipping.

order_total = float(input("Seems youve finished your shopping, please provide your subtotal so I can check for free shipping eligability: ")) #An annoying chat bot pops up randomly and asks for for your subtotal to figure out if you get free shipping yet.
if order_total < 50:
    total = order_total + 5     #If order_total is less than $50, then I say add the shipping!
    close = 50 - order_total    #And for funzies, calculate how much they need to get the free shipping
    print(f"So close, your Total cost is ${total:.2f} and you need ${close:.2f} more to reach free shipping")
else:
    total = order_total         #Otherwise, the price is the price with free shipping
    print(f"Free shipping eligable! Total cost: ${total:.2f}")
