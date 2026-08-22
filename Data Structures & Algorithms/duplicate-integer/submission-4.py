
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        list_size = len(nums)

        #unique_elements = len(set(nums))

        if list_size >= 0 and list_size <= 10**5:

            return len(set(nums)) != list_size

        return false
