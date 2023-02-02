import tkinter as tk
from tkinter import ttk, END
from tkinter.ttk import Entry

root = tk.Tk()
root.geometry('550x330')
root.resizable(False, False)
root.title('Link Trimmer')


def remove_music(text):
    text = text.replace("music.", "")
    entry.delete(0, END)
    return entry.insert(0, text)


def trim_from_and_symbol(text):
    if "&" in text:
        symbol_index = text.index("&")
        entry.delete(0, END)
        return entry.insert(0, text[:symbol_index])


def trim_all(text):
    remove_music(text)
    trim_from_and_symbol(text)
    return text


# Initialize a Label to display the User Input
label = tk.Label(root, text="", font="Courier 15 bold")
label.configure(text="\nPaste YouTube Music link and\nPick one of the options below:\n")
label.pack()

# Create an Entry widget to accept User Input
entry = Entry(root, width=77)
entry.focus_set()
entry.pack()

function_dictionary = {
    "remove_music": lambda x: x.replace("music.", ""),
    "trim_link": lambda x: x.replace("&feature=share", "")
}
# Create a Button to validate Entry Widget
ttk.Button(root, text="Remove '.music'", width=20, command=lambda: remove_music(entry.get())).pack(
    pady=20)
ttk.Button(root, text="Remove '&.......'", width=20, command=lambda: trim_from_and_symbol(entry.get())).pack(
    pady=20)
ttk.Button(root, text="Auto trim (press twice)", width=25, command=lambda: trim_all(entry.get())).pack(pady=20)

root.mainloop()

# test inputs:

# https://music.youtube.com/watch?v=zqOWV_pq9Zs&feature=share

# https://music.youtube.com/watch?v=zqOWV_pq9Zs&list=RDAMVMzqOWV_pq9Zs
