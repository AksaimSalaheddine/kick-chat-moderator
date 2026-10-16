"""Command-line entry point for the chat moderator."""

from filter import ChatFilter


def main():
    """Read messages until the user enters ``exit``."""
    chat_filter = ChatFilter()
    print("Kick Chat Moderator is starting...")
    while True:
        msg = input("Enter a message:")
        if msg == "exit":
            break
        result = chat_filter.check_message(msg)
        if result["allowed"]:
            print("Message is allowed")
        else:
            print("action:", result["action"])
            print("severity:", result["severity"])
            for match in result["matches"]:
                print("word:", match["word"])
if __name__ == "__main__":
    main()
