class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}

        for i in nums:
            count[i] =1+count.get(i,0)
        
        myArray = []

        for idx,value in count.items():
            myArray.append([value,idx])
        
        myArray.sort()
        
        myResult = []

        for i in range(k):
            myResult.append(myArray.pop()[1])
        
        return myResult
        
       
    

        


        

        