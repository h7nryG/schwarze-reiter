import tkinter as tk
from gamecontroller.controller import StoryController

if __name__ == "__main__":
    root = tk.Tk()
    controller = StoryController(root)
    root.mainloop()


