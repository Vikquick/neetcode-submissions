class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for idx_i, i in enumerate(nums):
            res = target - i
            for idx_j, j in enumerate(nums):
                if j == res and idx_j != idx_i:
                    return [idx_i, idx_j]
        