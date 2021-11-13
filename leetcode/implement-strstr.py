class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        try:
            haystack.index(needle)
            return haystack.index(needle)
        except ValueError:
            return -1
