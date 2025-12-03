# Sentiment Analysis Chatbot

This project is a simple Python-based chatbot that analyzes user messages and identifies whether the sentiment is **Positive**, **Negative**, or **Neutral** using a keyword-matching approach. It is lightweight, easy to run, and suitable for beginners who want to understand how sentiment detection works without machine learning.

---

## How to Run

1. **Install the required library**

   ```bash
   pip install pandas
   ```

2. **Add the dataset file**

   * Place your **Sentimate_dataset.csv** file in the same directory as the chatbot script.

3. **Run the Python file**

   ```bash
   python chatbot.py
   ```

4. **Start chatting**

   * Type your message in the console.
   * The chatbot will automatically detect the sentiment and give an appropriate reply.

---

## Chosen Technologies

| Technology                      | Purpose                                                              |
| ------------------------------- | -------------------------------------------------------------------- |
| **Python**                      | Main programming language for building the chatbot                   |
| **Pandas**                      | Used for loading and handling the sentiment dataset                  |
| **CSV Dataset**                 | Contains keywords and example sentences for sentiment identification |
| **Simple Text-Based Interface** | Allows direct interaction through the command line                   |

---

## Explanation of Sentiment Logic

The chatbot uses a **moderate and easy-to-understand rule-based system**:

1. The CSV file contains keywords labeled as **positive**, **negative**, or **neutral**.
2. When the user enters a message:

   * The chatbot scans the text for matching keywords.
   * It counts how many times positive, negative, or neutral words appear.
3. The sentiment with the highest match count becomes the detected sentiment.
4. Based on this sentiment:

   * Positive → gives an encouraging or friendly response
   * Negative → gives a calm, supportive, or understanding response
   * Neutral → gives a normal, balanced reply
5. If no keywords are found:

   * The chatbot assumes a **neutral** sentiment and replies normally.

This logic makes the chatbot simple, explainable, and easy to modify without requiring any complex AI or training models.


