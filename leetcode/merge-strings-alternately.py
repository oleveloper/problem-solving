class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        ret = []
        for a, b in zip(word1, word2):
            ret.append(a)
            ret.append(b)
        ret.append(word1[len(word2):])
        ret.append(word2[len(word1):])

        return ''.join(ret)
