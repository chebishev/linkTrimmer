import tkinter as tk
from tkinter import END, messagebox
from tkinter.ttk import Entry
import os
import pyshorteners
from dotenv import load_dotenv
from config import get_settings

settings = get_settings()
BITLY_API = settings.BITLY_API
ROOT_GEOMETRY = settings.ROOT_GEOMETRY
ROOT_RESIZABLE = settings.ROOT_RESIZABLE
ROOT_TITLE = settings.ROOT_TITLE
BUTTON_WIDTH = settings.BUTTON_WIDTH
BUTTON_BD = settings.BUTTON_BD



load_dotenv()

class LinkTrimmerApp:
    def __init__(self, root):
        """
        Create a new instance of LinkTrimmerApp.

        :param root: The parent window for this application.
        :type root: tkinter.Tk
        """
        self.root = root
        self.setup_ui()

    def setup_ui(self):
        """
        Sets up the user interface of the application.

        :return: None
        """
        self.root.geometry('550x330')
        self.root.resizable(False, False)
        self.root.title('Link Trimmer for YouTube/YouTube Music links')

        # Instructions
        tk.Label(
            self.root,
            text="\nPaste YouTube Music link and\nPick one of the options below:\n",
            font="Courier 15 bold"
        ).pack()

        # Input field
        self.entry = Entry(self.root, width=77)
        self.entry.focus_set()
        self.entry.pack()

        # Buttons
        tk.Button(self.root, text="Remove 'music.'", width=25, bd="3",
                  command=self.remove_music).place(x=70, y=160)

        tk.Button(self.root, text="Trim from '&' to the end", width=25, bd="3",
                  command=self.trim_from_ampersand_symbol).place(x=70, y=230)

        tk.Button(self.root, text="Quick trim", width=25, bg="forest green", fg="mint cream", bd="3",
                  command=self.trim_all).place(x=300, y=160)

        tk.Button(self.root, text="Shorten link with bit.ly", width=25, bd="3", bg="SteelBlue3", fg="mint cream",
                  command=self.shorten).place(x=300, y=230)

    def get_entry_text(self):
        """
        Retrieves and returns the text from the entry widget, with leading
        and trailing whitespace removed.

        :return: The trimmed text from the entry widget.
        :rtype: str
        """
        return self.entry.get().strip()

    def set_entry_text(self, text):
        """
        Sets the text of the entry widget to the given text and copies it to the
        system clipboard.

        :param text: The text to set in the entry widget and copy to the
            clipboard.
        :type text: str
        """
        self.entry.delete(0, END)
        self.entry.insert(0, text)
        self.copy_to_clipboard(text)
        messagebox.showinfo("Success", "URL copied to clipboard!")

    def copy_to_clipboard(self, text):
        """
        Copies the given text to the system clipboard.

        :param text: The text to copy to the clipboard.
        :type text: str
        """
        self.root.clipboard_clear()
        self.root.clipboard_append(text)
        self.root.update()  # Keeps clipboard contents after window closes

    def remove_music(self):
        """
        Removes the "music." substring from the text in the entry widget, if
        present, and updates the entry widget with the modified text. If the
        substring is not present, the original text is copied to the clipboard.

        :return: None
        """
        text = self.get_entry_text()
        if "music." in text:
            text = text.replace("music.", "")
            self.set_entry_text(text)
        else:
            self.copy_to_clipboard(text)

    def trim_from_ampersand_symbol(self):
        """
        Trims the text in the entry widget from the ampersand symbol (&) to the
        end of the text, if present, and updates the entry widget with the
        modified text. If the ampersand symbol is not present, the original text
        is copied to the clipboard.

        :return: None
        """
        text = self.get_entry_text()
        if "&" in text:
            text = text.split("&", 1)[0]
            self.set_entry_text(text)
        else:
            self.copy_to_clipboard(text)

    def trim_all(self):
        """
        Removes the "music." substring from the text in the entry widget, if
        present, and trims the text from the ampersand symbol (&) to the end of
        the text, if present. If neither the substring nor the ampersand symbol
        is present, the original text is copied to the clipboard.

        :return: None
        """
        text = self.get_entry_text()
        # Repeated code, because of the copy_to_clipboard method
        # If you call the methods directly you'll receive messagebox more than once
        # same as remove_music method
        if "music." in text:
            text = text.replace("music.", "")
        # same as trim_from_ampersand_symbol method
        if "&" in text:
            text = text.split("&", 1)[0]
        self.set_entry_text(text)

    def shorten(self):
        """
        Retrieves the text from the entry widget, shortens it using the bit.ly
        API, and sets the entry widget to the shortened URL. Also copies the
        shortened URL to the system clipboard.

        If the shortening process fails, an error message is displayed to the
        user.

        :return: None
        """
        url = self.get_entry_text()
        key = BITLY_API

        if not key or key == "Your API Key":
            messagebox.showerror("API Key Missing", "Please set a valid BITLY_API key in your .env file.")
            return

        try:
            shortener = pyshorteners.Shortener(api_key=key)
            short_url = shortener.bitly.short(url)
            self.set_entry_text(short_url)

            # Copy to clipboard
            self.root.clipboard_clear()
            self.root.clipboard_append(short_url)
            self.root.update()  # Keeps clipboard after window closes

        except Exception as e:
            messagebox.showerror("Shortening Failed", str(e))


if __name__ == "__main__":
    root = tk.Tk()
    app = LinkTrimmerApp(root)
    root.mainloop()
