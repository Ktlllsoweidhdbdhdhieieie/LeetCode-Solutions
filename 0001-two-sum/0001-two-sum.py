class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #ek loop chalenge pahle number ke liye
        for i in range(len(nums)):
            #dusri loop chalenge aage wale number ke liye
            for j in range(i+1,len(nums)):
                if nums[i]+nums[j]==target:
                    return[i, j]
        