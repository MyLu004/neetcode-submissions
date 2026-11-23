class Solution {
    /**
     * @param {number[]} nums
     * @return {boolean}
     */
    hasDuplicate(nums) {
        let myS = new Set();

        for (let i = 0; i < nums.length; i++){
            if (myS.has(nums[i])){
                return true
            }
            else{
                myS.add(nums[i]);
            }
        }
        return false
    }
}
