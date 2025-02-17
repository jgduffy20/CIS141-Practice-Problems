# Create a program that loops over a list and does something interesting with that list.
# Your program must be different than any of the Practice Problems or any code we covered together in the Lecture videos.
# Be creative! Try to personalize your program to your own life & interests.

# Book genre analyzer program, Find out how much of my library is goofy!
# Calculates the Genre percentage of a given library list


books = [
    ["To Kill a Mockingbird", "Fiction"],
    ["Hunger Games", "Dystopian"],
    ["The Great Gatsby", "Fiction"],
    ["Eye of Minds", "Science Fiction"],
    ["The Hobbit", "Fantasy"],
    ["Dune", "Science Fiction"]
]       # Creating the book list!
'''
books = [
    ["The Girl who loved Tom Gordon", "Mystery"],
    ["The Martian", "Science Fiction"],
    ["The Da Vinci Code", "Mystery"],
    ["The Princess Bride", "Fantasy"],
    ["The Girl with the Dragon Tattoo", "Mystery"],
    ["The Adventures of Tom Sawyer", "Historical Fiction"],
    ["Alice in Wonderland", "Fantasy"]
]       # Made another list!
'''
genres = [] # Initialize tracking lists Genres and Counts
counts = []

for book in books: # Process each book for book loop
    current_genre = book[1] # For each book on the list, check the 1 spot, which is second location since we start at 0

    if current_genre in genres:# Check if genre already tracked
        genre_index = genres.index(current_genre)
        counts[genre_index] += 1 # If tracked then move to next in list
    else:
        genres.append(current_genre)
        counts.append(1) # Otherwise, add it to the end


total_books = len(books)        # New list to do math against
print("Your Reading Breakdown:")# Tell the user their reading breakdown and then;
for i in range(len(genres)):    # Use variable i to go through genres list
    percentage = (counts[i] / total_books) * 100 # Checks out of 100 so we have a nice percentage
    print(f"- {genres[i]}: {percentage:.1f}% of your books") # Tell user their bookscore!
