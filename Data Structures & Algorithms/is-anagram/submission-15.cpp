class Solution {
public:
    bool isAnagram(string s, string t) {
        if(s.size() != t.size()){return false;}

        unordered_map<char, int> countT;
        unordered_map<char, int> countS;

        for(int i=0; i < t.length(); i++){
            countS[s[i]]++;
            countT[t[i]]++;
        }

        return countS == countT;
    }
};
