import re
from collections import Counter

text = "Artificial Intelligence is transforming the world."


text = text.lower()
text = re.sub(r'[^a-z\s]', '', text)
words = text.split()

print("Tokens:", words)


def generate_ngrams(words, n):
    return [tuple(words[i:i+n]) for i in range(len(words)-n+1)]

unigrams = generate_ngrams(words, 1)
bigrams = generate_ngrams(words, 2)
trigrams = generate_ngrams(words, 3)


unigram_counts = Counter(unigrams)
bigram_counts = Counter(bigrams)
trigram_counts = Counter(trigrams)

print("\nUnigrams:", unigram_counts)
print("\nBigrams:", bigram_counts)
print("\nTrigrams:", trigram_counts)


def predict_next_word(word):
    candidates = {pair[1]: count for pair, count in bigram_counts.items() if pair[0] == word}
    if not candidates:
        return "No prediction available"
    return max(candidates, key=candidates.get)

print("\nNext word prediction for 'artificial':", predict_next_word("artificial"))
print("Next word prediction for 'intelligence':", predict_next_word("intelligence"))
print("Next word prediction for 'is':", predict_next_word("is"))