from filter import ChatFilter
def main():
    chat_filter = ChatFilter()
    print("Kick Chat Moderator is starting...")
    while True:
        msg = input("Enter a message:")
        if msg == "exit":
            break
        result = chat_filter.check_message(msg)
        if result != "Allowed":
            word = result["word"]
            action = result["action"]
            print("word:", word)
            print("action:", action)
        else:
            print("Message is allowed")
if __name__ == "__main__":
    main()