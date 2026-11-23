class Solution {
    /**
     * @param {string} s
     * @param {string} t
     * @return {boolean}
     */
    isAnagram(s, t) {
        if(s.length != t.length){
            return false
        }

        // declare new dict for s and t
        let myS = {}
        let myT = {}

        for(let i = 0; i<s.length;i++){
            myS[s[i]] = (myS[s[i]] || 0) +1
            myT[t[i]] = (myT[t[i]] || 0) +1
        }

        for(const key in myS){
            if (myS[key] != myT[key]){
                return false
            }
        }
        return true

    }
}
