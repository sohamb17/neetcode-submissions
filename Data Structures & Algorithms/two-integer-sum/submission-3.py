class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        from bisect import bisect
        n = len(nums)
        s = {}
        for i in range(n):
            if nums[i] not in s:
                s[nums[i]] = i
        e = {}
        for i in range(n - 1, -1, -1):
            if nums[i] not in e:
                e[nums[i]] = i
        nums.sort()
        for i in range(n):
            t = target - nums[i]
            j = bisect(nums, t) - 1
            if j >= 0 and nums[j] == t:
                return sorted([s[nums[i]], e[nums[j]]])