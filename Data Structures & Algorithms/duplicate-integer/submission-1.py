class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seenList = set()

        for i in nums:
            if i in seenList:
                return True
            else:
                seenList.add(i)
            
        return False
        