class Solution:
    def countDigitOccurrences(self, nums: list[int], digit: int) -> int:
        nums=" ".join([str(x) for x in nums])
        nums=Counter(nums)
        return nums[str(digit)]
