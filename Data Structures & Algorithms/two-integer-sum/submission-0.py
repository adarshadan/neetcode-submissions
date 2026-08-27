class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_indices = []
        isMatchFound = False
        count1 = 0
        count2 = 0
        for i,value1 in enumerate(nums):
            for j,value2 in enumerate(nums):
                if i!=j:
                    #print(f"i: {i} ,j: {j}")
                    #print(f"value1: {value1} ,value2: {value2}")
                    if value1 + value2 == target:
                        num_indices.append(i)
                        num_indices.append(j)
                        isMatchFound = True
                        print("Match Found")
                        break
            if isMatchFound:
                break
        return num_indices