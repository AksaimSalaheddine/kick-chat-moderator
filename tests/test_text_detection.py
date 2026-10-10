import pytest
from text_detection import contains_word

def test_words_hyphen():
    result = contains_word("spam", "s-p-a-m")
    assert result

def test_contains_word_not_found():
    result = contains_word("spam", "hello everyone")
    assert not result
@pytest.mark.parametrize("word, message" , [
    ("spam","newspam"),
    ("spam", "spamming"),
])
def test_contains_word_inside_longer_word(word, message):
    result = contains_word(word, message)
    assert not result