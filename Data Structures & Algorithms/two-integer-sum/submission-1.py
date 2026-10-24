class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        a = set()
        for i in range(len(nums)):
            b =target - nums[i]
            if b in nums and i !=nums.index(b):
                a.add(i)
                a.add(nums.index(b))
        return sorted(a)
        