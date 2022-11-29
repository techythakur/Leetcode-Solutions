class RandomizedSet:

    def __init__(self):
        # Initialize Set
        self.sets = set()

    def insert(self, val: int) -> bool:
        # If n is present in set then return false
        if val in self.sets : 
            return False
        
        # If n is not present in set then add it to the set.
        self.sets.add(val)
        return True

    def remove(self, val: int) -> bool:
        # If n is in set then remove n else return false
        if val in self.sets:
            self.sets.remove(val)
            return True
        return False

    def getRandom(self) -> int:
        # Return random number using random module
        return random.choice(list(self.sets))

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()