class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if nums == []:
            return [-1, -1]
        '''Finding First Position of Element (binary search)'''
        start = 0
        end = len(nums) - 1
        while start <= end - 1:
            if nums[(start + end) // 2] < target:
                start = (start + end) // 2 + 1
            else:
                end = (start + end) // 2
        if nums[start] != target:
            return [-1, -1]
        left = start
       
        '''Finding Last Position of Element'''
        end = len(nums) - 1
        while start <= end - 1:
            if nums[(start + end) // 2] <= target:
                start = (start + end) // 2 + 1
            else:
                end = (start + end) // 2
        if nums[end] != target:
            right = end - 1
        else:
            right = end
        return [left, right]
