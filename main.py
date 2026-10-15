from filter import ChatFilter
chat_filter = ChatFilter()
print("Kick Chat Moderator is starting...")
msg = input("Enter a message:")
result = chat_filter.check_message(msg)
if result != "Allowed":
    word = result["word"]
    action = result["action"]
    print("word:", word)
    print("action:", action)
else:
    print("Message is allowed")