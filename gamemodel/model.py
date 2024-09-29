# model.py
from assets import content, story


class StoryModel:
    def __init__(self):
        """ Initializes the model. """
        self.erster_prototyp_pfad = content.string_proto_pfad
        self.current_index = 0
        self.chapter = story.chapter

    def get_current_section(self):
        """ Returns the current section of the story. """
        return self.erster_prototyp_pfad[self.current_index]

    def get_story_content(self, section):
        """ Returns the content of a section. """
        return self.chapter.get(section).get('content')

    def get_option_text(self, section, option):
        """ Returns the text of an option. """
        return self.chapter.get(section).get('text_options').get(option)

    def get_next_section(self, section, option):
        """ Returns the next section of the story. """
        return self.chapter.get(section).get('options').get(option)

    def advance_section(self, next_section):
        """ Advances the story to the next section. """
        self.erster_prototyp_pfad.insert(self.current_index, next_section)
        self.current_index += 1

    def get_progress(self):
        """ Returns the progress of the story. """
        return round((self.current_index + 1) / len(self.erster_prototyp_pfad) * 100)