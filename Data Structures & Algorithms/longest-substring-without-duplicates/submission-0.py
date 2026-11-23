class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        mySet = set()
        l = 0
        result = 0
        for i in range(len(s)):
            while s[i] in mySet:
                mySet.remove(s[l])
                l += 1
            mySet.add(s[i])
            result = max(result, (i-l+1))
        return result