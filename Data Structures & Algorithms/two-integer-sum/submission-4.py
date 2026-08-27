class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_indices = []
        isMatchFound = False
        for i,value1 in enumerate(nums):
            for j,value2 in enumerate(nums):
                if i!=j:
                    if value1 + value2 == target:
                        num_indices.append(i)
                        num_indices.append(j)
                        isMatchFound = True
                        break
            if isMatchFound:
                break
        return num_indices