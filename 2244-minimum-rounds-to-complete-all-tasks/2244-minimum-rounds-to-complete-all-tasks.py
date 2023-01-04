class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        tasks = Counter(tasks)              
        if 1 in tasks.values(): return -1  

        ans = 0                            
        for n in tasks.values():
            ans+= n//3 + bool(n%3)      
        return  ans