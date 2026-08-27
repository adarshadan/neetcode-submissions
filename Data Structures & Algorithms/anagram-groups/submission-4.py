class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        output = []
        seen = {}
        index = 0
        for item in strs:
            sorted_item = "".join(sorted(item))
            if sorted_item in seen:
                output[seen[sorted_item]].append(item)
            else:
                output.append([item])
                seen[sorted_item] = index
                index += 1

        return output