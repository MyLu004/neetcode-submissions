class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        output = []
        #sliding windown pointer
        l, r = 0,0
        #deque list
        q = collections.deque()

        while r < len(nums):
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            q.append(r) #append the index itself
            
            #remove left value from the window
            if l > q[0]:
                q.popleft()

            #if want to update the wondow, ,make sure the r+1 larger than size k
            if (r+1) >= k:
                output.append(nums[q[0]])
                l += 1
            r += 1

        return output
       