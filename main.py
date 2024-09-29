import textwrap
import tkinter as tk
import story as story
import content

class StoryApp:
    def __init__(self):
        self.erster_prototyp_pfad: [] = content.string_proto_pfad
        self.current_index: int = 0
        root.title("Reiter der schwarzen Sonne")
        self.chapter = story.chapter

        self.text_widget = tk.Text(root, height=40, width=50, wrap=tk.WORD)
        self.text_widget.pack()

        self.label_widget = tk.Label(root, height=2, width=50)
        self.label_widget.pack()
        self.option_1_button = tk.Button(root, text="Option1", command=lambda: self.select_option('1'))
        self.option_1_button.pack()
        print('test')
        self.option_2_button = tk.Button(root, text="Option2", command=lambda: self.select_option('2'))
        self.option_2_button.pack()
        self.button = tk.Button(root, text="Display Section", command=self.display_next_section)
        self.button.pack()


    def display_next_section(self):
        if self.current_index < len(self.erster_prototyp_pfad):
            section = self.erster_prototyp_pfad[self.current_index]
            story_value = self.chapter.get(section).get('content')
            wrapped_text = textwrap.fill(story_value, width=50)
            self.text_widget.delete(1.0, tk.END)
            self.text_widget.insert(tk.END, wrapped_text)
            progress_number: int = round((self.current_index+1) / len(self.erster_prototyp_pfad) * 100)
            progress_indicator = f"{progress_number} %"
            self.label_widget.config(text=progress_indicator)
            self.update_option_buttons()
            self.current_index += 1


    def update_option_buttons(self):
        current_section = self.erster_prototyp_pfad[self.current_index]
        option_1_text = self.chapter.get(current_section).get('text_options').get('1')
        option_2_text = self.chapter.get(current_section).get('text_options').get('2')
        self.option_1_button.config(text=option_1_text, command=lambda: self.select_option('1'))
        self.option_2_button.config(text=option_2_text, command=lambda: self.select_option('2'))


    def select_option(self, option):
        current_section = self.erster_prototyp_pfad[self.current_index-1]
        next_section = self.chapter.get(current_section).get('options').get(option)
        self.erster_prototyp_pfad.insert(self.current_index, next_section)
        self.display_next_section()


if __name__ == "__main__":
    root = tk.Tk()
    app = StoryApp()
    root.mainloop()
