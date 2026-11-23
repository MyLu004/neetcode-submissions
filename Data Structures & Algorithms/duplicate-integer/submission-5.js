class Solution {
    /**
     * @param {number[]} nums
     * @return {boolean}
     */
    hasDuplicate(nums) {
        const myS = new Set()


        for (let i of nums){
            if (!myS.has(i)){
                myS.add(i)
            }
            else{
                return true
            }
        }
        return false
    }

}
