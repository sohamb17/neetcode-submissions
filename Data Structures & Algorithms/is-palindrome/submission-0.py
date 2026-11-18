class Solution:
    def isPalindrome(self, s: str) -> bool:
        alphanum = ''.join(c.lower() for c in s if c.isalnum())
        return alphanum == alphanum[::-1]