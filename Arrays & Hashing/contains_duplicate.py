class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        mySet = set(nums)
        return not len(mySet) == len(nums)