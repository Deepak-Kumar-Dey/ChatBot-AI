import pandas as pd
import random


def load_dataset():
    try:
        df = pd.read_csv("Sentimate_dataset.csv")

        print("Loaded columns:", list(df.columns))

        keywords = df["keyword"].dropna().tolist()
        sentiments = df["sentiment"].dropna().tolist()

        positive_keywords = []
        negative_keywords = []

        for kw, sent in zip(keywords, sentiments):
            if sent.lower() == "positive":
                positive_keywords.append(str(kw).lower())
            elif sent.lower() == "negative":
                negative_keywords.append(str(kw).lower())

        return positive_keywords, negative_keywords

    except Exception as e:
        print("Error loading dataset:", e)
        exit()


positive_keywords, negative_keywords = load_dataset()



positive_responses = [
    "That's great! It really sounds like things went well.",
    "Wow, that's amazing! It seems like you're really happy about it.",
    "That's wonderful to hear! Moments like this truly feel good.",
    "Nice! I'm glad things turned out well.",
    "That sounds really positive! Tell me more about it.",
    "That's awesome! I'm happy to hear something good happened."
]

negative_responses = [
    "I'm really sorry you're dealing with this. That sounds difficult.",
    "That must have been upsetting. I'm here for you.",
    "I understand… that sounds tough. What happened exactly?",
    "That seems stressful. Want to talk about what caused it?",
    "Hmm… that doesn’t sound pleasant. How are you feeling now?",
    "That must have hurt emotionally. You can share more if you want."
]

neutral_responses = [
    "Okay, I see. Tell me more about it.",
    "Hmm… interesting. What made you say that?",
    "Alright, sounds normal. Want to explain a bit more?",
    "I get it. How would you like to continue?",
    "Okay… I'm listening. What happened next?",
    "Got it. Thanks for sharing. Want to go deeper?"
]


def detect_sentiment(message):
    msg = message.lower()

    for kw in positive_keywords:
        if kw in msg:
            return "positive"

    for kw in negative_keywords:
        if kw in msg:
            return "negative"

    return "neutral"


def get_response(sentiment, user_message):
    if sentiment == "positive":
        return random.choice(positive_responses)

    if sentiment == "negative":
        return random.choice(negative_responses)

    return random.choice(neutral_responses)


def chatbot():
    print("\nChatbot: Hello! I am your sentiment chatbot")
    print("Type 'exit' anytime to quit.\n")

    while True:
        user_input = input("You: ")

        if user_input.lower() == "exit":
            print("Chatbot: Goodbye! Take care")
            break

        sentiment = detect_sentiment(user_input)
        reply = get_response(sentiment, user_input)

        print(f"Chatbot: {reply}\n")


if __name__ == "__main__":
    chatbot()
