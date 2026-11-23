class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        rightList = t
        if len(s) != len(t):
            return False

        for i in s:
            #print(i)
            if i in t:
                #print(i,t)
                t = t.replace(i,'',1)
            else:
                continue
        
        print(t)

        if len(t)>0:
            return False
        else:
            return True