from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_indices = []
        for i,value in enumerate(nums):
            complement = target - value
            if complement in nums:
                j = nums.index(complement)
                if i!=j and j >=0:
                    num_indices.append(min(i,j))
                    num_indices.append(max(i,j))
                    break
        return num_indices