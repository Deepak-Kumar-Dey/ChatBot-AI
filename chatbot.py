import pandas as pd
import random
import re


def load_dataset(path="Sentimate_dataset.csv"):
    try:
        df = pd.read_csv(path)
        print("Loaded columns:", list(df.columns))

        
        pos = []
        neg = []
        neu = []
        for _, row in df.iterrows():
            kw = str(row["keyword"]).strip().lower()
            s = str(row["sentiment"]).strip().lower()
            if s == "positive":
                pos.append(kw)
            elif s == "negative":
                neg.append(kw)
            else:
                neu.append(kw)
        return pos, neg, neu
    except Exception as e:
        print("Error loading dataset:", e)
        raise

positive_keywords, negative_keywords, neutral_keywords = load_dataset()



positive_responses = [
    "That's great to hear! Sounds like things went well.",
    "Awesome! I'm glad you're feeling good about it.",
    "Nice! That really sounds positive.",
    "Wow! That's really wonderful.",
    "Happy to hear that! Tell me more.",
]

negative_responses = [
    "I'm sorry you're feeling this way. That sounds tough.",
    "That must have been disappointing. I'm here for you.",
    "I understand… that doesn't sound good. Want to talk about it?",
    "Hmm… that seems upsetting. What exactly happened?",
    "That sounds difficult. I'm listening if you want to share more.",
]

neutral_responses = [
    "Okay, I see. Tell me more.",
    "Interesting… what makes you say that?",
    "Alright. Would you like to explain a bit more?",
    "Got it. I'm listening.",
    "Okay. What happened next?",
]



negation_regex = re.compile(
    r"\b(not|no|never|n't|dont|don't|didnt|didn't|cannot|can't|cant|never|hardly|barely|without)\b",
    flags=re.IGNORECASE
)

def word_match(text, phrase):
    """
    Word-boundary match for phrase in text (phrase may be multiple words).
    """
    pattern = r"\b" + re.escape(phrase) + r"\b"
    return re.search(pattern, text) is not None

def has_negation_before(text, match_span, window_words=3):
    """
    Check if any negation word appears within `window_words` before the matched phrase.
    match_span is (start, end) index of the phrase in text.
    """
    start_idx = match_span[0]
   
    before = text[max(0, start_idx - 200): start_idx]
   
    tokens = re.findall(r"\w+|[^\w\s]", before.lower())
    
    words = [t for t in tokens if re.match(r"\w+", t)]
    tail = words[-window_words:] if words else []
 
    for w in tail:
        if negation_regex.match(w):
            return True

   
    explicit_pattern = re.compile(r"(not|no|never|n't|don't|didn't|didnt|cant|can't|cannot|hardly|barely)\s+$", flags=re.IGNORECASE)
    if explicit_pattern.search(before):
        return True

    return False

def find_phrase_spans(text, phrase):
    """Return list of (start,end) spans where phrase (whole-phrase) occurs in text."""
    pattern = re.compile(r"\b" + re.escape(phrase) + r"\b", flags=re.IGNORECASE)
    return [m.span() for m in pattern.finditer(text)]



def detect_sentiment(message):
    msg = message.strip().lower()

  
    for kw in negative_keywords:
        if word_match(msg, kw):
            return "negative"


    for kw in positive_keywords:
        spans = find_phrase_spans(msg, kw)
        if spans:
            
            for span in spans:
                if has_negation_before(msg, span, window_words=3):
                    return "negative"
           
            return "positive"

  
    for kw in neutral_keywords:
        if word_match(msg, kw):
            return "neutral"

   
    for kw in negative_keywords:
        if kw in msg:
            return "negative"
    for kw in positive_keywords:
       
        if kw in msg:
           
            i = msg.find(kw)
            if i != -1:
                if has_negation_before(msg, (i, i+len(kw)), window_words=3):
                    return "negative"
                return "positive"

  
    return "neutral"


def get_response(sentiment):
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
        reply = get_response(sentiment)

        print(f"Chatbot: {reply}\n")


if __name__ == "__main__":
    chatbot()
