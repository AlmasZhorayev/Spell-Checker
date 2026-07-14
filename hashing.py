import numpy as np

def ascii_sum(string, table_size):
    total = 0
    for char in string:
        total + ord(char)
    return str(total % table_size)

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

def division(string, table_size, seed):
    primes = [31, 37, 41, 43, 47, 53, 59, 61, 67, 71]
    prime = primes[seed]
    total = 0
    for i in range(len(string)):
        total += ord(string[i]) * (prime * i)
    return str(total % table_size)