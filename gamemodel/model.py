# model.py
from assets import content, story


class StoryModel:
    def __init__(self):
        self.erster_prototyp_pfad = content.string_proto_pfad
        self.current_index = 0
        self.chapter = story.chapter

    def get_current_section(self):
        return self.erster_prototyp_pfad[self.current_index]

    def get_story_content(self, section):
        return self.chapter.get(section).get('content')

    def get_option_text(self, section, option):
        return self.chapter.get(section).get('text_options').get(option)

    def get_next_section(self, section, option):
        return self.chapter.get(section).get('options').get(option)

    def advance_section(self, next_section):
        self.erster_prototyp_pfad.insert(self.current_index, next_section)
        self.current_index += 1

    def get_progress(self):
        return round((self.current_index + 1) / len(self.erster_prototyp_pfad) * 100)