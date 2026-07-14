import nltk

def build_corpus():
    words_list = nltk.corpus.words.words()
    brown_list = nltk.corpus.brown.words()
    all_words = set(w.lower() for w in words_list + list(brown_list))
    return all_words