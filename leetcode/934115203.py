# Length of Last Word
# https://leetcode.com/problems/length-of-last-word/submissions/934115203/

import re

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        words = re.sub(r"^\s+", " ", s).strip().split(' ')
        return len(words[-1])
