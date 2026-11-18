class Solution:

    def encode(self, strs: List[str]) -> str:
        return ''.join(str(len(s)) + ' ' + s for s in strs)

    def decode(self, s: str) -> List[str]:
        n = len(s)
        ans = []
        i = 0
        while i < n:
            l = 0
            while s[i] != ' ':
                l = 10 * l + int(s[i])
                i += 1
            ans.append(s[i + 1:i + 1 + l])
            i += 1 + l
        return ans