import pytest
from filter import ChatFilter


def test_message_is_allowed():
    chat_filter = ChatFilter()
    result = chat_filter.check_message("hello everyone")

    assert result == "Allowed"

def test_message_is_not_allowed():
    chat_filter = ChatFilter()
    result = chat_filter.check_message("S-P-A-M and HARASS-MENT and insult")
    assert result != "Allowed"
    assert result["severity"] == "high"
    assert result["action"] == "banned"

@pytest.mark.parametrize("message", [
    "s.p.a.m",
    "s-p-a-m",
    "s p a m",
])
def test_dotted_spam(message):
    chat_filter = ChatFilter()
    result = chat_filter.check_message(message)
    assert result["word"] == "spam"
    assert result["severity"] == "medium"
    assert result["action"] == "timeout"

@pytest.mark.parametrize("message, expected", [
    ("hello everyone", "Allowed"),
    ("spamming", "Allowed"),
    ("newspam", "Allowed"),
    ("insulting", "Allowed"),
])
def test_message(message, expected):
    chat_filter = ChatFilter()
    result = chat_filter.check_message(message)
    assert result == expected

