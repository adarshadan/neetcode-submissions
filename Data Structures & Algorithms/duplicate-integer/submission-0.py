from typing import List
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        list_size = len(nums)

        unique_elements = len(set(nums))

        #print(list_size)
        #print(unique_elements)

        if list_size < 0 or list_size > 10**5:
            raise "Invalid List Size"
        else:
            if unique_elements != list_size:
                return True
            else:
                return False

'''nums = [1,2,3,3]

obj = Solution()
has_duplicate = obj.hasDuplicate(nums)
print(has_duplicate)'''