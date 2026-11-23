class Solution {
    /**
     * @param {number[]} prices
     * @return {number}
     */
    maxProfit(prices) {
        let l = 0, r = 1;
        let myMax = 0

        while(r < prices.length){
            if(prices[l]< prices[r]){
                let profit = prices[r] - prices[l];
                myMax = Math.max(myMax,profit)
            }
            else{
                l= r
            }
            r++;
        }
        
        return myMax
    }
    
}
