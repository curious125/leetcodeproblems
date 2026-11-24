class Solution:
    def sumOfBeauties(self, nums: list[int]) -> int:
        n = len(nums)
        c = 0
        suffix = [0]*len(nums)
        prefix = [0]*len(nums)
        prefix[0] = nums[0]
        for i in range(1,n):
            prefix[i] = max(prefix[i-1],nums[i-1])
        suffix[n-1] = nums[n-1]
        for i in range(n-2,-1,-1):
            suffix[i] = min(suffix[i+1],nums[i+1])

        for i in range(1,n-1):
            if prefix[i] < nums[i] < suffix[i]:
                c+=2
            elif nums[i-1] < nums[i] < nums[i+1]:
                c+=1
        return c           