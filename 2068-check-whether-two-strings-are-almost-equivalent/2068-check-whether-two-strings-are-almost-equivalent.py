from collections import Counter
class Solution:
    def checkAlmostEquivalent(self, word1: str, word2: str) -> bool:
        count1 = Counter(word1)
        count2 = Counter(word2)
        for key, value in count1.items():
            if abs(value-count2.get(key,0))>3:
                return False
        
        for key, value in count2.items():
            if abs(value-count1.get(key,0))>3:
                return False
        return True