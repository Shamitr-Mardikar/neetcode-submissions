class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen_set = set()
        for item in nums:
            if item not in seen_set:
                seen_set.add(item)
            else:
                return True
        return False