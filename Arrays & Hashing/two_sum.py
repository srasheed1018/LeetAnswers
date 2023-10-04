class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i, n in enumerate(nums):
            difference = target-n
            try:
                diffIndex = nums.index(difference)
            except:
                 continue;   
            if ((difference in nums) and (i != diffIndex)):
                return [i, diffIndex]
        return False
