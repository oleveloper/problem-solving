class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = [65, 69, 73, 79, 85, 97, 101, 105, 111, 117]
        li = [c for c in s if ord(c) in vowels]
        ret = []

        vowel_pointer = 0
        for c in s:
            if vowel_pointer < len(li) and c == li[vowel_pointer]:
                ret.append(li[-1-vowel_pointer])
                vowel_pointer += 1
            else:
                ret.append(c)

        return ''.join(ret)
