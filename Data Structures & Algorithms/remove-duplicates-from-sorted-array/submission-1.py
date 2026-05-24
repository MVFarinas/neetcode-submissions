class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l = 1 #initialize left pointer at index 1 instead of 0 since i0 will alawys stay the same

        #initialize right pointer at 1 and have it iterate through array
        for r in range (1, len(nums)):
            if nums[r] != nums[r-1]: #rPointer value vs value before
                nums[l] = nums[r] #set lPointer value = rPointer value
                l += 1 #move lPointer 
                #no need to do r += 1 since for loop automatically does this

        return l