class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:       
        seen = {}
        output = []
        for num in nums:
            if num in seen:
                seen[num] += 1
            else:
                seen[num] = 1

        freq_list = sorted(seen.items(), key = lambda values: values[1], reverse = True)

        a,_  = zip(*freq_list[0:k])

        output = list(a)
      
        return output