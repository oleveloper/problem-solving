class Solution:
    def reverseWords(self, s: str) -> str:
        li = list(s)
        l, r = 0, len(s) - 1
        while l < r:
            li[l], li[r] = li[r], li[l]
            l += 1
            r -= 1
        
        words = ''.join(li).split(' ')
        words = words[::-1]
        s = ' '.join(words)
        
        return s
