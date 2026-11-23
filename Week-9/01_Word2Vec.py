
# Muhammad Haris Assignment
# Week 9: Word2Vec Demonstration

# Import required libraries
from gensim.models import Word2Vec
from nltk.tokenize import word_tokenize
import nltk

# Download tokenizer resource
nltk.download("punkt")
nltk.download("punkt_tab")

# Sample training sentences
sentences = [
    "artificial intelligence is changing the world",
    "machine learning is a part of artificial intelligence",
    "deep learning uses neural networks",
    "natural language processing understands human language",
    "word embeddings represent words as numerical vectors",
    "machine learning helps computers learn from data",
    "neural networks are used in deep learning"
]

# Tokenize sentences
tokenized_sentences = [
    word_tokenize(sentence.lower()) for sentence in sentences
]

# Train Word2Vec model
model = Word2Vec(
    sentences=tokenized_sentences,
    vector_size=50,
    window=3,
    min_count=1,
    workers=1,
    sg=1,
    epochs=100
)

# Display vocabulary
print("Word2Vec Vocabulary:")
print(model.wv.index_to_key)

# Display vector of a word
word = "learning"

print("\nVector Representation of:", word)
print(model.wv[word])

# Find similar words
print("\nWords Similar to 'learning':")

for similar_word, score in model.wv.most_similar("learning", topn=3):
    print(similar_word, ":", score)
