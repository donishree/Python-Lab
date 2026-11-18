"""
Program 3(c) - Lab Exercise 3 – Frequency counter using dictionaries
Source: Python Lab Report
"""

# Lab Exercise 3: Frequency counter using dictionaries

text = input("Enter a sentence: ").lower()

# Word frequency
word_freq = {}
for word in text.split():
    word = word.strip(".,!?;:")          # remove punctuation
    if word:
        word_freq[word] = word_freq.get(word, 0) + 1

print("\nWord frequency:")
ranked = sorted(word_freq.items(), key=lambda x: x[1], reverse=True)
for word, count in ranked:
    print(f"  {word:<12}: {count}")

# Character (letter) frequency
char_freq = {}
for ch in text:
    if ch.isalpha():
        char_freq[ch] = char_freq.get(ch, 0) + 1

print("\nLetter frequency:")
for ch in sorted(char_freq):
    print(f"  {ch} : {'*' * char_freq[ch]} ({char_freq[ch]})")

if word_freq:
    most_common = max(word_freq, key=word_freq.get)
    print(f"\nMost frequent: {most_common} ({word_freq[most_common]})")
    print("Unique words:", len(set(word_freq)))
