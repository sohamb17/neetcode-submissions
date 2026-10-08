class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        from collections import Counter
        c = Counter(nums)
        return any(i > 1 for i in c.values())