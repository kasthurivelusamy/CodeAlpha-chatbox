"""
CodeAlpha - Python Programming Internship
TASK 4: Basic Chatbot

A simple rule-based chatbot that responds to predefined user inputs.
Key Concepts Used: if-elif, functions, loops, input/output.
"""

import random

# Predefined responses. Each key can have multiple possible replies for variety.
RESPONSES = {
    "hello": ["Hi!", "Hello there!", "Hey! Nice to see you."],
    "hi": ["Hi!", "Hello there!"],
    "how are you": ["I'm fine, thanks! How about you?", "Doing great, thanks for asking!"],
    "what is your name": ["I'm a simple Python chatbot built for the CodeAlpha internship."],
    "what can you do": ["I can chat with you about a few basic things. Try saying 'hello', 'how are you', or 'bye'."],
    "thank you": ["You're welcome!", "No problem at all!"],
    "thanks": ["You're welcome!", "Anytime!"],
    "bye": ["Goodbye! Have a great day!", "Bye! Take care."],
    "goodbye": ["Goodbye! Have a great day!", "See you later!"],
}

DEFAULT_RESPONSES = [
    "Sorry, I didn't understand that. Could you rephrase?",
    "I'm not sure how to respond to that yet.",
    "Hmm, I don't know that one. Try 'hello' or 'how are you'.",
]

EXIT_KEYWORDS = {"bye", "goodbye", "exit", "quit"}


def get_response(user_input):
    """Return a chatbot response based on simple keyword matching."""
    text = user_input.lower().strip().strip("!?.")

    for keyword, replies in RESPONSES.items():
        if keyword in text:
            return random.choice(replies)

    return random.choice(DEFAULT_RESPONSES)


def is_exit_command(user_input):
    text = user_input.lower().strip().strip("!?.")
    return any(word in text for word in EXIT_KEYWORDS)


def chat():
    print("=" * 40)
    print("  SIMPLE RULE-BASED CHATBOT")
    print("=" * 40)
    print("Type 'bye' or 'exit' to end the conversation.\n")

    while True:
        user_input = input("You: ").strip()

        if not user_input:
            print("Bot: Please type something.")
            continue

        response = get_response(user_input)
        print(f"Bot: {response}")

        if is_exit_command(user_input):
            break


if __name__ == "__main__":
    chat()
