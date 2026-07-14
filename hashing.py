import numpy as np

def ascii_sum(string, table_size):
    total = 0
    for char in string:
        total + ord(char)
    return total % table_size