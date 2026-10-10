import re
def build_pattern(word):
    pattern = ""
    for index, char in enumerate(word):
        if index != len(word) - 1:
            pattern += re.escape(char)
            pattern += "[ .-]*"
        else :
            pattern += re.escape(char)
    pattern = rf"\b{pattern}\b"
    return pattern

def contains_word(word, message):
    pattern = build_pattern(word)
    result = re.search(pattern, message, re.IGNORECASE)
    return result is not None