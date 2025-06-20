def chatbot():
    print("\n" + "=" * 50)
    print("🤖✨  W E L C O M E   T O   C H A T B O T ✨🤖")
    print("=" * 50)
    print("💬 Talk to me! I'm here to chat with you.")
    print("📌 Try typing: 'hello', 'how are you', 'what is your name', 'bye'")
    print("-" * 65 + "\n")

    while True:
        user_input = input("👤 You: ").lower()

        if user_input == "hello":
            print("🤖 Bot: Hi there! 👋")
        elif user_input == "how are you":
            print("🤖 Bot: I'm doing great, thanks for asking! 😊")
        elif user_input == "what is your name":
            print("🤖 Bot: I'm your friendly chatbot! 🤖")
        elif user_input == "bye":
            print("🤖 Bot: Goodbye! Have a nice day! 👋")
            print("\n" + "=" * 50)
            print("🌟 Chatbot session ended. Come back soon! 🌟")
            print("=" * 50 + "\n")
            break
        else:
            print("🤖 Bot: Hmm... I didn't quite get that. 🤔")

chatbot()