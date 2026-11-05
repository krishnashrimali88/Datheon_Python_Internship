import json
import re

EXIT_WORDS = {"bye", "exit", "quit"}
STOPWORDS = {"a", "the", "is", "are", "do", "i", "my", "you", "your",
             "what", "when", "how", "will", "of", "to", "can", "we"}


def normalize(text):
  
    return re.findall(r"[a-z0-9]+", text.lower().strip())


def keywords(text):
    return {w for w in normalize(text) if w not in STOPWORDS}


with open("Faq.json", encoding="utf-8") as f:
    data = json.load(f)

state = "greeting"
print("Assistant: Welcome! Ask me about hours, project submission or certificates.")

while state != "exit":
    user = input("\nYou: ")
    words = normalize(user)
    sentence = " ".join(words)

    if not words:
        print("Assistant: Please type something.")
        continue


    if set(words) & EXIT_WORDS and len(words) <= 3:
        print("Assistant: Goodbye!")
        state = "exit"
        continue

   
    best = max(data["faqs"], key=lambda faq: len(keywords(user) & keywords(faq["question"])))
    matches = len(keywords(user) & keywords(best["question"]))

    if matches > 0:
        print(f"Assistant: {best['answer']}")
        state = "helping"
    elif any(f" {g} " in f" {sentence} " for g in data["greetings"]):
        print("Assistant: Hello! How can I help you?")
        state = "helping"
    else:
        print("Assistant: Sorry, I didn't understand. You can ask about:")
        for faq in data["faqs"]:
            print(f"  - {faq['question']}")
