import numpy as np

def ascii_sum(string, table_size):
    total = 0
    for char in string:
        total + ord(char)
    return total % table_size

def jenkins_hash(string, table_size):
    hash_value = 0
    for char in string:
        hash_value += ord(char)
        hash_value += hash_value << 10
        hash_value ^= hash_value >> 8
    hash_value += hash_value << 3
    hash_value ^= hash_value >> 11
    hash_value += hash_value << 15
    return str(hash_value % table_size)