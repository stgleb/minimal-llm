import numpy as np
import random

# Sample text data
data = """
Astronomy, the scientific study of celestial objects, space, and the universe as a whole,
has fascinated humanity for centuries. From ancient civilizations observing the night sky
to modern astrophysics and space exploration, the field of astronomy continues to evolve,
revealing the wonders of the universe and our place within it.
"""

# Step 1: Tokenize the text
def tokenize(text):
    return text.lower().split()


# Step 2: Create embeddings (using one-hot encoding for simplicity)
def create_embeddings(tokens, vocab_size):
    embeddings = np.zeros((len(tokens), vocab_size))
    for i, token in enumerate(tokens):
        embeddings[i][word_to_index[token]] = 1
    return embeddings

# Step 3: Define a simple training function (dummy example)
def train_model(embeddings, epochs=50):
    for epoch in range(epochs):
        index = random.randint(0, len(embeddings) - 1)
        print(f"Epoch {epoch + 1}: Training on word '{tokens[index]}' with one-hot vector:", embeddings[index])

# Step 5: Sample inference function (predicting next word)
def predict_next_word(current_word):
    index = word_to_index[current_word]
    print(f"Predicted next word after '{current_word}': {index_to_word[(index + 1) % len(vocab)]}")

tokens = tokenize(data)
vocab = set(tokens)
word_to_index = {word: i for i, word in enumerate(vocab)}
index_to_word = {i: word for i, word in enumerate(vocab)}

embeddings = create_embeddings(tokens, len(vocab))

# Step 4: Train the model
train_model(embeddings)

# Example inference
predict_next_word("space")
predict_next_word("sky")
predict_next_word("astronomy")
predict_next_word("universe")