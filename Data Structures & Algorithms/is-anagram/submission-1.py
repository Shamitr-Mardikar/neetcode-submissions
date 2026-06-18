class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
            
        alphabet_s = list(s)
        alphabet_t = list(t)
        s_dict = {}
        t_dict = {}
        for letter in alphabet_s:
            if letter in s_dict:
                s_dict[letter] += 1
            else:
                s_dict[letter] = 1

        for letter in alphabet_t:
            if letter in t_dict:
                t_dict[letter] += 1
            else:
                t_dict[letter] = 1

        if s_dict == t_dict:
            return True
        
        return False