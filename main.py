from filter import ChatFilter
chat_filter = ChatFilter()
print("Kick Chat Moderator is starting...")
msg = input("Enter a message:")
print(chat_filter.check_message(msg))

