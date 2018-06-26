class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums)):
            num = nums[i]
            need = target - num
            if need in nums[i+1:]:
                return [i, nums[i+1:].index(need)+i+1]
        return []
