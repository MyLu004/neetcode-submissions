class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        # make the empty array for hashmap
        s1Count, s2Count = [0] *26, [0]*26

        #initial the first value of len(s1) for both string
        for i in range(len(s1)):
            s1Count[ord(s1[i]) - ord('a')] += 1 #map to the index in the ASCII to +1
            s2Count[ord(s2[i]) - ord('a')] += 1 #map to the index in the ASCII to +1
           
        matches = 0
        #compare each of the map
        #init match compare
        for i in range(26):
            if s1Count[i] == s2Count[i]:
                matches += 1 
            else:
                pass
        
        #sliding windown
        l = 0

        #update the matches value
        for r in range(len(s1),len(s2)):
            if matches == 26: #return immediately if it match this
                return True
            
            index = ord(s2[r]) - ord('a') #update the new value
            s2Count[index] += 1
            if s1Count[index] == s2Count[index]: 
            #check if the value in s1 hashmap to increment the matches
                matches += 1
            elif s1Count[index] + 1 == s2Count[index]:
                matches -= 1


            index = ord(s2[l]) - ord('a') #update the new value
            s2Count[index] -= 1
            if s1Count[index] == s2Count[index]: 
            #check if the value in s1 hashmap to increment the matches
                matches += 1
            elif s1Count[index] - 1 == s2Count[index]:
                matches -= 1

            l += 1
        return matches == 26






