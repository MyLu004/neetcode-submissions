class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t) or t == "":
            return ""
        

        #initialize 2 empty hash map to compare late
        countT, window = {},{}

        for c in t:
            #if c exist in map, it will get +1, else: default = 0
            countT[c] = 1 + countT.get(c,0)

        #to compare later on
        have, need = 0, len(countT)
        
        res = [-1,-1]
        resLen = float("infinity")

        l = 0
        
        for r in range(len(s)):
            c = s[r] #value[idx]
            window[c] = 1 + window.get(c,0)

            #check if the element is satify the T hash-table
            if c in countT and window[c] == countT[c]:
                have += 1 #incr have if met condt in T-table
            

            #condition between have == need
            while have == need:
                #update result

                #will at least got exec 1 time
                if (r - l + 1)< resLen:
                    res = [l,r]
                    resLen = (r-l+1)
                
                #pop from the left until the condition not met
                #rmv the left most character | pop from the left of the window
                window[s[l]] -= 1
                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    have -= 1
                l += 1

        l,r = res
        return s[l:r+1] if resLen != float("infinity") else ""







