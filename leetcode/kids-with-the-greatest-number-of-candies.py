class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        ret = []
        m = max(candies)
        for x in candies:
            ret.append(x + extraCandies >= m)

        return ret
