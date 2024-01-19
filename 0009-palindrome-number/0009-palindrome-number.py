class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x>=0:
            string=str(x)
            newString=string[::-1]
            if string==string[::-1]:
                return True
            else:
                return False
        else:
            return False