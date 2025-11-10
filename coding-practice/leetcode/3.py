# https://leetcode.com/problems/longest-substring-without-repeating-characters/description/
# Longest Substring Without Repeating Characters - Sliding Window

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        window = set()
        left = 0
        max_length = 0

        for right in range(len(s)):
            char = s[right]

            while char in window:
                window.remove(s[left])
                left += 1
            
            window.add(char)
            max_length = max(max_length, right - left + 1)
            
        return max_length
    