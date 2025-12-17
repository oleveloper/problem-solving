from collections import defaultdict

class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        window_frequency = defaultdict(int)
        char_frequency = {char: s1.count(char) for char in set(s1)}
        distinct_need = len(char_frequency)
        
        matched = 0
        left = 0
        for right in range(len(s2)):
            right_char = s2[right]
            window_frequency[right_char] += 1
            if right_char in char_frequency and window_frequency[right_char] == char_frequency[right_char]:
                matched += 1

            if right - left + 1 > len(s1):
                left_char = s2[left]
                if left_char in char_frequency and window_frequency[left_char] == char_frequency[left_char]:
                    matched -= 1
                window_frequency[left_char] -= 1
                left += 1
            
            if right - left + 1 == len(s1):
                if matched == distinct_need:
                    return True

        return False
