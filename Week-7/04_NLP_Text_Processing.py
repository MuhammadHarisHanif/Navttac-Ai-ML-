
# Muhammad Haris Assignment
# Tasks 60 and 61: NLP and Text Processing

# Import required libraries
import re
import nltk

from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer, WordNetLemmatizer
from nltk import pos_tag

# Download required NLTK resources
nltk.download("punkt")
nltk.download("punkt_tab")
nltk.download("stopwords")
nltk.download("wordnet")
nltk.download("averaged_perceptron_tagger_eng")

# Sample text
text = """
Artificial Intelligence is changing the world.
Machine Learning helps computers learn from data.
Natural Language Processing allows computers to understand human language.
"""

# 1. Text Cleaning
clean_text = re.sub(r"[^a-zA-Z\s]", "", text.lower())

print("Original Text:")
print(text)

print("\nCleaned Text:")
print(clean_text)

# 2. Sentence Tokenization
sentences = sent_tokenize(text)

print("\nSentence Tokenization:")
print(sentences)

# 3. Word Tokenization
words = word_tokenize(clean_text)

print("\nWord Tokenization:")
print(words)

# 4. Stop Word Removal
stop_words = set(stopwords.words("english"))

filtered_words = [
    word for word in words if word not in stop_words
]

print("\nAfter Stop Word Removal:")
print(filtered_words)

# 5. Stemming
stemmer = PorterStemmer()

stemmed_words = [
    stemmer.stem(word) for word in filtered_words
]

print("\nStemming:")
print(stemmed_words)

# 6. Lemmatization
lemmatizer = WordNetLemmatizer()

lemmatized_words = [
    lemmatizer.lemmatize(word) for word in filtered_words
]

print("\nLemmatization:")
print(lemmatized_words)

# 7. Part of Speech Tagging
pos_tags = pos_tag(words)

print("\nPart of Speech Tagging:")
print(pos_tags)
