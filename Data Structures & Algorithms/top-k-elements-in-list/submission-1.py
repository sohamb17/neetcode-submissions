class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        import heapq
        from collections import Counter
        c = Counter(nums).items()
        min_heap = []
        for ki, v in c:
            heapq.heappush(min_heap, (v, ki))
            if len(min_heap) > k:
                heapq.heappop(min_heap)
        return [heapq.heappop(min_heap)[1] for _ in range(k)]