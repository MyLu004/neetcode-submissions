class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        ops = {"+": (lambda x,y: x+y), "-": (lambda x,y: y-x), "*":(lambda x,y: x*y), "/":(lambda x,y:y/x)}
        val = 0
        mystack = []

        for i in tokens:
            if i.lstrip('-+').isdigit():
                mystack.append(int(i))
            else:
                mystack.append(int(ops[i](mystack.pop(), mystack.pop())))

        return mystack[0]