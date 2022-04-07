# last-stone-weight
# https://leetcode.com/problems/last-stone-weight

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        while len(stones) > 1:
            x = max(stones)
            stones.remove(x)
            y = max(stones)
            stones.remove(y)
            
            if x != y:
                stones.append(x - y)
            
        if len(stones) == 0:
            return 0
        else:
            return stones[0]
