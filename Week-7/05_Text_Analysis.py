
# Muhammad Haris Assignment
# Task 62: Text Analysis

# Import required libraries
import re
from collections import Counter

# Sample text
text = """
Artificial Intelligence is transforming technology.
Machine Learning is a part of Artificial Intelligence.
Natural Language Processing helps computers understand human language.
Machine Learning and Deep Learning are important AI technologies.
"""

# 1. Convert text to lowercase
text = text.lower()

# 2. Remove punctuation and special characters
clean_text = re.sub(r"[^a-z\s]", "", text)

# 3. Split text into words
words = clean_text.split()

# 4. Count total words
total_words = len(words)

# 5. Count unique words
unique_words = len(set(words))

# 6. Calculate word frequency
word_frequency = Counter(words)

# 7. Display most common words
most_common = word_frequency.most_common(5)

# Display results
print("Text Analysis Results")
print("---------------------")

print("Total Words:", total_words)
print("Unique Words:", unique_words)

print("\nWord Frequency:")
for word, frequency in word_frequency.items():
    print(word, ":", frequency)

print("\nTop 5 Most Common Words:")
for word, frequency in most_common:
    print(word, ":", frequency)
