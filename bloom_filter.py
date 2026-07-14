class BloomFilter:
    def __init__(self, table_size, hash_functions):
        self.table_size = table_size
        self.hash_functions = hash_functions
        self.bit_array = [0] * table_size

    def add(self, item):
        for hash_function in self.hash_functions:
            index = hash_function(item) % self.table_size
            self.bit_array[index] = 1

    def query(self, item):
        for hash_function in self.hash_functions:
            index = hash_function(item) % self.table_size
            if self.bit_array[index] == 0:
                return False
        return True