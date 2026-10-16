"""Load and validate JSON moderation rules."""

import json
from pathlib import Path


def load_rules(path: str) -> dict[str, list[str]]:
    """Load and validate moderation rules from ``path``."""
    with Path(path).open(encoding="utf-8") as file:
        moderation_rules = json.load(file)

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
