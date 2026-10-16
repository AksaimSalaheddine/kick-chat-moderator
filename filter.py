"""Core chat moderation decisions."""

from rule_loader import load_rules
from text_detection import contains_word


class ChatFilter:
    """Evaluate messages against rules loaded from a JSON file."""

    ACTION_PRIORITY = {"warn": 1, "timeout": 2, "ban": 3}
    ACTION_SEVERITY = {"warn": "low", "timeout": "medium", "ban": "high"}

    def __init__(self, rules_path: str = "config/moderation_rules.json") -> None:
        self.rules = load_rules(rules_path)

    def check_message(self, message: str) -> dict:
        """Return a consistent moderation result for a chat message."""
        matches = []

        for action, words in self.rules.items():
            for word in words:
                if contains_word(word, message):
                    matches.append({
                        "word": word,
                        "action": action,
                        "severity": self.ACTION_SEVERITY[action],
                    })

        if not matches:
            return {
                "allowed": True,
                "action": "allow",
                "severity": None,
                "matches": [],
            }

        highest_match = max(
            matches, key=lambda match: self.ACTION_PRIORITY[match["action"]]
        )
        return {
            "allowed": False,
            "action": highest_match["action"],
            "severity": highest_match["severity"],
            "matches": matches,
        }
