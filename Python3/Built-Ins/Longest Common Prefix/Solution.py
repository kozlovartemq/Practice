# https://leetcode.com/problems/longest-common-prefix/
from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 1:
            return strs[0]

        prefix = ""
        array = sorted(strs, key=lambda x: len(x))

        for i in range(len(array[0])):
            j = 1
            while j < len(array):
                if array[0][i] == array[j][i]:
                    if j == len(array) - 1:
                        prefix += array[0][i]
                    j += 1
                else:
                    return prefix
        return prefix


if __name__ == '__main__':
    s = Solution()
    print(s.longestCommonPrefix(['flight', 'flower']))
