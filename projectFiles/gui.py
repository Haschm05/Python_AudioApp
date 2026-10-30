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
#import beets
import os

class Interface:
    def __init__(self):
        # tkinter interface
        self.root = tk.Tk()
        self.root.title("AudioApp")
        self.root.geometry('350x200')

    def play_button(self):
        # gui button (to play audio files)
        self.play_button = tk.Button(self.root, text="Play", command=self.play_file)
        self.play_button.pack()

    def next_button(self):
        # gui button (to play the next audio file)
        self.next_button = tk.Button(self.root, text="Next", command=self.play_next_file)
        self.next_button.pack()

    def prev_button(self):
        # a gui button (to play the previous audio file)
        self.prev_button = tk.Button(self.root, text="Prev", command=self.play_prev_file)
        self.prev_button.pack()

    def contents_display_button(self, display_file_path):
        self.contents_display_button = tk.Button(self.root, text="Contents", command=self.display_file_contents)
        self.contents_display_button.pack()

    def play_file(self):
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
        lbl.pack()


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
    app.play_button()
    app.next_button()
    app.prev_button()
    app.contents_display_button(FilePath("music_testing").display_file_contents)
    app.root.mainloop()

if __name__ == "__main__":
    main()

