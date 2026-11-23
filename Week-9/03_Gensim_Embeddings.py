
# Muhammad Haris Assignment
# Week 9: Custom Word Embeddings using Gensim

# Import required libraries
import re
from gensim.models import Word2Vec

# Custom text dataset
documents = [
    "artificial intelligence is transforming technology",
    "machine learning helps computers learn from data",
    "deep learning uses artificial neural networks",
    "natural language processing works with human language",
    "data science uses statistics and machine learning",
    "neural networks are important in deep learning",
    "artificial intelligence is used in robotics",
    "machine learning is useful for prediction",
    "computers process information using algorithms",
    "word embeddings convert words into numerical vectors"
]

# 1. Text preprocessing
tokenized_sentences = []

for sentence in documents:
    sentence = sentence.lower()
    sentence = re.sub(r"[^a-z\s]", "", sentence)

    words = sentence.split()
    tokenized_sentences.append(words)

# 2. Train custom Word2Vec model
model = Word2Vec(
    sentences=tokenized_sentences,
    vector_size=100,
    window=3,
    min_count=1,
    workers=1,
    sg=1,
    epochs=100
)

# 3. Display vocabulary
print("Custom Word Embeddings")
print("----------------------")

print("\nVocabulary:")
print(model.wv.index_to_key)

# 4. Generate word vector
word = "learning"

print("\nVector Representation of:", word)
print(model.wv[word])

# 5. Find similar words
print("\nWords Similar to 'learning':")

for similar_word, score in model.wv.most_similar(word, topn=3):
    print(similar_word, ":", score)

# 6. Save trained model
model.save("custom_word2vec.model")

print("\nModel saved successfully!")

# 7. Load saved model
loaded_model = Word2Vec.load("custom_word2vec.model")

print("\nLoaded Model Vocabulary:")
print(loaded_model.wv.index_to_key)

# 8. Check embedding dimensions
print("\nEmbedding Dimensions:")
print(loaded_model.wv.vector_size)
