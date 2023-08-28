import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans

df = pd.read_csv('sbir_awards.csv')
abstracts = df['Abstract'].dropna()

vectorizer = TfidfVectorizer(stop_words='english')
X = vectorizer.fit_transform(abstracts)

# number of clusters can be adjusted as needed
kmeans = KMeans(n_clusters=10)
kmeans.fit(X)
terms = vectorizer.get_feature_names_out()
labels = kmeans.labels_


df_clusters = pd.DataFrame({'Abstract': abstracts, 'Cluster': labels})
df_clusters.to_csv('abstract_clusters.csv', index=False)
