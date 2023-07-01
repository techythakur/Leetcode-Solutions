class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        def solve(ind,arr):
            if ind==n:
                nonlocal ans
                mx=max(arr)
                ans=min(ans,mx)
                return
            for i in range(k):
                arr[i]+=cookies[ind]
                solve(ind+1,arr)
                arr[i]-=cookies[ind]
                if arr[i]==0:
                    break

        n=len(cookies)
        ans=float('inf')
        arr=[0 for i in range(k)]
        solve(0,arr)
        return ans