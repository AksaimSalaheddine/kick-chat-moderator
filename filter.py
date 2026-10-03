from rules import *
class ChatFilter:
    def check_message(self, message):
        highest_rule = {}
        highest_level = 0
        for rule in RULES:
            word = rule["word"]
            if word in message:
                current_level = SEVERITY_LEVELS[rule["severity"]]
                if current_level > highest_level:
                    highest_level = current_level
                    highest_rule = rule
        if highest_rule != {}:
            return highest_rule
        else:
            return "Allowed"