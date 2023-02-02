import tkinter as tk
from tkinter import ttk, END
from tkinter.ttk import Entry

root = tk.Tk()
root.geometry('550x330')
root.resizable(False, False)
root.title('Link Trimmer for YouTube Music links')


# trims "music." from the link and returns it to the input field
def remove_music(text):
    text = text.replace("music.", "")
    entry.delete(0, END)
    return entry.insert(0, text)


# removes all characters from "&" to the end of the link and returns it to the input field
def trim_from_ampersand_symbol(text):
    if "&" in text:
        index_of_ampersand = text.index("&")
        entry.delete(0, END)
        return entry.insert(0, text[:index_of_ampersand])


# Executes the functions above with double click and return the modified link in the input field
def trim_all(text):
    remove_music(text)
    trim_from_ampersand_symbol(text)
    return text


# Initialize a Label to display the User Input
label = tk.Label(root, text="", font="Courier 15 bold")
label.configure(text="\nPaste YouTube Music link and\nPick one of the options below:\n")
label.pack()

# Create an Entry widget to accept User Input
entry = Entry(root, width=77)
entry.focus_set()
entry.pack()

# Creates Buttons for Removing, Trimming and Auto trimming:
ttk.Button(root, text="Remove 'music.'", width=20,
           command=lambda: remove_music(entry.get())).pack(pady=20)
ttk.Button(root, text="Trim from '&' to the end", width=25,
           command=lambda: trim_from_ampersand_symbol(entry.get())).pack(pady=20)
ttk.Button(root, text="Auto trim (press twice)", width=25,
           command=lambda: trim_all(entry.get())).pack(pady=20)

# execution of the program
root.mainloop()

# test inputs:

# https://music.youtube.com/watch?v=zqOWV_pq9Zs&feature=share

# https://music.youtube.com/watch?v=zqOWV_pq9Zs&list=RDAMVMzqOWV_pq9Zs
