class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        s_backspaced = []
        t_backspaced = []
        
        for i in range(len(s)):
            if s[i] == '#':
                if s_backspaced:
                    s_backspaced.pop()
            else:
                s_backspaced.append(s[i])
            
        for i in range(len(t)):
            if t[i] == '#':
                if t_backspaced:
                    t_backspaced.pop()
            else:
                t_backspaced.append(t[i])
        
        return s_backspaced == t_backspaced
        '''stacks=[]
        stackt=[]
        for i in s:
            if i=="#" and stacks:
                stacks.pop()
            else:
                stacks.append(i)
        for j in t:
            if j=="#" and stackt:
                stackt.pop()
            else:
                stackt.append(i)
        print(stackt,t)
        return stacks==stackt'''