import numpy as np

def get_hash_functions(table_size):
    hash_functions = []
    hash_functions.append(lambda s: ascii_sum(s, table_size))
    hash_functions.append(lambda s: jenkins_hash(s, table_size))
    for seed in range(10):
        hash_functions.append(lambda s, seed=seed: division(s, table_size, seed))
    for seed in range(10):
        hash_functions.append(lambda s, seed=seed: fnv1a(s, table_size, seed))
    return hash_functions

def ascii_sum(string, table_size):
    total = 0
    for char in string:
        total += ord(char)
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

def fnv1a(string, table_size, seed):
    fnv_primes = [16777619, 16777633, 16777639, 16777643, 16777669,
                  16777679, 16777681, 16777699, 16777711, 16777721]
    prime = fnv_primes[seed]
    hash_value = 0x811c9dc5
    for char in string:
        hash_value *= prime
        hash_value ^= ord(char)
        hash_value &= 0xffffffff
    return str(hash_value % table_size)