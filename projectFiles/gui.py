"""
AudioApp
This app will enable the user to listen to theri own audio files
without sacrificing the functionality of an app like spotify.

Developer: Hayden Schmidt
Last update: September, 8, 2026

To-do list:
 - Get GUI working
 - Code upload function
 - Code play function
 - Set up main project structure
 - Troubleshoot
 - Set up file management
 - Add functionality
 - Deploy as application
 - Update as needed
"""

import tkinter as tk
import os

class Interface(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Audio App")
        self.geometry("300x200")

        # Add a label
        label = tk.Label(self, text="Hello, GUI!", font=("Arial", 16))
        label.pack(pady=20)

        # Add a button
        btn = tk.Button(self, text="Click Me", command=self.on_click)
        btn.pack()

    def on_click(self):

        print("Button clicked!")


if __name__ == "__main__":
    app = Interface()
    app.mainloop()

