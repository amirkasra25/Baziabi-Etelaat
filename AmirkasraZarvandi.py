STOP_WORDS = {"a", "an", "and", "are", "as", "at", "be", "but", "by", "for", "he", "in", "is", "it",
              "me", "my", "of", "on", "or", "she", "that", "the", "this", "to", "was", "with", "your"}

SUFFIXES = ["ization", "izes", "ized", "ize", "ing", "ed", "ly", "es", "s"]

TEXTS = {
    "1": "Friends, Romans, countrymen, lend me your ears;",
    "2": "John's new U.S.A. laptop is a state-of-the-art device. The price is high, but the quality is amazing!",
    "3": "The authorization for this authorized project is pending. He authorizes the payments regularly.",
}

def stem(word):
    if "-" in word:
        return word
    for suffix in SUFFIXES:
        if word.endswith(suffix) and len(word) - len(suffix) >= 3:
            return word[:-len(suffix)]
    return word


def preprocess(text):
    terms = []
    for word in text.split():
        word = word.strip(",.;!?").replace(".", "").lower()
        if word.endswith("'s") or word.endswith("’s"):
            word = word[:-2]
        if word not in STOP_WORDS:
            terms.append(stem(word))
    return terms


choice = input("Enter 1, 2 or 3 for a sample text, or type your own text: ")
text = TEXTS.get(choice, choice)

output = preprocess(text)
gold = preprocess(text)
o, g = set(output), set(gold)

print("Text:", text)
print("Output:", output)
print("Gold:", gold)
print("Precision:", len(o & g) / len(o) if o else 0)
print("Recall:", len(o & g) / len(g) if g else 0)
print("Extra:", o - g)
print("Missed:", g - o)
