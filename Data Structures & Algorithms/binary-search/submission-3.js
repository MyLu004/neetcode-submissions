class Solution {
    /**
     * @param {number[]} nums
     * @param {number} target
     * @return {number}
     */


    binarySearchFunction(l, r, nums, target){
        if (l >  r) return -1;

        let midPoint = l + Math.floor((r-l)/2)

        if (nums[midPoint] === target) return midPoint;

        return nums[midPoint] < target ? 
            this.binarySearchFunction(midPoint+1,r,nums,target):
            this.binarySearchFunction(l, midPoint-1, nums, target)
    }

    search(nums, target) {
        return this.binarySearchFunction(0, nums.length-1, nums, target)
        

        


    }
}
