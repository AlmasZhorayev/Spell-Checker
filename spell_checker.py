import re 
import bloom_filter
import corpus
import bktree
import hashing

def build_spell_checker(table_size = 18000000):
    words = corpus.build_corpus()
    hash_functions = hashing.get_hash_functions(table_size)

    bf = bloom_filter.BloomFilter(table_size, hash_functions)
    for word in words:
        bf.add(word)
    
    tree = bktree.BKTree()
    for word in words:
        tree.add(word)

    return bf, tree

def check_sentence(sentence, bf, tree, k=3):
    results = {}
    words = sentence.lower().split()
    for word in words:
        cleaned_word = re.sub(r"[^a-z'-]", '', word)
        if cleaned_word and not bf.query(cleaned_word):
            results[cleaned_word] = tree.query(cleaned_word, k)
    return results