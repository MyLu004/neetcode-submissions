class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        unordered_map<int, int> count;

        for(int num : nums){
            count[num]++;
        }

        vector<pair<int,int>> myArr;
        for (const auto& p : count){
            myArr.push_back({p.second, p.first});
        }
        // sort descendance
        sort(myArr.rbegin(), myArr.rend());

        vector<int> myResult;
        for(int i = 0; i < k; i++){
            myResult.push_back(myArr[i].second);
        }
        return myResult;
    }
};
