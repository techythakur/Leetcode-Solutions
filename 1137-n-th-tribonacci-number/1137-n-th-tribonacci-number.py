class Solution:
    def tribonacci(self, n: int) -> int:
        arr=[0,1,1]
        if n==0:
            return arr[0]
        if n==1 or n==2:
            return arr[1]
        for i in range(3,n+1):
            arr.append(arr[i-1]+arr[i-2]+arr[i-3])
        return arr[n]
            