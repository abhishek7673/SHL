# import pandas as pd
# from sentence_transformers import SentenceTransformer, util

# class SHLRecommender:
#     def __init__(self, catalog_path="catalog_data.csv"):
#         self.model = SentenceTransformer("TfidfVectorizer")
#         self.catalog = pd.read_csv(catalog_path)
#         self.catalog["embedding"] = self.catalog["Tags"].apply(lambda x: self.model.encode(x, convert_to_tensor=True))

#     def recommend(self, query, top_k=10):
#         query_embedding = self.model.encode(query, convert_to_tensor=True)
#         self.catalog["score"] = self.catalog["embedding"].apply(lambda emb: float(util.pytorch_cos_sim(query_embedding, emb)))
#         top_results = self.catalog.sort_values("score", ascending=False).head(top_k)
#         return top_results[["Assessment Name", "URL", "Remote Support", "Adaptive Support", "Duration", "Type", "score"]]


# recommender.py
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

class SHLRecommender:
    def __init__(self, catalog_path="catalog_data.csv"):
        self.catalog = pd.read_csv(catalog_path)
        self.vectorizer = TfidfVectorizer(stop_words="english")
        self.vectors = self.vectorizer.fit_transform(self.catalog["Assessment Description"])

    def recommend(self, query, top_k=5):
        query_vec = self.vectorizer.transform([query])
        scores = cosine_similarity(query_vec, self.vectors).flatten()
        top_indices = scores.argsort()[::-1][:top_k]
        return self.catalog.iloc[top_indices][["Assessment Name", "URL", "Remote Support", "Adaptive Support", "Duration", "Type", "Tags"]]
