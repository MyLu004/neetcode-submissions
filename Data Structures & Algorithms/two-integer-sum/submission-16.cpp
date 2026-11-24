class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
       int numLen = nums.size();
        unordered_map<int, int> preMap;

        for (int i = 0; i< numLen; i++){
            int diff = target - nums[i];
            if(preMap.find(diff)!= preMap.end()){
                return {preMap[diff], i};
            }

            preMap.insert({nums[i],i});
        }
        return {};

       
    }
};
