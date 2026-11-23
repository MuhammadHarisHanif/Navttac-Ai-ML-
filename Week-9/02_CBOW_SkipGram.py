
# Muhammad Haris Assignment
# Week 9: CBOW and Skip-Gram Models

# Import required library
from gensim.models import Word2Vec

# Sample training sentences
sentences = [
    ["artificial", "intelligence", "is", "changing", "the", "world"],
    ["machine", "learning", "uses", "data", "to", "learn"],
    ["deep", "learning", "uses", "neural", "networks"],
    ["natural", "language", "processing", "understands", "text"],
    ["computers", "learn", "through", "machine", "learning"],
    ["neural", "networks", "are", "used", "in", "deep", "learning"]
]

# -----------------------------
# 1. CBOW Model
# -----------------------------

cbow_model = Word2Vec(
    sentences=sentences,
    vector_size=50,
    window=2,
    min_count=1,
    workers=1,
    sg=0,
    epochs=100
)

print("CBOW Model")
print("----------")

print("Vocabulary:")
print(cbow_model.wv.index_to_key)

print("\nVector of 'learning':")
print(cbow_model.wv["learning"])

# -----------------------------
# 2. Skip-Gram Model
# -----------------------------

skipgram_model = Word2Vec(
    sentences=sentences,
    vector_size=50,
    window=2,
    min_count=1,
    workers=1,
    sg=1,
    epochs=100
)

print("\nSkip-Gram Model")
print("----------------")

print("Vocabulary:")
print(skipgram_model.wv.index_to_key)

print("\nVector of 'learning':")
print(skipgram_model.wv["learning"])

# Find similar words
print("\nCBOW Similar Words:")
print(cbow_model.wv.most_similar("learning", topn=3))

print("\nSkip-Gram Similar Words:")
print(skipgram_model.wv.most_similar("learning", topn=3))
