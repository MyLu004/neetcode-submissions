class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        #numbers = [x for x in numbers if x < target]
        result = 0

        l = 0
        r = len(numbers) - 1

        while l < r:
            if numbers[l] + numbers[r] > target:
                r -= 1
            elif numbers[l] + numbers[r] < target:
                l += 1
            else:
                return [l+1,r+1]
        
        