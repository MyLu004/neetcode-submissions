class Solution {
    /**
     * @param {number[]} nums
     * @param {number} target
     * @return {number[]}
     */
    twoSum(nums, target) {
        let myA = []

        for (let i = 0; i < nums.length; i++){
            myA.push([nums[i],i])
            // store the array with [value, index]
        }

        

        // sort the array
        // sort the value
        myA.sort((a,b)=> a[0]-b[0])

        //declare index for start and the end
        let i = 0
        let j = nums.length - 1

        while (i < j){
            let myCur = myA[i][0] + myA[j][0]

            if (myCur === target){
                return [Math.min(myA[i][1], myA[j][1]), Math.max(myA[i][1],myA[j][1])]
            }
            else if(myCur < target){
                i++;
            }
            else {
                j--;
            }
        }
        return []

    }
}