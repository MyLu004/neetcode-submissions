class MinStack {
    constructor() {
        this.MyS = []
        this.MinS = []
    }

    /**
     * @param {number} val
     * @return {void}
     */
    push(val) {
        this.MyS.push(val)

        //compute the min val to push into the min stack
        let minVal = Math.min(val, this.MinS.length === 0? val: this.MinS[this.MinS.length-1])

        this.MinS.push(minVal)


    }

    /**
     * @return {void}
     */
    pop() {
        this.MyS.pop()
        this.MinS.pop()

    }

    /**
     * @return {number}
     */
    top() {
        return this.MyS[this.MyS.length-1]
    }

    /**
     * @return {number}
     */
    getMin() {
        return this.MinS[this.MinS.length-1]
    }
}
