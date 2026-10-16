"""Regex-based detection for words and lightly obfuscated phrases."""

import re


def build_pattern(word: str) -> str:
    """Build a word-boundary pattern that permits separators between letters."""
    characters = r"[^a-zA-Z]*".join(re.escape(char) for char in word)
    return rf"\b{characters}\b"


def contains_word(word: str, message: str) -> bool:
    """Return whether ``message`` contains ``word``, ignoring case."""
    return re.search(build_pattern(word), message, re.IGNORECASE) is not None
