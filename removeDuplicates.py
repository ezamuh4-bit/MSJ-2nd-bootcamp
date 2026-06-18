class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n=len(nums)
        nums[:]=list(set(nums))
        after = len (nums)
        nums.sort()
        #nums.extend(["_"] * 3)
        return after
