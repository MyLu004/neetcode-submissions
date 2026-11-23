class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.myArray = nums

    def add(self, val: int) -> int:
        self.myArray.append(val)
        self.myArray.sort()
        return self.myArray[len(self.myArray)-self.k]
        
