class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        from collections import deque
        n = len(nums)
        pre = [nums[0]]
        for i in range(1, n):
            pre.append(pre[-1] * nums[i])
        suff = deque([nums[-1]])
        for i in range(n - 2, -1, -1):
            suff.appendleft(suff[0] * nums[i])
        ans = []
        for i in range(n):
            if 0 < i < n - 1:
                ans.append(pre[i - 1] * suff[i + 1])
            elif 0 < i:
                ans.append(pre[i - 1])
            elif i < n - 1:
                ans.append(suff[i + 1])
        return ans
