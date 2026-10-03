from rules import BANNED_WORDS
class ChatFilter:
    def check_message(self, message):
        for word in BANNED_WORDS:
            if word in message:
                return "banned"
        return "unbanned"

# Test
# print(chat_filter.check_message(input("Enter a message: ")))