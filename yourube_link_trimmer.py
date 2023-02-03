import pyshorteners
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


# Executes the functions above and return the modified link in the input field
def trim_all():
    remove_music(entry.get())
    trim_from_ampersand_symbol(entry.get())


def shorten_url(url):
    service = pyshorteners.Shortener(api_key='6e4f69ed88460cc3cb3c96b6c1857c64e26ef452')
    short_url = service.bitly.short(url)
    entry.delete(0, END)
    return entry.insert(0, short_url)


# Initialize a Label to display the User Input
label = tk.Label(root, text="", font="Courier 15 bold")
label.configure(text="\nPaste YouTube Music link and\nPick one of the options below:\n")
label.pack()

# Create an Entry widget to accept User Input
entry = Entry(root, width=77)
entry.focus_set()
entry.pack()

# Creates Buttons for Removing, Trimming and Auto trimming:
tk.Button(root, text="Remove 'music.'", width=25, bd="3",
          command=lambda: remove_music(entry.get())).place(x=70, y=160)
tk.Button(root, text="Trim from '&' to the end", width=25, bd="3",
          command=lambda: trim_from_ampersand_symbol(entry.get())).place(x=70, y=230)
tk.Button(root, text="Quick trim", width=25, bg="forest green", fg="mint cream", bd="3",
          command=lambda: trim_all()).place(x=300, y=160)
button_text = "Get short link"
tk.Button(root, text=button_text, width=25, bd="3", bg="SteelBlue3", fg="mint cream",
          command=lambda: shorten_url(entry.get())).place(x=300, y=230)

# execution of the program
root.mainloop()

# test inputs:

# https://music.youtube.com/watch?v=zqOWV_pq9Zs&feature=share

# https://music.youtube.com/watch?v=zqOWV_pq9Zs&list=RDAMVMzqOWV_pq9Zs
