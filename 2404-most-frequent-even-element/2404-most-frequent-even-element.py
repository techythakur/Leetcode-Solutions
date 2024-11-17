class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        dic = {}
        for i in nums:
            if i%2==0:
                if i not in dic:
                    dic[i]=1
                else:
                    dic[i]+=1
        sorted_dic = sorted(dic.items(), key=lambda x: (-x[1], x[0]))
        return sorted_dic[0][0] if sorted_dic else -1
        