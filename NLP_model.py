import pandas as pd
import spacy
from collections import Counter
import en_core_web_sm
nlp = en_core_web_sm.load()


df = pd.read_csv('sbir_awards.csv')
abstracts = df['Abstract'].dropna()

# word frequencies
word_freq = Counter()
for abstract in abstracts:
    doc = nlp(abstract)
    words = [token.text for token in doc if not token.is_stop and not token.is_punct]
    word_freq.update(words)

word_freq_df = pd.DataFrame(word_freq.items(), columns=['Word', 'Frequency'])
word_freq_df.to_csv('word_frequencies.csv', index=False)

# noun chunk frequencies
noun_chunk_freq = Counter()
for abstract in abstracts:
    doc = nlp(abstract)
    noun_chunks = [chunk.text for chunk in doc.noun_chunks]
    noun_chunk_freq.update(noun_chunks)

noun_chunk_freq_df = pd.DataFrame(noun_chunk_freq.items(), columns=['Noun Chunk', 'Frequency'])
noun_chunk_freq_df.to_csv('noun_chunk_frequencies.csv', index=False)


from sklearn.feature_extraction.text import CountVectorizer

def extract_ngrams(text, min_n, max_n):
    vectorizer = CountVectorizer(ngram_range=(min_n, max_n))
    ngrams = vectorizer.fit_transform(text)
    ngrams_list = vectorizer.get_feature_names_out()
    return ngrams_list

n_min = 3
n_max = 6

ngrams_list = extract_ngrams(abstracts, n_min, n_max)
ngram_freq = Counter(ngrams_list)

ngram_freq_df = pd.DataFrame(ngram_freq.items(), columns=['N-gram', 'Frequency'])
ngram_freq_df.to_csv('ngram_frequencies.csv', index=False)