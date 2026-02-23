class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        divided = list(s)
        pointer = 0
        for c in t:
            if pointer < len(s) and c == divided[pointer]:
                pointer += 1
        return pointer == len(s)
