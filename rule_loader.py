import json

#  Previous code
# def load_rules_1(path):
#     with open(path, "r") as file:
#         data = file.read()
#     moderation_rules = json.loads(data)
#
#     if not isinstance(moderation_rules, dict):
#         raise ValueError("Moderation rules must be a dictionary")
#
#     allowed_severities = {"high", "medium", "low"}
#     allowed_actions = {"warn", "timeout", "banned"}
#
#     for rule in moderation_rules:
#         if not isinstance(rule, dict):
#             raise ValueError("Each moderation rule must be a dictionary")
#
#         required_fields = {"word", "severity", "action"}
#         if not required_fields.issubset(rule):
#             raise ValueError("Each rule must contain word, severity, and action")
#
#         if rule["action"] not in allowed_actions:
#             raise ValueError("Invalid action")
#         if rule["severity"] not in allowed_severities:
#             raise ValueError("Invalid severity")
#
#     return moderation_rules
#  Previous code

def load_rules(path):
    with open(path, "r") as file:
        data = file.read()

    moderation_rules = json.loads(data)

    if not isinstance(moderation_rules, dict):
        raise ValueError("Moderation rules must be a dictionary")

    required_actions = {"ban", "timeout", "warn"}

    if not required_actions.issubset(moderation_rules):
        raise ValueError("Rules must contain ban, timeout, and warn")

    for action, words in moderation_rules.items():
        if action not in required_actions:
            raise ValueError("Invalid moderation action")

        if not isinstance(words, list):
            raise ValueError("Each action must contain a list of words")

        for word in words:
            if not isinstance(word, str) or not word.strip():
                raise ValueError("Each word must be a non-empty string")

    return moderation_rules
