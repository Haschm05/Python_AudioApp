"""
AudioApp
This app will enable the user to listen to theri own audio files
without sacrificing the functionality of an app like spotify.

Developer: Hayden Schmidt
Last update: October, 29, 2026

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
from tkinter import *
from tkinter.ttk import Frame
#import beets
import os

class Interface:
    def __init__(self):
        # tkinter interface
        self.root = tk.Tk()
        self.root.title("AudioApp")
        self.root.geometry('350x200')

    def play_pause_button(self):
        # gui button (to play audio files)
        self.play_pause_button = tk.Button(self.root, text="Play/Pause", command=self.play_pause_file)
        self.play_pause_button.grid()

    def next_button(self):
        # gui button (to play the next audio file)
        self.next_button = tk.Button(self.root, text="Next", command=self.play_next_file)
        self.next_button.grid()

    def prev_button(self):
        # a gui button (to play the previous audio file)
        self.prev_button = tk.Button(self.root, text="Prev", command=self.play_prev_file)
        self.prev_button.grid()

    def contents_display_button(self, display_file_path):
        pass

    def play_pause_file(self):
        # logic to play the selected audio file
        pass

    def play_next_file(self):
        # logic to play the next audio file
        pass

    def play_prev_file(self):
        # logic to play the previous audio file
        pass

    def display_file_contents(self):
        # logic to display the contents of the selected audio file
        output = FilePath("music_testing").display_file_contents()
        lbl = tk.Label(self.root, text=output)
        lbl.grid()

    def scroll_window(self):
        # Create Canvas and Scrollbar
        canvas = Canvas(self.root)
        scrollbar = Scrollbar(self.root, orient=VERTICAL, command=canvas.yview)
        canvas.configure(yscrollcommand=scrollbar.set)

        scrollbar.pack(side=RIGHT, fill=Y)
        canvas.pack(side=LEFT, fill=BOTH, expand=True)

        # Add Frame Inside Canvas
        scrollable_frame = Frame(canvas)
        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")

    # Bind Scroll Events
    def on_frame_configure(event):
        canvas.configure(scrollregion=canvas.bbox("all"))

        scrollable_frame.bind("<Configure>", on_frame_configure)

    # Add Widgets to Scrollable Frame
    for i in range(20):
        Label(scrollable_frame, text=f"Item {i+1}").pack(pady=5)
        root.mainloop()

    def button_grid(self):

        btn = tk.Button(self.root, text="Play/Pause", width=5, height=2, padx=1, pady=1, bg="lightblue", command=self.play_pause_file)
        btn.grid(column=0, row=0)

        btn = tk.Button(self.root, text="Next", width=5, height=2, padx=1, pady=1, bg="lightblue", command=self.play_next_file)
        btn.grid(column=1, row=0)

        btn = tk.Button(self.root, text="Prev", width=5, height=2, padx=1, pady=1, bg="lightblue", command=self.play_prev_file)
        btn.grid(column=2, row=0)

        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_columnconfigure(0, weight=1)
        self.root.grid_columnconfigure(1, weight=1)
        self.root.grid_columnconfigure(2, weight=1)
        self.root.grid_columnconfigure(3, weight=1)

class FilePath:
    def __init__(self, file_path):
        self.file_path = file_path

    def get_file_path(self):
        directory = "music_testing"
        parent_dir = "C:\\Users\\Hayde\\OneDrive\\Documents"
        path = os.path.join(parent_dir, directory)
        return path

    def display_file_contents(self):
        file_path = self.get_file_path()
        for file_name in os.listdir(file_path):
            print(file_name)
        return "\n".join(os.listdir(file_path))

def main():
    app = Interface()
    app.button_grid()
    app.root.mainloop()

if __name__ == "__main__":
    main()
