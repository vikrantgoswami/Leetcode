class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        res.append(1)

        #calculating product of prefixes for each element
        for i in range(1,len(nums)):
            res.append(res[i-1]*nums[i-1])

        #calculating product of suffixes for each element
        suffix_product = nums[-1] #cause there are no elements to left of last element
        for i in range(len(nums)-2,-1,-1):
            res[i] = res[i]*suffix_product
            suffix_product = suffix_product*nums[i]

        return res

        
