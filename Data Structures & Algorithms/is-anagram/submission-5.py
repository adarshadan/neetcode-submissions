class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        str1_len = len(s)
        str2_len = len(t)

        dict_1 = {}
        dict_2 = {}

        if (str1_len >=1 and str1_len <= 5* 10**4) and (str2_len >=1 and str2_len <= 5* 10**4) and str1_len == str2_len:
            
            for char in s:
                dict_1[char] = dict_1.get(char,0) + 1

            for char in t:
                dict_2[char] = dict_2.get(char,0) + 1

            return dict_1 == dict_2

        return False