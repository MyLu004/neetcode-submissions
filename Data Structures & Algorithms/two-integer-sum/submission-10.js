class Solution {
    /**
     * @param {number[]} nums
     * @param {number} target
     * @return {number[]}
     */
    twoSum(nums, target) {
        
        let myA = []
        for (let i =0; i< nums.length; i++){
            myA.push([nums[i],i])
        }

        myA.sort((a,b)=> a[0]-b[0])


        let l = 0, r = nums.length-1

        while(l<r){
            let myCur = myA[l][0] + myA[r][0]

            if(myCur === target){
                return [Math.min(myA[l][1],myA[r][1]), Math.max(myA[l][1], myA[r][1])]
            }
            else if( myCur < target){
                l++
            }
            else{
                r--
            }
        }
        return []

    }
}