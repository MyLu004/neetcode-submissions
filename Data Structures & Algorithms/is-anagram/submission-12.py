class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) != len(t):
            return False
        
        countS , countT = {},{}

        for a,b in zip(s,t):
            countS[a] = 1 + countS.get(a,0)
            countT[b] = 1 + countT.get(b,0)
        
        return countS == countT