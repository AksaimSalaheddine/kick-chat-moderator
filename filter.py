from text_detection import contains_word
from rule_loader import load_rules

# Previous code
# Previous code
# class ChatFilter:
#     def check_message(self, message):
#         highest_level = 0
#         highest_rule = {}
#         for rule in RULES:
#             word = rule["word"]
#             if contains_word(word, message):
#                 current_level = SEVERITY_LEVELS[rule["severity"]]
#                 if current_level > highest_level:
#                     highest_level = current_level
#                     highest_rule = rule
#         if highest_rule == {}:
#             return "Allowed"
#         else:
#             return highest_rule
# Previous code


# class ChatFilter:
#     def __init__(self, rules_path="config/moderation_rules.json"):
#         self.rules = load_rules(rules_path)
#
#     def check_message(self, message):
#         action_priority = {
#             "warn": 1,
#             "timeout": 2,
#             "ban": 3
#         }
#
#         highest_priority = 0
#         highest_rule = {}
#
#         for action, words in self.rules.items():
#             for word in words:
#                 if contains_word(word, message):
#                     current_priority = action_priority[action]
#
#                     if current_priority > highest_priority:
#                         highest_priority = current_priority
#                         highest_rule = {
#                             "word": word,
#                             "action": action
#                         }
#
#         if highest_rule == {}:
#             return "Allowed"
#
#         return highest_rule
#  Previous code



class ChatFilter:
    def __init__(self, rules_path="config/moderation_rules.json"):
        self.rules = load_rules(rules_path)

    def check_message(self, message):
        action_priority = {
            "warn": 1,
            "timeout": 2,
            "ban": 3
        }

        highest_priority = 0
        highest_rule = {}

        for action, words in self.rules.items():
            for word in words:
                if contains_word(word, message):
                    current_priority = action_priority[action]

                    if current_priority > highest_priority:
                        highest_priority = current_priority
                        highest_rule = {
                            "word": word,
                            "action": action
                        }

        if highest_rule == {}:
            return "Allowed"

        return highest_rule
