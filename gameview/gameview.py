# view.py
import tkinter as tk
import textwrap

class StoryView:
    def __init__(self, root, controller):
        """ Initializes the view. """
        self.controller = controller
        root.title("Reiter der schwarzen Sonne")
        root.geometry("600x700")
        # Add a text widget to display the story
        self.text_widget = tk.Text(root, height=40, width=75, wrap=tk.WORD)
        self.text_widget.pack()
        # Add a button to display the next section
        self.display_button = tk.Button(root, text="Display Section", command=self.controller.display_next_section)
        self.display_button.pack()
        # Add a label to display the progress
        self.label_widget = tk.Label(root, height=2, width=50)
        self.label_widget.pack()
        # Add a button to display the next section
        self.option_1_button = tk.Button(root, text="Option1", command=lambda: self.controller.select_option('1'))
        self.option_1_button.pack()
        # Add a button to display the next section
        self.option_2_button = tk.Button(root, text="Option2", command=lambda: self.controller.select_option('2'))
        self.option_2_button.pack()


    def update_text(self, text):
        """ Updates the text displayed in the text widget. """
        wrapped_text = textwrap.fill(text, width=70)
        self.text_widget.delete(1.0, tk.END)
        self.text_widget.insert(tk.END, wrapped_text)

    def update_progress(self, progress):
        """ Updates the progress displayed in the label widget. """
        self.label_widget.config(text=f"{progress} %")

    def update_option_buttons(self, option_1_text, option_2_text):
        """ Updates the text displayed in the option buttons. """
        self.option_1_button.config(text=option_1_text)
        self.option_2_button.config(text=option_2_text)