class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indexMap = {} #start hash (index:value)

        for i in range(len(nums)):
            n = nums[i]
            diff = target - n
            if diff in indexMap:
                return [indexMap[diff],i]
            
            else:
                indexMap[n] = i