# view.py
import tkinter as tk
import textwrap

class StoryView:
    def __init__(self, root, controller):
        self.controller = controller
        root.title("Reiter der schwarzen Sonne")

        self.text_widget = tk.Text(root, height=40, width=50, wrap=tk.WORD)
        self.text_widget.pack()

        self.label_widget = tk.Label(root, height=2, width=50)
        self.label_widget.pack()

        self.option_1_button = tk.Button(root, text="Option1", command=lambda: self.controller.select_option('1'))
        self.option_1_button.pack()

        self.option_2_button = tk.Button(root, text="Option2", command=lambda: self.controller.select_option('2'))
        self.option_2_button.pack()

        self.display_button = tk.Button(root, text="Display Section", command=self.controller.display_next_section)
        self.display_button.pack()

    def update_text(self, text):
        wrapped_text = textwrap.fill(text, width=50)
        self.text_widget.delete(1.0, tk.END)
        self.text_widget.insert(tk.END, wrapped_text)

    def update_progress(self, progress):
        self.label_widget.config(text=f"{progress} %")

    def update_option_buttons(self, option_1_text, option_2_text):
        self.option_1_button.config(text=option_1_text)
        self.option_2_button.config(text=option_2_text)