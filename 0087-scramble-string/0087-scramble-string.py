class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:
        if len(s1)!=len(s2):
            return False
        m=dict()
        def f(a,b):
            if (a,b) in m:
                return m[(a,b)]
            if a==b:
                m[a,b]=True
                return True
            if len(a)!=len(b):
                m[(a,b)]=False
                return False
            
            for i in range(1,len(a)):
                if f(a[:i],b[:i]) and f(a[i:],b[i:]):
                    m[(a,b)]=True
                    return True
                if f(a[:i],b[-i:]) and f(a[i:],b[:len(a)-i]):
                    m[(a,b)]=True
                    return True
                
            m[(a,b)]=False
            return False
        return f(s1,s2)