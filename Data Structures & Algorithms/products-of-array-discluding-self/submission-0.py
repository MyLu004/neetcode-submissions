class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix_list = list(nums)
        post_list = list(nums)
        result=[]

        for i in range(len(nums)):
            if i == 0:
                prefix_list[i] *= 1
            else:
                prefix_list[i] = prefix_list[i] * prefix_list[i-1]

        for i in reversed(range(len(nums))):
            if i == (len(nums)-1):
                post_list[i] *= 1
            else:
                post_list[i] = post_list[i] * post_list[i+1]

        for i in range(len(nums)):
            if i == 0:
                result.append(post_list[i+1])
            elif i ==  (len(nums)-1):
                result.append(prefix_list[i-1])
            else:
                result.append(prefix_list[i-1]*post_list[i+1])
        
        return result

        