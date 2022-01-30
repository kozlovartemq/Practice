#  https://leetcode.com/problems/roman-to-integer/
class Solution:
    def romanToInt(self, s: str) -> int:
        index_array = []  # list of indexes of "two-element" numbers
        sum_array = []  # list of integers
        two_elements = dict(IV=4, IX=9, XL=40, XC=90, CD=400, CM=900)
        one_element = dict(I=1, V=5, X=10, L=50, C=100, D=500, M=1000)

        def add_wrong_indexes(i: int) -> None:
            index_array.append(i)
            index_array.append(i + 1)

        for i in range(len(s) - 1):  # finding the "two-elements" numbers
            element = s[i] + s[i + 1]
            if element in two_elements.keys():
                add_wrong_indexes(i)
                sum_array.append(two_elements[element])

        for item in [i for i in range(len(s)) if i not in index_array]:  # finding the "one-element" numbers
            if s[item] in one_element.keys():
                sum_array.append(one_element[s[item]])
        return sum(sum_array)
                
