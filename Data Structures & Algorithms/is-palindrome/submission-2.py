class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = (s.replace(" ","")).lower()
        mystring = ''.join([char for char in s if char.isalpha() or char.isalnum()])
        newstring = ""
        for i in mystring[::-1]:
            newstring +=i
        
        return (newstring == mystring)