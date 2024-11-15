class Solution:
    def countSegments(self, s: str) -> int:
        arr = []
        curr = ""
        for i in s:
            if i==" ":
                if curr != "":
                    arr.append(curr)
                curr = ""
                continue
            curr += i
        if curr not in arr and curr !="":
            arr.append(curr)
        return len(arr)
            