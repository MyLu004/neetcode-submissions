class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        myCount={}
        for i in nums:
            myCount[i] = 1 + myCount.get(i,0)
    
        myArr = []

        for idx, value in myCount.items():
            myArr.append([value,idx])
    
        myArr.sort()

        myresult = []
        while len(myresult) < k:
            myresult.append(myArr.pop()[1])
    
        return myresult
    

        


        

        