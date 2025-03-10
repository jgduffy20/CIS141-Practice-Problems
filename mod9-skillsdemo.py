# Mod 9 Skills Demonstration
'''
Make the following changes to the file:

Update get_gpa() using the grade* point average calculator function you designed in Mod 4 Skills Demonstration.
- You can copy and paste the function body for this demonstration (it would be silly to make you re-type).
- Your goal is to have the application display the student's grade* point average (GPA) for the class based on the score (0-100) that they input.
- You're welcome to print out any other information in addition to the GPA.
- Add a link to our Syllabus between "Learn More" and the link to the OC CIS homepage ("https://olympic.instructure.com/courses/2549477/assignments/syllabus").
'''

import tkinter as tk
from tkinter import messagebox
import webbrowser

def get_gpa(score):
    #Errors out if the user puts in a value that can't be turned into a float
    try:
        score = float(score)
    except ValueError:
        return "Please enter a valid number."

    #Errors if the user puts in a number outside the specified range
    if score < 0 or score > 100:
        return "Score must be between 0 and 100."

    #Replace the code here with your code
    if score >= 93:
        gpa = 4.0
    elif score >= 90:
        gpa = 3.7
    elif score >= 87:
        gpa = 3.3
    elif score >= 83:
        gpa = 3.0
    elif score >= 80:
        gpa = 2.7
    elif score >= 77:
        gpa = 2.3
    elif score >= 73:
        gpa = 2.0
    elif score >= 70:
        gpa = 1.7
    elif score >= 67:
        gpa = 1.3
    elif score >= 63:
        gpa = 1.0
    elif score >= 60:
        gpa = 0.7
    else:
        gpa = 0.0
    if gpa <= 2.0:
        return f"{gpa} Sorry, you have to take the course again"
    else:
        return f"{gpa} Good job"

def submit_score():
    score = score_entry.get()
    result = get_gpa(score)
    result_label.config(text=result)

def open_link(event):
    webbrowser.open("https://www.olympic.edu/academics/academic-pathways/business-information-technology/computer-information-systems")

def open_link2(event):
    webbrowser.open("https://olympic.instructure.com/courses/2549477/assignments/syllabus")

# Create the main window
window = tk.Tk()
window.title("Course GPA Evaluator")
window.geometry("500x500")

# Set up the menu with an Exit option
menu_bar = tk.Menu(window)
file_menu = tk.Menu(menu_bar, tearoff=0)
file_menu.add_command(label="Exit", command=window.quit)
menu_bar.add_cascade(label="File", menu=file_menu)
window.config(menu=menu_bar)

# Display the logo image at the top
logo_img = tk.PhotoImage(file="logo.png")
logo_label = tk.Label(window, image=logo_img)
logo_label.pack(pady=10)

# Label and entry for score input
info_label = tk.Label(window, text="This app helps you determine your course GPA(0.0-4.0) from your class score (0-100):")
info_label.pack(pady=5)
score_label = tk.Label(window, text="Enter your score (0-100):")
score_label.pack(pady=5)
score_entry = tk.Entry(window)
score_entry.pack(pady=5)

# Button to submit the score
submit_button = tk.Button(window, text="Submit", command=submit_score)
submit_button.pack(pady=10)

# Label to display the GPA message/result
result_label = tk.Label(window, text="", font=("Arial", 14))
result_label.pack(pady=10)

#Learn more text
learn_label = tk.Label(window, text="Learn more")
learn_label.pack(pady=5)

# Hyperlink to the Olympic College Computer Information Systems homepage
link_label = tk.Label(window, text="Olympic College Computer Information Systems (CIS)", fg="blue", cursor="hand2")
link_label.pack(pady=5)
link_label.bind("<Button-1>", open_link)

link_label2 = tk.Label(window, text="CIS Syllabus", fg="blue", cursor="hand2")
link_label2.pack(pady=5)
link_label2.bind("<Button-1>", open_link2)

window.mainloop()
