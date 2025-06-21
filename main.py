import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Step 1: Load the dataset
df = pd.read_csv("data/netflix_titles.csv")

# Step 2: Clean the data
df['description'] = df['description'].fillna("")

# Step 3: Convert text to TF-IDF vectors
tfidf = TfidfVectorizer(stop_words='english')
tfidf_matrix = tfidf.fit_transform(df['description'])

# Step 4: Compute cosine similarity matrix
cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)

# Step 5: Create a reverse index to look up movie by title
indices = pd.Series(df.index, index=df['title']).drop_duplicates()

# Step 6: Recommendation function
def get_recommendations(title, cosine_sim=cosine_sim):
    if title not in indices:
        return "❌ Movie not found in database."

    idx = indices[title]
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)[1:6]
    movie_indices = [i[0] for i in sim_scores]
    return df['title'].iloc[movie_indices]

# Step 7: Ask for user input
movie_name = input("Enter a movie title: ")
recommendations = get_recommendations(movie_name)
print("\n🎬 Top 5 Recommended Movies:")
print(recommendations)
