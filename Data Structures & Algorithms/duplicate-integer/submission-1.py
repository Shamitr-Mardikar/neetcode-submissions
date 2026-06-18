class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        test_dict = {}
        for item in nums:
            if item in test_dict:
                test_dict[item] += 1
            else:
                test_dict[item] = 1

        for (key,value) in test_dict.items():
            if value > 1:
                return True    
        return False
        
