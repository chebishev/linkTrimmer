import tkinter as tk
from tkinter import END, messagebox
from tkinter.ttk import Entry
import os
import pyshorteners
from dotenv import load_dotenv

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
            text="""Paste YouTube Music link and
                    Pick one of the options below:""",
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

        tk.Button(self.root, text="Shorten & Copy", width=25, bd="3", bg="SteelBlue3", fg="mint cream",
                  command=self.shorten_and_copy).place(x=300, y=230)

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
        Sets the text of the entry widget to the given text, after clearing its
        current contents.

        :param text: The new text to set in the entry widget.
        :type text: str
        """
        self.entry.delete(0, END)
        self.entry.insert(0, text)

    def remove_music(self):
        """
        Removes the substring "music." from the text in the entry widget,
        if it exists, and updates the entry with the modified text.

        :return: None
        """
        text = self.get_entry_text()
        if "music." in text:
            text = text.replace("music.", "")
            self.set_entry_text(text)

    def trim_from_ampersand_symbol(self):
        """
        Trims the text in the entry widget by removing all characters from
        the ampersand (&) to the end of the string, if the ampersand exists.

        :return: None
        """
        text = self.get_entry_text()
        if "&" in text:
            text = text.split("&", 1)[0]
            self.set_entry_text(text)

    def trim_all(self):
        """
        Performs both the removal of "music." and the trimming from the
        ampersand (&) to the end of the string on the text in the entry widget.

        :return: None
        """
        self.remove_music()
        self.trim_from_ampersand_symbol()

    def shorten_and_copy(self):
        """
        Retrieves the text from the entry widget, shortens it using the bit.ly
        API, and sets the entry widget to the shortened URL. Also copies the
        shortened URL to the system clipboard.

        If the shortening process fails, an error message is displayed to the
        user.

        :return: None
        """
        url = self.get_entry_text()
        key = os.getenv('BITLY_API')

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

            messagebox.showinfo("Success", "Short URL copied to clipboard!")

        except Exception as e:
            messagebox.showerror("Shortening Failed", str(e))


if __name__ == "__main__":
    root = tk.Tk()
    app = LinkTrimmerApp(root)
    root.mainloop()
