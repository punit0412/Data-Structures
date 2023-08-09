class HashTable:
    def __init__(self):
        self.capacity = 10
        self.keys = [None]*self.capacity
        self.values = [None]*self.capacity

    def insert(self,key,data):
        # find the index for the particular key
        index = self.hashFunction(key)
        # to avoid collision we have to find the empty slots
        while self.keys[index] is not None:
            # if that is key is already present in the table then update the data
            if self.keys[index] == key:
                self.keys[index] = key
                self.values[index] = data
                return
            # we take the modulo with capacity to check the index should not greater than capacity

            index = (index+1) % self.capacity

        # we have found the index where slot is empty

        self.keys[index] = key
        self.values[index] = data

    def get(self,key):
        index = self.hashFunction(key)
        while self.keys[index] is not None:
            if self.keys[index] == key:
                return self.values[index]

            index = (index+1) % self.capacity
        return None

    def hashFunction(self,key):
        hash_sum = 0
        for letter in key:
            hash_sum += ord(letter) # ord function returns the ascii value of letter

        return hash_sum % self.capacity

