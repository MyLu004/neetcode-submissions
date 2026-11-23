class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        result = 0

        j = 0
        for i in range(len(s)):
            #increment or add the char into the hash array
            count[s[i]] = 1 + count.get(s[i],0)

            while (i - j + 1) - max(count.values()) > k:
                count[s[j]] -= 1
                j += 1
            result = max(result, i-j+1)
        return result