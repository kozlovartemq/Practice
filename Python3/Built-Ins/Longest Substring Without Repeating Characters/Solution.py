# https://leetcode.com/problems/longest-substring-without-repeating-characters/
class Solution:
    def lengthOfLongestSubstring(s: str) -> int:
        substrings = []
        for i in range(len(s) - 1):
            substrings.append(s[i])
            j = i + 1
            while s[j] not in substrings[i]:
                substrings[i] += s[j]
                if j != len(s)-1:
                    j += 1
                else:
                    break
        longest_substring = sorted(substrings, key=len)[-1]
        return len(longest_substring)
