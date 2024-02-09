class Solution:
    def removeDigit(self, number: str, digit: str) -> str:
        s=int(number.replace(digit,'',1))
        for i in range(len(number)):
            if number[i]==digit:
                x=number[:i]+number[i+1:]
                s=max(s,int(x))
                
        return str(s)
            
            
        
            