class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        #optimal approach invloves 2-pointer approach to find 3sum
        n = len(nums)
        res = []
        nums.sort() #sorting the array to apply 2-pointer approach here

        for i in range(n-2):
            #check if nums[i] is equal to previous value of nums[i]
            if i>0 and nums[i-1] == nums[i]:
                continue
            j = i+1
            k = n-1
            while j<k:
                curr_sum = nums[i] + nums[j] + nums[k]
                if curr_sum > 0:
                    #if sum if greater than 0, we need to decrease it to brin it close to zero
                    #so we decrease k so as to lower down the sum
                    k-=1
                elif curr_sum < 0:
                    #if sum is less than 0, we need to increase the summision value
                    #so we increase j
                    j+=1
                else:
                    #here sum is equal to 0, we got a solution
                    res.append([nums[i], nums[j], nums[k]])
                    #now we move our two pointers
                    j+=1
                    k-=1
                    #but here we might have some duplicates at new j & k indexes
                    #so we gotta handle that as well
                    while j < k and nums[j] == nums[j-1]:
                        j+=1
                    
        return resclass Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        #optimal approach invloves 2-pointer approach to find 3sum
        n = len(nums)
        res = []
        nums.sort() #sorting the array to apply 2-pointer approach here

        for i in range(n-2):
            #check if nums[i] is equal to previous value of nums[i]
            if i>0 and nums[i-1] == nums[i]:
                continue
            j = i+1
            k = n-1
            while j<k:
                curr_sum = nums[i] + nums[j] + nums[k]
                if curr_sum > 0:
                    #if sum if greater than 0, we need to decrease it to brin it close to zero
                    #so we decrease k so as to lower down the sum
                    k-=1
                elif curr_sum < 0:
                    #if sum is less than 0, we need to increase the summision value
                    #so we increase j
                    j+=1
                else:
                    #here sum is equal to 0, we got a solution
                    res.append([nums[i], nums[j], nums[k]])
                    #now we move our two pointers
                    j+=1
                    k-=1
                    #but here we might have some duplicates at new j & k indexes
                    #so we gotta handle that as well
                    while j < k and nums[j] == nums[j-1]:
                        j+=1
                    
        return res