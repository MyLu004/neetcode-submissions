class Solution {
    /**
     * @param {number[]} temperatures
     * @return {number[]}
     */
    dailyTemperatures(temperatures) {
        const resultList = new Array(temperatures.length).fill(0)

        const myStack = [] // pair [temp:idx]

      for (let i = 0; i < temperatures.length; i++){
        const t = temperatures[i]

        while(myStack.length > 0 && t > myStack[myStack.length-1][0]){
            const [stackVal, stackIndx] = myStack.pop()
            resultList[stackIndx] = i - stackIndx
        }
        myStack.push([t,i])
      }
      return resultList;

    }
}
