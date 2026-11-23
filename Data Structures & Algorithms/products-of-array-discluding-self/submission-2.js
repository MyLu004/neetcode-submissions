class Solution {
    /**
     * @param {number[]} nums
     * @return {number[]}
     */
    productExceptSelf(nums) {
        let prod = 1;
        let zeroCount = 0;


        // checking how many zero are there in the array
        for(let i of nums){
            if (i !== 0){
                prod *= i;
            }
            else{
                zeroCount++;
            }
        }

        if(zeroCount > 1){
            return Array(nums.length).fill(0)
        }

        const res = Array(nums.length)
        for (let i = 0; i < nums.length; i++){
            if (zeroCount>0){
                res[i] = nums[i] === 0 ? prod: 0;
            }
            else{
                res[i] = prod/nums[i]
            }
        }
        return res;

    }
}
