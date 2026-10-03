from filter import ChatFilter
chat_filter = ChatFilter()
print("Kick Chat Moderator is starting...")
msg = input("Enter a message:")
result = chat_filter.check_message(msg)
if result != "Allowed":
    severity = result["severity"]
    word = result["word"]
    action = result["action"]
    print("word:", word)
    print("severity:", severity)
    print("action:", action)
else:
    print("Message is allowed")