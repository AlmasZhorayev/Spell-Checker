import nltk
import os
import pickle

CACHE_PATH = "corpus_cache.pkl"

def build_corpus():
    if os.path.exists(CACHE_PATH):
        print('Loading cached corpus...')
        with open(CACHE_PATH, 'rb') as f:
            return pickle.load(f)
    print("Building corpus from NLTK...")
    nltk.download('words', quiet=True)
    nltk.download('brown', quiet=True)

    words_list = nltk.corpus.words.words()
    brown_list = nltk.corpus.brown.words()
    all_words = set(w.lower() for w in words_list + list(brown_list))

    with open(CACHE_PATH, 'wb') as f:
        pickle.dump(all_words, f)
    print(f'Corpus cached {len(all_words)} unique words for future use.')
    
    return all_words