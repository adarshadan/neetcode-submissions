class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        str1_len = len(s)
        str2_len = len(t)

        dict_1 = {}
        dict_2 = {}

        if (str1_len >=1 and str1_len <= 5* 10**4) and (str2_len >=1 and str2_len <= 5* 10**4) and str1_len == str2_len:
            
            for char in s:
                if char not in dict_1.keys():
                    dict_1[char] = 1
                else: 
                    dict_1[char] += 1

            for char in t:
                if char not in dict_2.keys():
                    dict_2[char] = 1
                else: 
                    dict_2[char] += 1

            return dict_1 == dict_2

        return False