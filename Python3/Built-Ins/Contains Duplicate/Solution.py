class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        if len(set(nums)) == len(nums):
            return False
        else:
            return True
     
    """Without using a set"""
    def containsDuplicate(nums) -> bool:
    for i in range(len(nums) - 1):
        j = i + 1
        while j != len(nums):
            if nums[i] == nums[j]:
                return True
            j += 1
    return False
