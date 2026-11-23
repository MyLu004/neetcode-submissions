class Solution {
    /**
     * @param {string} s
     * @return {boolean}
     */
    isValid(s) {
        const myStack = []

        const closeToOpenDict = {
            ')':'(',
            ']':'[',
            '}':'{'
        }



         for (let i of s){
            if (closeToOpenDict[i]){
                // check if the stack not empty and the stack value is open corresponding to the close
                if(myStack.length !== 0 && myStack[myStack.length-1] === closeToOpenDict[i]){
                    myStack.pop()
                }
                else{
                    return false
                }
            }
            else{
                myStack.push(i)
            }
         }
         return myStack.length === 0;


    }
}
