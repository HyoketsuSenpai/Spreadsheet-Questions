class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        ans = []
        for i in range(len(nums)):
            
            while nums[nums[i] - 1] != nums[i]:
                nums[nums[i] - 1],nums[i] = nums[i],nums[nums[i] - 1]
        
        for i in range(len(nums)):
            if i + 1 != nums[i]:
                ans.append(i + 1)
        return ans
            
