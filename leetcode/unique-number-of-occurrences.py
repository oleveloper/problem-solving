class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        m = {}
        arr = sorted(arr)

        for n in arr:
            if n in m:
                m[n] += 1
            else:
                m[n] = 1

        return len(set(m.values())) == len(set(arr))
