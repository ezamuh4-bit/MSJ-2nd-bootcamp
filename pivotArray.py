class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        smaller = []
        same = []
        larger = []

        for num in nums:
            if num > pivot:
                larger.append(num)
            elif num < pivot:
                smaller.append(num)
            else:
                same.append(num)

        return smaller + same + larger
