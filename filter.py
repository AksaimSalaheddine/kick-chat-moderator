from text_detection import contains_word
from rules import *
class ChatFilter:
    def check_message(self, message):
        highest_level = 0
        highest_rule = {}
        for rule in RULES:
            word = rule["word"]
            if contains_word(word, message):
                current_level = SEVERITY_LEVELS[rule["severity"]]
                if current_level > highest_level:
                    highest_level = current_level
                    highest_rule = rule
        if highest_rule == {}:
            return "Allowed"
        else:
            return highest_rule