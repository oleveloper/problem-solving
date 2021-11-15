class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        i = int(''.join(list(map(str, digits)))) + 1
        return [int(a) for a in str(i)]
