# 1431. Kids With The Greatest Number Of Candies
# https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/description/

class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        answer = []
        for i in candies:
            answer.append(i + extraCandies == max(i + extraCandies, max(candies)))

        return answer
