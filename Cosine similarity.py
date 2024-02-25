from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def calculate_cosine_similarity(statement1, statement2):
    # Create a CountVectorizer
    vectorizer = CountVectorizer()

    vectors = vectorizer.fit_transform([statement1, statement2])

    similarity_matrix = cosine_similarity(vectors)

    similarity = similarity_matrix[0, 1]

    return similarity

# Example usage
statement1 = input("Enter a statement")
statement2 = input("Enter another statement")
similarity_score = calculate_cosine_similarity(statement1, statement2)
print(f"Cosine Similarity: {similarity_score}")
