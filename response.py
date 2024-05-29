from random import choice,randint

def get_response(user_input: str) -> str:
    lowered: str = user_input.lower()

    if lowered == "":
        return "Well, you're awfully silent..."
    elif "hello" in lowered:
        return "Hello there! How can I assist you with tech today?"
    elif "python" in lowered:
        return "Python is a versatile programming language used in web development, data science, artificial intelligence, and more. Do you need help with Python?"
    elif "javascript" in lowered:
        return "JavaScript is a programming language commonly used for web development. What specifically would you like to know about JavaScript?"
    elif "machine learning" in lowered or "ai" in lowered:
        return "Machine learning and artificial intelligence are fascinating fields! What aspect of ML or AI are you interested in?"
    elif "roll dice" in lowered:
        return f"You rolled:{randint(1,6)}"
    elif "discord" in lowered:
        return "Discord is a popular platform for communication among gamers and communities. How can I assist you with Discord?"
    else:
        return choice(["I'm sorry, I'm not sure how to respond to that. Let's chat about tech! What else would you like to know?","Do mind rephrasing that again","I am at the starting stage still needs some AI brain in me, help me Gnanendra"])

