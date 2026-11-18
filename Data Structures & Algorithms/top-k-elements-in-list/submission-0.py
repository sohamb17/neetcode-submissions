class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from collections import Counter
        return [k for k, v in Counter(nums).most_common(k)]