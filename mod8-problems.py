'''
-----------------------------------MODULE 8 PRACTICE PROBS -----------------------------------------------------------
I'm very tired, but hopefully things will be getting better soon. Thanks for your understanding!
------------------------------------------------------------------------------------------------------
#1. Create a file called gardening_tips.txt and add at least 3 gardening tips to
it.
Write a Python script that reads a file gardening_tips.txt and prints
out each tip one by one.
'''
# Create list of gardening tips
gardening_tips = [
    "Water your plants early in the morning to reduce evaporation.",
    "Use compost to enrich your soil with nutrients.",
    "Prune your plants regularly to encourage healthy growth."]

# Open file in write mode to create/overwrite it
with open("gardening_tips.txt", "w") as file:
    for tip in gardening_tips:# Loop through each tip in the list
        file.write(tip + "\n")# Write tip to file with newline character

# Open file in read mode to access contents
with open("gardening_tips.txt", "r") as file:
    print("Gardening Tips:")# Print header for output
    for line in file:       # Read file line by line
        print(line.strip()) # Remove whitespace and print clean line

'''
#2. Write a Python program that allows users to log their hiking trips. The program
should:
- Use a while loop to repeatedly ask for a hike name and distance in miles
- Save each entry to hiking_log.txt (each hike on a new line)
- When the user presses 0, exit the loop & print the contents of hiking_log.txt
'''
# Open file in append mode to preserve existing entries
with open("hiking_log.txt", "a") as file:
    while True:                                                                # Start infinite loop for user input
        hike_name = input("Please provide the name of your hike(0 to stop): ") # Get hike name from user
        if hike_name == "0":                                                   # Check for exit condition
            break                                                              # Exit loop
        distance = input("Enter the distance of the hike in miles: ")          # Get distance from user
        file.write(f"{hike_name} - {distance} miles\n")                        # Write the user entry to file

# Open file in read mode to display contents
with open("hiking_log.txt", "r") as file:
    print("\nHiking Log:")  # Print log header
    for line in file:       # Read each line from file
        print(line.strip()) # Clean and print each entry

'''
#3. Create a text file called song_lyrics.txt and copy the lyrics of a song into
it. Write a Python program that:
- Reads the file
- Requests 5 inputs from the user: 5 words the user would like to count the
frequency of
- Counts how many times each word appears
- Creates a dictionary of the words and their counts
- Print the dictionary to the console
'''
# Open lyrics file for reading
with open("song_lyrics.txt", "r") as file:
    lyrics = file.read().lower()                                                                                                    # Read entire file content and convert to lowercase
word_counts = {}                                                                                                                    # Create empty dictionary for word counts
for count in range(5):                                                                                                              # Loop 5 times to get user words
    word = input(f"Please provide 5 words you would like counted from your provided lyrics({(count - 5)* -1} Words left): ").lower()# Get word input, say how many are left using some fun math I remembered and convert to lowercase
    word_counts[word] = lyrics.split().count(word)                                                                                  # Count occurrences in lyrics and store in dictionary
print("Word frequencies:", word_counts)                                                                                             # Print final results


'''
#4. Create a poll.txt file that contains a list of "yea" or "nay" votes separated
by commas.
Write a program that reads the poll.txt file
Count how many votes "yea" or "nay" received and print the results.
'''

# Open poll file for reading
with open("poll.txt", "r") as file:
    votes = file.read().split(",") # Read all yea and nays and split into list using commas
results = {                        # Create dictionary with vote counts
    "yea": votes.count("yea"),     # Count 'yea' votes
    "nay": votes.count("nay")}     # Count 'nay' votes
print("Vote Results:", results)    # Display final results, yay! All done.
