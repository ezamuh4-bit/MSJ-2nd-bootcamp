class Solution:
    def search(self, nums: List[int], target: int) -> int:
        num=set(nums)
        if target in num:
            return nums.index(target)
        return -1
