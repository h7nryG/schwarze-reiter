from gamemodel.model import StoryModel
from gameview.gameview import StoryView

class StoryController:
    def __init__(self, root):
        """ Initializes the controller. """
        self.model = StoryModel()
        self.view = StoryView(root, self)


    def display_next_section(self):
        """ Displays the next section of the story. """
        if self.model.current_index < len(self.model.erster_prototyp_pfad):
            section = self.model.get_current_section()
            story_value = self.model.get_story_content(section)
            self.view.update_text(story_value)
            progress = self.model.get_progress()
            self.view.update_progress(progress)
            self.update_option_buttons()
            self.model.current_index += 1


    def update_option_buttons(self):
        """ Updates the text of the option buttons. """
        current_section = self.model.get_current_section()
        option_1_text = self.model.get_option_text(current_section, '1')
        option_2_text = self.model.get_option_text(current_section, '2')
        self.view.update_option_buttons(option_1_text, option_2_text)


    def select_option(self, option):
        """ Selects an option and advances the story. """
        current_section = self.model.erster_prototyp_pfad[self.model.current_index - 1]
        next_section = self.model.get_next_section(current_section, option)
        self.model.advance_section(next_section)
        self.display_next_section()