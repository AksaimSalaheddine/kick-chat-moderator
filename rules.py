BANNED_WORDS = {
    "word": "harassment",
    "severity": "high",
    "action": "banned"
}
INSULT_WORDS = {
    "word": "insult",
    "severity": "low",
    "action": "warn"
}
SPAM_WORDS = {
    "word": "spam",
    "severity": "medium",
    "action": "timeout"
}
RULES = [
    BANNED_WORDS,
    INSULT_WORDS,
    SPAM_WORDS
]
SEVERITY_LEVELS = {
    "low": 1,
    "medium": 2,
    "high": 3}