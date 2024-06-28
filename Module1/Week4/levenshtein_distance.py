import streamlit as st

def calculate_distance(distances, token1, token2, t1, t2):
    """Calculate the distance between two tokens."""
    if token1[t1-1] == token2[t2-1]:
        distances[t1][t2] = distances[t1 - 1][t2 - 1]
    else:
        distances[t1][t2] = 1 + min(
            distances[t1][t2 - 1],  # Insert
            distances[t1 - 1][t2],  # Delete
            distances[t1 - 1][t2 - 1]  # Replace
        )

def levenshtein_distance(token1, token2):
    """Compute the Levenshtein distance between two strings."""
    distances = [[0] * (len(token2) + 1) for _ in range(len(token1) + 1)]

    for t1 in range(1, len(token1) + 1):
        distances[t1][0] = t1
    for t2 in range(1, len(token2) + 1):
        distances[0][t2] = t2

    for t1 in range(1, len(token1) + 1):
        for t2 in range(1, len(token2) + 1):
            calculate_distance(distances, token1, token2, t1, t2)

    return distances[-1][-1]

def load_vocab(file_path):
    """Load vocabulary from a file, ensuring each word is unique and sorted."""
    try:
        with open(file_path, 'r') as f:
            words = sorted({line.strip().lower() for line in f})
        return words
    except FileNotFoundError:
        st.error(f"File not found: {file_path}")
        return []

def main():
    """Main function to run the Streamlit app."""
    st.title("Word Correction using Levenshtein Distance")
    word = st.text_input('Word:')

    if st.button("Compute"):
        vocabs = load_vocab(file_path='./vocab.txt')
        leven_distances = {vocab: levenshtein_distance(word, vocab) for vocab in vocabs}
        sorted_distances = dict(sorted(leven_distances.items(), key=lambda item: item[1]))
        correct_word = next(iter(sorted_distances.keys()), 'No suggestion')
        st.write('Correct word:', correct_word)

        col1, col2 = st.columns(2)
        col1.write('Vocabulary:')
        col1.write(vocabs)

        col2.write('Distances:')
        col2.write(sorted_distances)

if __name__ == "__main__":
    main()
    