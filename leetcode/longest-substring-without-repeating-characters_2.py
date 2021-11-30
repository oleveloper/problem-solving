class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxlen = 0
        substr = []
        for i, v in enumerate(list(s)):
            if v in substr:
                substr = substr[substr.index(v) + 1:]

            substr.append(v)

            if maxlen < len(substr):
                maxlen = len(substr)
                
        return maxlen
