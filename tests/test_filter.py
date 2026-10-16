import pytest
from filter import ChatFilter


def test_message_is_allowed():
    chat_filter = ChatFilter()
    result = chat_filter.check_message("hello everyone")

    assert result == "Allowed"

def test_high_severity_first():
    chat_filter = ChatFilter()
    result = chat_filter.check_message("harassment first hello S-P-A-M and insult")
    assert result != "Allowed"
    assert result["action"] == "ban"


def test_high_severity_last():
    chat_filter = ChatFilter()
    result = chat_filter.check_message("hello S-P-A-M and insult then hara/ssment")
    assert result != "Allowed"
    assert result["action"] == "ban"

@pytest.mark.parametrize("message", [
    "s.p.a.m",
    "s-p-a-m",
    "s p a m",
    "s/p/a/m",
    "s_p_a_m",
    "s@p@a@m",
])
def test_dotted_spam(message):
    chat_filter = ChatFilter()
    result = chat_filter.check_message(message)
    assert result["word"] == "spam"
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



def test_message_matching_is_case_insensitive():
    chat_filter = ChatFilter()
    result = chat_filter.check_message("SPaM")

    assert result["word"] == "spam"
    assert result["action"] == "timeout"



def test_message_matches_configured_phrase():
    chat_filter = ChatFilter()
    result = chat_filter.check_message("please stop spamming")

    assert result["word"] == "stop spamming"
    assert result["action"] == "timeout"



