class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for num1 in range(len(nums)):
            for num2 in range(len(nums)):
                if nums[num1] + nums[num2] == target:
                    answer = [num1, num2]
                    return