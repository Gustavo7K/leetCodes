class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        crescente = True
        decrescente = True

        for i in range(len(nums) - 1):
            if nums[i] < nums[i + 1]:
                decrescente = False
            elif nums[i] > nums[i + 1]:
                crescente = False
        return crescente or decrescente