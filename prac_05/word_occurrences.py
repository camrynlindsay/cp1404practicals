"""
Word Occurrences
Estimate: 20 minutes
Actual:   32 minutes
"""

word_to_count = {}

text = input("Enter text: ").split()
for word in text:
    if word in word_to_count:
        word_to_count[word] += 1
    else:
        word_to_count[word] = 1
words = list(word_to_count.keys())
words.sort()
max_word_length = max(len(word) for word in word_to_count)
for word in words:
    print(f"{word:{max_word_length}} : {word_to_count[word]}")

