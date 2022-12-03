class Solution:
    def frequencySort(self, s: str) -> str:
        list1=list(s)
        ans=[n for n,count in Counter(list1).most_common() for i in range(count)]
        return "".join(ans)